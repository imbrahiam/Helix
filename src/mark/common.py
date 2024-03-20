from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import numpy as np
import openpyxl
import json
import os

def write_csv(df, path):
    df.to_csv(path, index=True, header=True)
    
def open_csv(path):
    return pd.read_csv(path)

def open_json(path):
    return json.load(open(path))

def get_date():
    return str(dt.now().strftime("%Y-%m-%d")) #-%H-%M-%S

def save_map(m, output_path):
    m.save(f"{output_path}\map.html")

def save_plot(plt, direction, output_path):
    return "Image saved" if plt.savefig(f'{output_path}\\{direction}barplot_{get_date()}.png', dpi=1200, bbox_inches='tight') else None

def set_output(fname, folder = 'output'):
    path = f'{folder}' # \\{owner}
    save_path = f'{path}/{fname}.csv'

    if not os.path.isdir(path):
        os.mkdir(path)

    return path, save_path

def get_rwdp(i): # Raw Data Path
    rdata = '../raw_data/Perfil_EmpresasImpo_2022_WEB.xlsx' if i == 0 else '../raw_data/IMP_2023_WEB.xlsx'
    return rdata

def draw_hplot(x, y, dftp, colname):
    
    if len(dftp.columns) == 1:
        xlabel = x
        ylabel = y

        # Spliting data for x and y.
        names = dftp.index
        values = dftp[colname]
        lim = values[-1] * 1.1

        # Setting font
        plt.rcParams['font.family'] = 'DejaVu Sans'
        plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

        # Set the style of the axes and the text color
        plt.rcParams['axes.edgecolor']='#333F4B'
        plt.rcParams['axes.linewidth']=0.8
        plt.rcParams['xtick.color']='#333F4B'
        plt.rcParams['ytick.color']='#333F4B'
        plt.rcParams['text.color']='#333F4B'

        # Numeric placeholder for the y axis
        my_range=list(range(1, len(dftp.index)+1))

        fig, ax = plt.subplots(figsize=(5,3.5))

        # Create for each expense type an horizontal line that starts at x = 0 with the length 
        # represented by the specific expense percentage value.
        plt.hlines(y=my_range, xmin=0, xmax=values, color='#007ACC', alpha=0.2, linewidth=5)

        # create for each expense type a dot at the level of the expense percentage value
        plt.plot(values, my_range, "o", markersize=5, color='#007ACC', alpha=0.6)

        # set labels
        ax.set_xlabel(xlabel, fontsize=15, fontweight='black', color = '#333F4B')
        ax.set_ylabel('')

        # set axis
        ax.tick_params(axis='both', which='major', labelsize=12)
        plt.yticks(my_range, dftp.index)

        # add an horizonal label for the y axis 
        fig.text(-0.23, 0.96, ylabel, fontsize=15, fontweight='black', color = '#333F4B')

        # change the style of the axis spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.spines['left'].set_bounds((1, len(my_range)))
        ax.set_xlim(0, lim)

        ax.spines['left'].set_position(('outward', 8))
        ax.spines['bottom'].set_position(('outward', 5))

        return fig, ax
    
    else:
        return None
    
def draw_vplot(x, y, dftp, colname, title):
    
    if len(dftp.columns) == 1:
        xlabel = x
        ylabel = y
        # Vertical Bars Plot
        fig, ax = plt.subplots()
        # dftp = df[:10] # Top 10

        # Save the chart so we can loop through the bars below.
        bars = ax.bar(
            x=np.arange(dftp.size),
            height=dftp[colname],
            tick_label=dftp.index
        )

        # Axis formatting.
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('#DDDDDD')
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='#EEEEEE')
        ax.xaxis.grid(False)

        # Add text annotations to the top of the bars.
        bar_color = bars[0].get_facecolor()
        for bar in bars:
          ax.text(
              bar.get_x() + bar.get_width() / 2,
              bar.get_height() + 0.3,
              round(bar.get_height(), 1),
              horizontalalignment='center',
              verticalalignment='bottom',
              color=bar_color,
              weight='bold'
          )

        # Add labels and a title.
        ax.set_xlabel(xlabel, labelpad=15, color='#333333')
        ax.set_ylabel(ylabel, labelpad=15, color='#333333')
        ax.set_title(title, pad=15, color='#333333',
                     weight='bold')

        ax.margins(0.01, None)
        fig.autofmt_xdate()
        fig.tight_layout()
        
        return fig, ax
    
    else:
        return None
    