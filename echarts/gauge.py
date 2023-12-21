from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode


def render_gauge(value, rank, key):
    options = {
        "series": [
            {
            "type": "gauge",
            "startAngle": 180,
            "endAngle": 0,
            "radius": '90%',
            "min": 0,
            "max": 5,
            "splitNumber": 4,
            "axisLine": {
                "show": "false",
                "lineStyle": {
                "width": 6,
                "color": [
                    [0.25, '#FF6E76'],
                    [0.5, '#FDDD60'],
                    [0.75, '#58D9F9'],
                    [1, '#7CFFB2']
                ]
                }
            },
            "pointer": {
                "length": '12%',
                "width": 10,
                "offsetCenter": [0, '-60%'],
                "itemStyle": {
                "color": 'auto'
                }
            },
            "splitLine": {
                "length": 20,
                "lineStyle": {
                "color": 'auto',
                "width": 5
                }
            },
            "axisLabel": {
                "color": "white",
                "show": "false"
            },
            "title": {
                "offsetCenter": [0, '20%'],
                "fontSize": 20,
                "fontWeight": "bold"
            },
            "detail": {
                "fontSize": 30,
                "offsetCenter": [0, '-35%'],
                "valueAnimation": "true",
                "color": 'inherit'
            },
            "data": [
                {
                "value": value,
                "name": f"Rank: #{rank}"
                }
            ]
            }
        ]
    }
    st_echarts(
        options=options, key=key
    )

def render_gauge_full_circle(data):
    options = {
        "series": [
            {
            "type": 'gauge',
            "startAngle": 90,
            "endAngle": -270,
            "pointer": {
                "show": False
            },
            "progress": {
                "show": "true",
                "overlap": "false",
                "roundCap": "true",
                "clip": "false",
                "itemStyle": {
                "borderWidth": 1,
                "color": 'blue'
                }
            },
            "axisLine": {
                "lineStyle": {
                "width": 20
                }
            },
            "splitLine": {
                "show": False,
                "distance": 0,
                "length": 10
            },
            "axisTick": {
                "show": False
            },
            "axisLabel": {
                "show": False,
                "distance": 50
            },
            "data": [
                {
                    "value": data,
                    "detail": {
                        "offsetCenter": ['0%', '0%']
                    }
                }
            ],
            "title": {
                "fontSize": 14
            },
            "detail": {
                "fontSize": 120,
            }
        }]
    }
    st_echarts(options=options, height="400px")

# Update ST_GAUGE_DEMOS to include specific values for render_gauge
ST_GAUGE_DEMOS = {
    "Gauge: Simple Gauge": (
        render_gauge    
    ),
    "Gauge: Full Circle Gauge": (
        render_gauge_full_circle
    )
}