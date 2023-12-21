from streamlit_echarts import st_echarts

def render_stacked_line_chart_sentiment(xData, posData, negData, neuData):
    options = {
        "tooltip": {"trigger": "axis"},
        "grid": {
            "left": '3%',
            "right": '4%',
            "containLabel": "true"
        },
        "legend": {"data": ["Positive", "Negative", "Neutral"]},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "name": "Month",
            "nameLocation": "middle",
            "nameGap": 30,
            "nameTextStyle": {
                "fontSize": 15,
                "fontWeight": "bold"
            },
            "type": "category",
            "boundaryGap": False,
            "data": xData,
        },
        "yAxis": {
            "type": "value",
            "name": "Sentiment Trend",
            "nameLocation": "middle",
            "nameGap": 30,
            "nameTextStyle": {
                "fontSize": 15,
                "fontWeight": "bold"
            },
        },
        "series": [
            {
                "name": "Positive",
                "type": "line",
                "smooth": "true",
                "data": posData,
                "itemStyle": {
                    "color": 'green'
                },
            },
            {
                "name": "Negative",
                "type": "line",
                "smooth": "true",
                "data": negData,
                "itemStyle": {
                    "color": 'red'
                },
            },
            {
                "name": "Neutral",
                "type": "line",
                "smooth": "true",
                "data": neuData,
                "itemStyle": {
                    "color": 'blue'
                },
            },
        ],
    }
    st_echarts(options=options, height='400px')


ST_LINE_DEMOS = {
    "Line: Stacked Line Chart": (
        render_stacked_line_chart_sentiment
    ),
}