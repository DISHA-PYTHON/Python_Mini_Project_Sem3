# Import python libraries
import PySimpleGUI as sg # for GUI
from numpy import * # for scientific calculator functionality
from numexpr import evaluate # to evaluate calculator input


def sci_calc():
	# GUI Layout is stored in a 2D list, storing the grid of objects in the window
	layout = [
		[sg.Text('',size=(28, 1),font=('Helvetica', 18),background_color='white',text_color='black',key='input')],
		[sg.Button('arccos('),sg.Button('arcsin('),sg.Button('arctan(')],
		[sg.Button('cos('),sg.Button('sin('),sg.Button('tan(')],
		[sg.Button('sqrt('),sg.Button('exp('),sg.Button('log(')],
		[sg.Button('('),sg.Button(')'),sg.Button('pi'),sg.Button('e')],
		[sg.Button('Clear'), sg.Button('%'), sg.Button('«'), sg.Button('**')],
		[sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
		[sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
		[sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
		[sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
		]

	# Gui application [window is the main object of the GUI which stores everything like layout etc]
	window = sg.Window('Scientific Calculator', layout=layout, default_button_element_size=(6,1), auto_size_buttons=False, font="Helvetica 18",)

	# Output of the Calculator
	Result = ''

	# Make Infinite Loop
	while True:
		# Detect button presses in the window
		button, _ = window.Read()
			
		# Check Press Button Values
		if button == 'Clear':
			Result = '' # make result back to empty string
			window.find_element('input').Update(Result)
		elif button=='«':
			Result = Result[:-1] # deleting last character of result
			window.find_element('input').Update(Result)
		elif len(Result) == 50 : # maximum input limit for calculator
			pass 
		
		# Results
		elif button == '=':
			answer = evaluate(Result) # this evaluates the string and calculates answer of the expression
			answer = str(round(float(answer),6)) # rounding answer to 6 decimal places and converting into string
			window.find_element('input').Update(answer) # update the display with answer
			Result = answer
		elif button == '%':
			answer = evaluate(Result)/100.0 # we divide the answer by 100 to get percentage
			answer = str(round(float(answer),6)) # rounding answer to 6 decimal places and converting into string
			window.find_element('input').Update(answer) # update the display with answer
			Result = answer
			
		# close the window
		elif button == 'Quit' or button == None:
			break
		else:
			Result += button # add the button text to the math expression ...
			window.find_element('input').Update(Result) # ... and update the result

	window.close() #Closes window. Users can safely call even if window has been destroyed.
	# Should always call when done with a window so that resources are properly freed up within your thread.

if __name__=="__main__": #file is being run directly ()...
	sci_calc() # ...then this func is being executed
	##(used to execute some code only if the file was run directly, and not imported.)