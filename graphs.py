import plotly
from plotly.graph_objs import Scatter, Layout, Figure


def render_graph(followers_data):
    # prvni graf, tecky
    trace1 = Scatter(
        x=[1, 2, 3, 4],
        y=[1, 2, 0, 2],
        mode='markers',
        marker={
            'size': 25,
            'color': 'rgba(255, 182, 193, .9)',
            'line': {
                'width': 3,
            }
        },
        name='tweets',
        yaxis='y2'
    )

    # prvni graf, tecky
    trace2 = Scatter(
        x=[1, 2, 3, 4],
        y=[4, 3, 1, 2],
        mode='markers',
        marker={
            'symbol': 'square',
            'size': 15,
            'color': 'rgba(120, 255, 193, .9)',
            'line': {
                'width': 2,
            }
        },
        name='likes',
        yaxis='y2'
    )

    # treti graf, souvisla cara
    trace3 = Scatter(
        x=[1, 2, 3, 4],
        y=[40, 50, 60, 54],
        mode='lines',
        name='followers',
    )

    data = [trace1, trace2, trace3]

    layout = Layout(
        title='Double Y Axis Example',
        xaxis=dict(
            zeroline=True,
            showline=True,
         ),
        yaxis=dict(
            title='followers',
            range=[0, 80],
            zeroline=True,
            showline = True
        ),
        yaxis2=dict(
            title='tweets, likes',
            range=[0, 4],
            zeroline=True,
            showline=True,
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )
    '''    
    # tohle by vykreslilo grafy pod sebou    
    data = tools.make_subplots(rows=1, cols=2)    
    data.append_trace(trace1, 1, 1)    
    data.append_trace(trace2, 1, 2)    
    '''
    fig = Figure(data=data, layout=layout)
    plotly.offline.plot(
        fig
           )
