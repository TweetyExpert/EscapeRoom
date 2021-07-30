# -391- Final Project

import tkinter as tk   #importing packages
from tkinter import *

import time
import math

keycheck=False
buttoncheck=False
lockcheck=False   #setting all the global varibles that will be used
keypadcheck=False
sbuttonscheck=False
buttonpresses=[]

class EscapeRoom(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame is the Starting page which is where you wake up
        tk.Label(self, text="I wake up stuck in a room. I see a door, but how do I open it?\n I also see a TV to my right and an old desk to my left. \n \n Let me look around.", font=(18), width=100,height=20).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look at the Desk",command=lambda: master.switch_frame(DeskPage)).pack()
        tk.Button(self, text="Look at the Door",command=lambda: master.switch_frame(DoorPage)).pack()
        tk.Button(self, text="Look at the TV",command=lambda: master.switch_frame(TVPage)).pack()
        
class DeskPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame that holds the desk top, and the two drawers
        tk.Label(self, text="There is a desk with a book on top and two drawers. What should I do?", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look at the Top of the Desk",command=lambda: master.switch_frame(TDeskPage)).pack()
        tk.Button(self, text="Look through the Left Drawer",command=lambda: master.switch_frame(LDrawerPage)).pack()
        tk.Button(self, text="Look through the Right Drawer",command=lambda: master.switch_frame(RDrawerPage)).pack()
        tk.Label(self, text="",width=100,height=1).pack()
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(StartPage)).pack()

class DoorPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame that is the escape door with all the puzzles
        tk.Label(self, text="",width=100,height=1).pack()
        tk.Button(self, text="Try to open the Door",command=lambda: master.switch_frame(TrydoorPage)).pack()
        tk.Label(self, text="",width=100,height=1).pack()
        tk.Label(self, text="This door looks like it is the exit, \n but there are four locks I need to unlock first to be able to open it.", font=(18),width=100,height=17).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look at the Button",command=lambda: master.switch_frame(ButtonPage)).pack()
        tk.Button(self, text="Look at the Lock",command=lambda: master.switch_frame(LockPage)).pack()
        tk.Button(self, text="Look at the Keypad",command=lambda: master.switch_frame(KeypadPage)).pack()
        tk.Button(self, text="Look at the Shaped Buttons",command=lambda: master.switch_frame(SButtonsPage)).pack()
        tk.Label(self, text="",width=100,height=1).pack()
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(StartPage)).pack()

class TrydoorPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame if they try the door and checks if they solved the puzzles
        if buttoncheck==True and lockcheck==True and keypadcheck==True and sbuttonscheck==True:
            tk.Label(self, text="You have escaped! Congratulations!", font=(100),width=100,height=20).pack(side="top", fill="x", pady=5)
        
        else:
            tk.Label(self, text="It is still locked. There is more to do.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()

class TVPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame with TV screen
        tk.Label(self, text="On the screen there is a Blue Square, Red Triangle, Violet Star, and Orange Circle.\n What does this mean?", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(StartPage)).pack()
        
class TDeskPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame with the top of the desk with the children's book
        tk.Label(self, text="On the desk there is a children’s book turned to the page with the text, \n“Casey visited the zoo. He first saw two owls that flew around. Then went to see the four penguins. \n One lion then roared and it was heard across the park! The last stop was seeing eight little otters swim in circles.”\n \n Maybe this means something?", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(DeskPage)).pack()     
        
class LDrawerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame with nothing in the drawer
        tk.Label(self, text="Nothing useful in here. I must keep looking.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(DeskPage)).pack() 
             
class RDrawerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global keycheck
        #Frame giving the key to the user or saying they found it already
        if keycheck==False:
            tk.Label(self, text="I found a key! I'll put it in my pocket.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            keycheck=True
        else:
            tk.Label(self, text="I already took the key, but there is nothing else.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(DeskPage)).pack()           
        
class ButtonPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame that holds the button press
        if buttoncheck==True:
            tk.Label(self, text="I already solved this.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
        
        else:
            tk.Label(self, text="On the wall there is a red button with the number 3 printed on it.\n Above, it reads “Count your seconds. You must be present when the time is right.”", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Press Button",command=lambda: master.switch_frame(PressButtonPage)).pack()
            tk.Label(self, text="",width=100,height=1).pack()
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
        
class PressButtonPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        currenttime=time.time()
        currenttime=math.trunc(currenttime)
        currenttime=str(currenttime)
        #Frame that checks if they pressed the button at the correct time
        for x in currenttime:
            pass
        if x == '3':
            tk.Label(self, text="I heard a click! Looks like I solved it!", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            global buttoncheck
            buttoncheck=True
            
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()             
        else:
            tk.Label(self, text="Nothing happened, I need to try again.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(ButtonPage)).pack()
        
class LockPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global keycheck
        global lockcheck
        #Frame that holds the lock and checks if the user has the key already to open it
        if lockcheck==True:
            tk.Label(self, text="I already solved this.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
        
        else:
            tk.Label(self, text="There is a lock here. No way to open it without a key.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            if keycheck==True:
                tk.Button(self, text="Try key",command=lambda: master.switch_frame(TrykeyPage)).pack()
            tk.Label(self, text="",width=100,height=1).pack()
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()

class TrykeyPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Frame that uses the key and sets that the lock is solved
        tk.Label(self, text="The key worked! One more lock down.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
        global lockcheck
        lockcheck=True
        tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
      
class KeypadPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global keypadcheck
        #Frame that Looks for the user to enter the correct numbers
        if keypadcheck==True:
            tk.Label(self, text="I already solved this.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
        
        else:
            tk.Label(self, text="", width=100,height=10).pack()
            tk.Label(self, text="Located here is a keypad with 4 empty spaces.\n Looks like I can enter some numbers.\n",width=100,font=(18)).pack(fill="x")
            global result
            
            result = tk.Text(self,height = 1,width = 4)
            result.pack(side='top')
            tk.Label(self, text="",width=100,height=10).pack()
            tk.Button(self, text="Try code",command=lambda: master.switch_frame(TrykeypadPage)).pack()
            tk.Label(self, text="",width=100,height=1).pack()
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
        
class TrykeypadPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global keypadcheck
        newresult='0'
        newresult=result.get('1.0','end-1c')
        #Frame to see what the user entered and if it is correct
        if newresult == '2418' :
            tk.Label(self, text="I heard a click and the keypad is now blank.\n It was the right code!", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            keypadcheck=True
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
        
        else:
            tk.Label(self, text="The code didn't seem to work. Let me try again.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(KeypadPage)).pack()
  
class SButtonsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global buttonpresses
        global sbuttonscheck
        buttonpresses=[]
        #Frame to give the user the ability to press the buttons and test
        if sbuttonscheck==True:
            tk.Label(self, text="I already solved this.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack()
            
        else:    
            tk.Label(self, text="I see 4 different buttons in the shape of square,triangle, star, and circle.\n Also, there is a rainbow painted above the buttons. What could this mean?", font=(18), width=100,height=20).pack(side="top", fill="x", pady=5)
            
            tk.Button(self, text="Square",borderwidth=3, relief='solid',command=lambda m='SQ' : Sbuttonpress(m,buttonpresses)).pack(side=LEFT,fill='x',padx=33)        
            tk.Button(self, text="Triangle",borderwidth=3, relief='solid',command=lambda m='T' : Sbuttonpress(m,buttonpresses)).pack(side=LEFT,fill='x',padx=33)        
            tk.Button(self, text="Star",borderwidth=3, relief='solid',command=lambda m='ST' : Sbuttonpress(m,buttonpresses)).pack(side=LEFT,fill='x',padx=33)        
            tk.Button(self, text="Circle",borderwidth=3, relief='solid',command=lambda m='C' : Sbuttonpress(m,buttonpresses)).pack(side=LEFT,fill='x',padx=33)        
            tk.Label(self, text="\n",height=1).pack()
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack(side=BOTTOM,pady=10)       
            tk.Label(self, text="\n \n",height=1).pack()
            tk.Button(self, text="Test button presses",command=lambda: master.switch_frame(checkSbuttonpress)).pack(side=BOTTOM,pady=10)

def Sbuttonpress(m,buttonpresses):
    global allbuttonpresses
    buttonpresses.append(m)
    allbuttonpresses=buttonpresses
        #Saves all the button presses in a list to be able to check for later

class checkSbuttonpress(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global allbuttonpresses
        global sbuttonscheck
        #Frame that checks if their button presses were right
        if allbuttonpresses == ['T', 'C', 'SQ', 'ST']:
            tk.Label(self, text="All of the buttons pushed into the wall. I got it right!", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            sbuttonscheck=True
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(DoorPage)).pack() 
        
        else:
            tk.Label(self, text="Nothing happened. Maybe I need to press them in a different order.", font=(18),width=100,height=20).pack(side="top", fill="x", pady=5)
            tk.Button(self, text="Go back",command=lambda: master.switch_frame(SButtonsPage)).pack()
            
#main
if __name__ == "__main__":
    app = EscapeRoom()
    app.mainloop()