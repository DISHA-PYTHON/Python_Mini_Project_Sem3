import PySimpleGUI as sg # for GUI
from main_calculator import *
from main_plotting import *
from main_ocr import *

# GUI Layout is stored in a 2D list, storing the grid of objects in the window
layout = [
	[sg.Button('Scientific Calculator')],
    [sg.Button('Graphical Calculator')],
    [sg.Button('Visual Calculator')],
]

# Gui application
window = sg.Window('Calculator', layout=layout, auto_size_buttons=True, font="Helvetica 18",)

# Make Infinite Loop
while True:
    # Detect button presses in the window
    button, _ = window.Read()

    if button == 'Scientific Calculator':
        sci_calc()
    elif button == 'Graphical Calculator':
        graph_calc()
    elif button == 'Visual Calculator':
        vis_calc()
    # close the window
    elif button == 'Quit' or button == None:
        break

window.close() #Closes window. Users can safely call even if window has been destroyed.
    # Should always call when done with a window so that resources are properly freed up within your thread.
