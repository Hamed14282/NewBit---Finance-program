import os
import csv
import glob
import sys

import customtkinter
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.figure import Figure
import logtest
import pandas as pd

logtest.Usertest.choose()
user = logtest.Usertest.get_user()

def get_all_months():
    months = set()

    files = glob.glob(f"data/{user}/*/*_savings.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_savings.csv", "")
        months.add(month)

    return sorted(months, key=lambda x: datetime.strptime(x, "%m.%Y"))

def categories_distribution(month=None):
    plt.style.use('seaborn-v0_8-darkgrid')

    if month is None:
        months = get_all_months()
        all_dfs = []
        for m in months:
            filename = f"data/{user}/{m}_expenses.csv"
            df = pd.read_csv(filename, header=None)
            df.columns = ["A", "B", "C", "D"]
            all_dfs.append(df)
        df = pd.concat(all_dfs)
    else:
        filename = f"data/{user}/{month}_expenses.csv"
        df = pd.read_csv(filename, header=None)
        df.columns = ["A", "B", "C", "D"]

    df_pie = df.groupby('D', as_index=False)['A'].sum()
    df_pie = df_pie.set_index('D')

    fig, ax = plt.subplots(facecolor="#212121")
    df_pie["A"].plot(
        kind="pie",
        ax=ax,
        labels=None,
        autopct=lambda pct: f"{pct:.1f}%" if pct > 5 else ""
    )

    total = df_pie["A"].sum()
    legend_labels = [f"{cat} ({val/total*100:.1f}%)" for cat, val in zip(df_pie.index, df_pie["A"])]


    ax.set_title("Categories")
    ax.legend(legend_labels, loc="upper left", bbox_to_anchor=(-0.3, 1), color='#d6d6d6')
    ax.set_ylabel("")
    return fig

categories_distribution()
