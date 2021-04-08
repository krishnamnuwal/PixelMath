import plotly.graph_objects as go
import plotly
import csv

import pandas as pd 

file=pd.read_csv("data.csv")
student=file.loc[file['student_id']=='TRL_xsl']
z=(student.groupby('level')['attempt'].mean())
print(z)
figure=go.Figure(go.Bar(y=z,x=['level1','level2','level3','level4'],orientation='v'))
plotly.offline.plot(figure)
# file=pd.read_csv("data.csv")
# z=(file.groupby('level')['attempt'].mean())
# print(z)
# figure=go.Figure(go.Bar(x=z,y=['level1','level2','level3','level4'],orientation='h'))
# plotly.offline.plot(figure)
# #figure.show()
# #print(file)