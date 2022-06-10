import pandas as pd
import plotly.express as px

# x = [10,30,40]
# print(pd.DataFrame(x))

df = pd.read_csv("Teacher refrence/data.csv")

graph = px.bar(df , x = 'Country' , y = 'InternetUsers')
graph.show()