import csv
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.figure import Figure
import pandas as pd
from matplotlib import style 

#  set the colour
plt.style.use('ggplot')

# making name as current month
now = datetime.now()
current_month = f"{now.month}.{now.year}"
filename = f"data/{current_month}_expenses.csv"

# read file
df = pd.read_csv(filename, header=None)
df.columns = ["A", "B", "C", "D"]

# group table
df_pie = df.groupby('D', as_index=False)['A'].sum()
df_pie = df_pie.set_index('D')

# pie chart
df_pie["A"].plot(
    kind="pie",          # тип діаграми — pie
    autopct="%1.1f%%",   # формат підписів секторів (проценти з однією цифрою після коми)
    title="Expenses per Category"  # заголовок
)
plt.ylabel("")
plt.show()
