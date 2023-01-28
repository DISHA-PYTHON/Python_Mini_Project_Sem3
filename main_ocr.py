import os # to handle file names
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from easyocr import Reader # OCR to extract text from image
reader_en = Reader(['en']) 
import io # python input output handling
from PIL import Image # to read images in python 
import PySimpleGUI as sg # for GUI
from numpy import * # to handle math expressions 
import numexpr as ne # to evaluate math expressions

def vis_calc():
    # GUI Layout is stored in a 2D list, storing the grid of objects in the window
    layout = [
        [sg.Image(key="-IMAGE-")], 
        [sg.Text("Input"),sg.Text('',font=('Helvetica',18),background_color='white',text_color='black',key='input')],
        [sg.Text("Output"),sg.Text('',font=('Helvetica',18),background_color='white',text_color='black',key='output')],
        [sg.Text("Image File"),sg.Input(size=(25, 1), key="-FILE-"),sg.FileBrowse(), 
        sg.Button("Load Image"),]
    ]

    # Gui application
    window = sg.Window("Visual Calculator",layout=layout,finalize=True,element_justification="center",font="Helvetica 18")
    
    # Make Infinite Loop
    while True:
        # Detect button presses from gui
        button, values = window.read()

        if button == 'Quit' or button == None:
            break
        elif button == "Load Image":
            filename = values["-FILE-"] # load filename from file browse option in GUI
            if os.path.exists(filename): # check if file exists and proceed
                
                image = Image.open(filename) # open the image file
                image.thumbnail((400, 400)) # resize image into 400x400 pixels

                # To display the image, we can convert the file into an byte stream using io.BytesIO,
                # which lets us save the image in computer memory.
                # Then we can use the image stored in memory to display it on the gui using the window.update() method
                bio = io.BytesIO() # byte stream object 
                image.save(bio, format="PNG") # store image in the memory as a stream of bytes (bio variable)
                window["-IMAGE-"].update(data=bio.getvalue()) # bio.getvalue() retrieves image from the memory and then we can update the gui

                # read text from image
                text = reader_en.readtext(filename,paragraph=True)[0][1] # use OCR reader to retrieve text from image
                window.FindElement('input').Update(text) # display text on the GUI

                # evaluate expression and write answer
                answer = ne.evaluate(text)
                window.FindElement('output').Update(answer) # show answer to math expression on the GUI

    window.close() #Closes window. Users can safely call even if window has been destroyed.
    # Should always call when done with a window so that resources are properly freed up within your thread.

if __name__=="__main__":  #file is being run directly (). GUI should not load directly after importing the file. 
	vis_calc() # then this func is being executed
    ##(used to execute some code only if the file was run directly, and not imported.)