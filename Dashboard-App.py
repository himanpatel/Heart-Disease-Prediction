import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import pandas as pd
import plotly.graph_objects as go

excel_file = (r'C:\Users\Himanshu Patel\Downloads\cardiovascular-disease-dataset\Cleansed_MyData.csv')
ReadDataFromCsv = pd.read_csv(excel_file)

SelectAllColumns = list(ReadDataFromCsv.columns)
features = SelectAllColumns
opts = [{'label': i, 'value': i} for i in features]
opts = opts[1:12]
# trace_close = go.Scatter(x=list(ReadDataFromCsv.AP_HIGH),
#                         y=list(ReadDataFromCsv.CARDIO_DISEASE),
#                         name="Physical Activity Graph",
#                         line=dict(color="#ff0000"))


external_stylesheets = [
    'https://dash-gallery.plotly.host/dash-study-browser/assets/custom.css',
    'https://dash-gallery.plotly.host/dash-study-browser/assets/base.css'
]
print(SelectAllColumns)
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

# App Layout
app.layout = html.Div(
    children=[
        # Error Message
        html.Div(id="error-message"),
        # Top Banner
        html.Div(
            className="study-browser-banner row",
            children=[
                html.H2(className="h2-title", children="Heart Disease Dashboard"),
                html.Div(
                    className="div-logo",
                    children=html.Img(
                        className="logo",
                        src='data:image/png;base64,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'
                    ),
                ),
                html.H2(className="h2-title-mobile", children="Heart Disease Dashboard"),
            ],
        ),
        # Body of the App
        html.Div(
            className="row app-body",
            children=[
                # User Controls
                html.Div(
                    className="four columns card",
                    children=[
                        html.Div(
                            className="bg-white user-control",
                            children=[
                                 html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Select Attribute"),
                                        dcc.Dropdown(id="x-axis-dropdown", options=opts, value=features[1]),
                                    ],
                                ),
                                 html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Filter Attribute"),
                                        dcc.Dropdown(id="filter-dropdown", options=opts, value=features[2]),
                                    ],
                                ),
                                 html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Filter Attribute Values"),
                                        dcc.Dropdown(id="filter-dropdown-values", options=[]),
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                # Graph
                html.Div(
                    className="eight columns card-left",
                    children=[
                        html.Div(
                            className="bg-white",
                            children=[
                                html.H5("Heart data plot"),
                                dcc.Graph(id="heart-data-plot"),
                            ],
                        )
                    ],
                ),
                dcc.Store(id="error", storage_type="memory"),
            ],
        ),
    ]
)

@app.callback(dash.dependencies.Output('filter-dropdown-values', 'options'),
              [dash.dependencies.Input('filter-dropdown', 'value')])
def update_filter_values(input_filter_value):
    opts = ReadDataFromCsv[input_filter_value].unique().tolist()
    options = [{'label': i, 'value': i} for i in opts]
    value = opts[0]
    #return [{'label': i, 'value': i} for i in ReadDataFromCsv[input_filter_value].unique()]

    return [{'label': i, 'value': i} for i in opts]
    """return {
        options: options,
        value: value
    }"""

"""@app.callback(dash.dependencies.Output('heart-data-plot', 'figure'),
             [dash.dependencies.Input('x-axis-dropdown', 'value')])
def update_attribute(input_value):
        WightTrueGroupWhere = ReadDataFromCsv.loc[ReadDataFromCsv['CARDIO_DISEASE'] == 1]
        WightFalseGroupWhere = ReadDataFromCsv.loc[ReadDataFromCsv['CARDIO_DISEASE'] == 0]

        WightTrueGroup = WightTrueGroupWhere.groupby([input_value], as_index=False)[
            "CARDIO_DISEASE"].count()
        WightFalseGroup = WightFalseGroupWhere.groupby([input_value], as_index=False)[
            "CARDIO_DISEASE"].count()

        print(WightTrueGroup)
        print(WightFalseGroup)
        WightTrueGroup.columns = [input_value, 'CARDIO_DISEASE_TRUE']
        WightFalseGroup.columns = [input_value, 'CARDIO_DISEASE_FALSE']

        WightTrueGroup.append(WightFalseGroup)

        WightFalseGroup.drop(input_value, axis=1, inplace=True)

        CombinedColumns = pd.concat([WightTrueGroup, WightFalseGroup], axis=1)

        print(CombinedColumns.head(10))
        data = []
        trace_PA_True = go.Bar(
            name="Positive",
            x=CombinedColumns[input_value],
            y=CombinedColumns["CARDIO_DISEASE_TRUE"],
            offsetgroup=0,
        )

        trace_PA_False = go.Bar(
            name="Negative",
            x=CombinedColumns[input_value],
            y=CombinedColumns["CARDIO_DISEASE_FALSE"],
            offsetgroup=1,
        )

        data.append(trace_PA_False)
        data.append(trace_PA_True)
        layout = {"title": input_value + " vs Cardio Disease graph"}

        return {
            "data": data,
            "layout": layout
        }"""


@app.callback(dash.dependencies.Output('heart-data-plot', 'figure'),
              [dash.dependencies.Input('x-axis-dropdown', 'value'),
               dash.dependencies.Input('filter-dropdown', 'value'),
               dash.dependencies.Input('filter-dropdown-values', 'value')])


def update_filter_attribute(input_value,input_filter,input_filter_value):



        WightTrueGroupWhere = ReadDataFromCsv.loc[ReadDataFromCsv['CARDIO_DISEASE'] == 1]
        WightFalseGroupWhere = ReadDataFromCsv.loc[ReadDataFromCsv['CARDIO_DISEASE'] == 0]

        if  input_filter != "None" and input_value != "None" and input_filter_value != "None":
            print("if loop 3 conditions")
            WightTrueGroup = WightTrueGroupWhere.groupby([input_value,input_filter], as_index=False)["CARDIO_DISEASE"].count()
            WightFalseGroup = WightFalseGroupWhere.groupby([input_value,input_filter], as_index=False)["CARDIO_DISEASE"].count()
            WightTrueGroup = WightTrueGroup.loc[WightTrueGroup[input_filter] == input_filter_value]
            WightFalseGroup = WightFalseGroup.loc[WightFalseGroup[input_filter] == input_filter_value]
        elif input_value != "None":
             print("else conditions")
             WightTrueGroup = WightTrueGroupWhere.groupby([input_value], as_index=False)["CARDIO_DISEASE"].count()
             WightFalseGroup = WightFalseGroupWhere.groupby([input_value], as_index=False)["CARDIO_DISEASE"].count()

        if  input_filter != "None" and input_value != "None":
            print("if loop 2 conditions")
            WightTrueGroup.columns = [input_value,input_filter, 'CARDIO_DISEASE_TRUE']
            WightFalseGroup.columns = [input_value,input_filter, 'CARDIO_DISEASE_FALSE']
        else:
            print("2nd else conditions")
            WightTrueGroup.columns = [input_value, 'CARDIO_DISEASE_TRUE']
            WightFalseGroup.columns = [input_value, 'CARDIO_DISEASE_FALSE']



        WightTrueGroup.append(WightFalseGroup)

        WightFalseGroup.drop(input_value, axis=1, inplace=True)

        CombinedColumns = pd.concat([WightTrueGroup, WightFalseGroup], axis=1)

        print(CombinedColumns.head(10))
        data = []
        trace_PA_True = go.Bar(
               name="Positive",
               x=CombinedColumns[input_value],
               y=CombinedColumns["CARDIO_DISEASE_TRUE"],
               offsetgroup=0,
        )

        trace_PA_False = go.Bar(
            name="Negative",
            x=CombinedColumns[input_value],
            y=CombinedColumns["CARDIO_DISEASE_FALSE"],
            offsetgroup=1,
        )

        data.append(trace_PA_False)
        data.append(trace_PA_True)
        layout = {"title" : input_value+" vs Cardio Disease graph"}

        return {
        "data": data,
        "layout": layout
        }





if __name__ == "__main__":
    app.run_server(debug=True)
