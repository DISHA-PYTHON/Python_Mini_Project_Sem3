import PySimpleGUI as sg # for GUI
import matplotlib.pyplot as plt # for plotting
import numpy as np # for handling arrays etc
from numpy import * # for handling arrays etc
from numexpr import evaluate # to evaluate calculator input


# Following lines are directly referenced from
# PySimpleGui demo programs for displaying matplotlib graph inside GUI
# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Matplotlib.py
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib 
matplotlib.use("TkAgg") # Use Tkinter Agg

def pack_figure(graph, figure):
    canvas = FigureCanvasTkAgg(figure, graph.Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side='top', fill='both', expand=1)
    return plot_widget
# ---------------- end of lines ----------------

def graph_calc():

    def plot_figure(equation):

        fig = plt.figure(1) # create a blank figure
        ax = plt.gca() # get current axes of the figure

        # evaluate the equation to be plotted
        # this creates the numpy array of y values
        # where every value in y array is a function of values in the x array
        y = evaluate(equation) 

        if overlay is False: # no overlay
            ax.cla() # clear the current axes if no overlay
        
        ax.set_xlabel("X axis") # labeling x axis
        ax.set_ylabel("Y axis") # labeling y axis

        plt.plot(x, y, color=color, linewidth=width) # finally plot figure with all plotting parameters
        
        fig.canvas.draw() # render figure into canvas

    colorlist = ['black','blue','orange','green','red','purple','brown','pink','gray','olive','cyan']
    widthlist = [1,2,3,4,5,6,7,8,9,10]

    # default plotting values
    equation = '3*x+4' # equation to be plotted
    xmin = -10 # left limit of plotting range
    xmax = 10 # right limit of plotting range
    npoints = 1000 # number of points in the x and y arrays
    color = colorlist[0]  # color of the graph
    width = 1 # line width of the graph
    overlay = True # option whether to overlay graph or not

    # GUI Layout is stored in a 2D list, storing the grid of objects in the window
    ipsz = (10,20)
    layout = [
        [sg.Text("y="), sg.Input(f'{equation}',key="equation")],
        [sg.Text("xmin"),sg.Input(f'{xmin}',key="xmin",size=ipsz),sg.Text("xmax"), sg.Input(f'{xmax}',key="xmax",size=ipsz),sg.Text("#points"), sg.Input(f'{npoints}',key="npoints",size=ipsz)],
        [sg.Text("color"),sg.Combo(colorlist,key="color",default_value=color,readonly=True),
        sg.Text("width"),sg.Combo(widthlist,key="width",default_value=width,readonly=True)],
        [sg.Graph((640, 480), (0, 0), (640, 480), key='Graph')],
        [sg.Button("Plot"),sg.Checkbox("overlay",default=overlay,key="overlay")],
    ]

    # Gui application
    window = sg.Window("Graphing Calculator", layout=layout, finalize=True, element_justification="center", font="Helvetica 18")

    # Initialize plot to be shown on the gui
    graph = window["Graph"]
    plt.ioff() # disable interactive mode in matplotlib
    fig = plt.figure(1) # create a blank figure
    ax = plt.subplot(111) # create XY axis
    x = np.linspace(xmin,xmax,num=npoints) # create array of x coordinates of all points in the graph

    # Add initialized plot to gui
    pack_figure(graph, fig)

    # Make Infinite Loop
    while True:
        # Button Values
        button, value = window.Read()

        # Check Press Button Values
        if button == 'Plot':
            # interpret equation
            equation = value["equation"]

            # update plotting options
            xmin = float(value["xmin"])
            xmax = float(value["xmax"])
            npoints = int(eval(value["npoints"]))
            x = np.linspace(xmin,xmax,num=npoints)
            color = value["color"]
            width = value["width"]
            overlay = value["overlay"]

            # update figure
            plot_figure(equation)

        # close the window
        elif button == 'Quit' or button == None:
            break

    window.close()

if __name__=="__main__":
	graph_calc()
    ##(used to execute some code only if the file was run directly, and not imported.)