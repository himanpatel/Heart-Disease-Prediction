import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input
import pandas as pd
import plotly.graph_objects as go

excel_file = (r'C:\Users\Himanshu Patel\Downloads\cardiovascular-disease-dataset\Cleansed_MyData.csv')
ReadDataFromCsv = pd.read_csv(excel_file)
df=pd.DataFrame(ReadDataFromCsv)

SelectAllColumns =  list(ReadDataFromCsv.columns)
features = SelectAllColumns
opts = [{'label' : i, 'value' : i} for i in features]

pd.DataFrame({'CARDIO_DISEASE': [1,0]})

WightTrueGroupWhere = ReadDataFromCsv.loc[ReadDataFromCsv['CARDIO_DISEASE'] == 1]
WightFalseGroupWhere = ReadDataFromCsv.loc[ReadDataFromCsv['CARDIO_DISEASE'] == 0]

WightTrueGroup = WightTrueGroupWhere.groupby(["PHYSICAL_ACTIVITY"], as_index=False)["CARDIO_DISEASE"].count()
WightFalseGroup = WightFalseGroupWhere.groupby(["PHYSICAL_ACTIVITY"], as_index=False)["CARDIO_DISEASE"].count()

WightTrueGroup.columns = ['PHYSICAL_ACTIVITY', 'CARDIO_DISEASE_TRUE']
WightFalseGroup.columns = ['PHYSICAL_ACTIVITY', 'CARDIO_DISEASE_FALSE']

WightTrueGroup.append(WightFalseGroup)

WightFalseGroup.drop('PHYSICAL_ACTIVITY', axis=1, inplace=True)

CombinedColumns = pd.concat([WightTrueGroup, WightFalseGroup], axis = 1)


print(CombinedColumns.head(10))
trace_weight = go.Figure(
    data=[
        go.Bar(
            name="Positive",
            x=CombinedColumns["PHYSICAL_ACTIVITY"],
            y=CombinedColumns["CARDIO_DISEASE_TRUE"],
            offsetgroup=0,
        ),
        go.Bar(
            name="Negative",
            x=CombinedColumns["PHYSICAL_ACTIVITY"],
            y=CombinedColumns["CARDIO_DISEASE_FALSE"],
            offsetgroup=1,
        ),
    ],
    layout=go.Layout(
        title="Cardiovascular Disease Vs Physically Active",
        yaxis_title=""
    )
)

#trace_weight =  go.Bar(name='Cardio Positive', x=list(CombinedColumns.WEIGHT), y=list(CombinedColumns.CARDIO_DISEASE_TRUE))

trace_Cholestrol = go.Bar(x=list(ReadDataFromCsv.CHOLESTEROL),
                     y=list(ReadDataFromCsv.CARDIO_DISEASE))

external_stylesheets =[
    'https://dash-gallery.plotly.host/dash-study-browser/assets/custom.css',
    'https://dash-gallery.plotly.host/dash-study-browser/assets/base.css'
]
print(SelectAllColumns)
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id="WeightGraph",
                figure= trace_weight
            )
        ],className="six columns")
    ]),
    html.Div([
        html.Div([
            dcc.Graph(
               id="CholestrolGraph",
               figure={
                   "data": [trace_Cholestrol],
                   "layout": {
                       "title": "Cholestrol Graph"
                  }
              }
          )
       ],className="six columns")
])
], className="row")

if __name__ == "__main__":
    app.run_server(debug=True,port=8052)