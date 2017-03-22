import pandas
import matplotlib.pyplot as plt

def stacked_bar_chart(df, colorscale="grayscale", y_scale=False):
    
    interval = int(round((235-20)/len(df.columns)))
    if colorscale.lower() in ("grayscale", "greyscale", "bw"):
        colors = ['#%02x%02x%02x' % (i, i, i) for i in range(235, 20, -interval)]
    
    if colorscale in ("bluescale"):
        colors = ['#%02x%02x%02x' % (int(round(i*0.4)), int(round(i*0.8)), i) for i in range(235, 20, -interval)]


    axis = df.plot.bar(stacked=True, linewidth=0, width=1.0, color=colors)
    if y_scale:
        axis.set_ylim(0,y_scale)
    x_start, x_end = axis.get_xlim()
    x_range = range(int(x_start), int(x_end), 10)
    tick_range = range(int(min(df.index)+1), int(max(df.index)+1), 10)
    axis.xaxis.set_ticks(x_range)
    axis.set_xticklabels(tick_range)
    plt.show()
