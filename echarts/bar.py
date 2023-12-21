from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode

def render_basic_bar(xData, value):
    options = {
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
            "type": 'shadow'
            }
        },
        "xAxis": {
            "type": "category",
            "data": xData,
            "name": "Sentiment Score",
            "nameLocation": "middle",
            "nameGap": 30,
            "nameTextStyle": {
                "fontSize": 15,
                "fontWeight": "bold"
            },
        },
        "yAxis": {
            "type": "value",
            "name": "Month",
            "nameLocation": "middle",
            "nameGap": 30,
            "nameTextStyle": {
                "fontSize": 15,
                "fontWeight": "bold"
            },
        },
        "series": [
            {
                "data": value, 
                "type": "bar",
                "itemStyle": {
                    "color": 'blue'
                },
                "showBackground": "true",
                "backgroundStyle": {
                    "color": 'rgba(180, 180, 180, 0.2)'
                }
            }
        ],
    }
    st_echarts(options=options, height="500px")

def render_vertical_rating(value, key):
    options = {
        "title": {
            "text": f'Rating Distribution (Total: {sum(value)})',
            "left": 'center'
        },
        "xAxis": {
            "max": max(value) + 20,
        },
        "yAxis": {
            "type": "category",
            "data": ["5-star", "4-star", "3-star", "2-star", "1-star"],
            "splitLine": {
                "show": "false"
            },
            "inverse": "true"
        },
        "series": [
            {
                "type": 'bar',
                "label": {
                    "position": 'right',
                    "show": "true"
                },
                "data": value,
                "itemStyle": {
                    "color": 'blue'
                },
                "showBackground": "true",
                "backgroundStyle": {
                    "color": 'rgba(180, 180, 180, 0.2)'
                }
            },
        ],
        "legend": {
            "show": "true"
        },
    }
    st_echarts(
        options=options, key=key
    )

def render_horizontal_stacking(yData, posData, negData, neuData):
    options = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "shadow"  # 'shadow' as default; can also be 'line' or 'shadow'
            }
        },
        "legend": {},
        "grid": {
            "left": "3%",
            "right": "4%",
            "bottom": "3%",
            "containLabel": True
        },
        "xAxis": {
            "type": "value"
        },
        "yAxis": {
            "type": "category",
            "data": yData
        },
        "series": [
            {
                "name": 'Positive',
                "type": 'bar',
                "stack": 'total',
                "label": {
                    "show": False 
                },
                "emphasis": {
                    "focus": 'series'
                },
                "itemStyle": {
                    "color": 'green'
                },
                "data": posData
            },
            {
                "name": 'Negative',
                "type": 'bar',
                "stack": 'total',
                "label": {
                    "show": False
                },
                "emphasis": {
                    "focus": 'series'
                },
                "itemStyle": {
                    "color": 'red'
                },
                "data": negData
            },
            {
                "name": 'Neutral',
                "type": 'bar',
                "stack": 'total',
                "label": {
                    "show": False
                },
                "emphasis": {
                    "focus": 'series'
                },
                "itemStyle": {
                    "color": 'blue'
                },
                "data": neuData
            }
        ]
    }

    st_echarts(
        options=options
    )

def render_vertical_bar(data, value, name, max):
    options = {
        "grid": {
            "left": "8%",
            "right": "8%",
            "bottom": "3%",
            "containLabel": True
        },
        "xAxis": {
            "max": max,
        },
        "yAxis": {
            "type": "category",
            "data": data,
            "splitLine": {
                "show": "false"
            },
            "inverse": "true",
            "name": name
        },
        "series": [
            {
                "type": 'bar',
                "label": {
                    "position": 'right',
                    "show": "true"
                },
                "data": value,
                "itemStyle": {
                    "color": 'blue'
                },
                "showBackground": "true",
                "backgroundStyle": {
                    "color": 'rgba(180, 180, 180, 0.2)'
                }
            },
        ],
        "legend": {
            "show": "true"
        },
    }
    st_echarts(
        options=options, height='400px'
    )

# Update ST_GAUGE_DEMOS to include specific values for render_gauge
ST_BAR_DEMOS = {
    "Bar: Basic Bar": (
        render_basic_bar
    ),
    "Bar: Vertical Rating": (
        render_vertical_rating   
    ),
    "Bar: Horizontal Stacked Bar": (
        render_horizontal_stacking   
    ),
    "Bar: Basic Vertical Bar": (
        render_vertical_bar   
    ),
}