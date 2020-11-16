# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:36:44 2020

@author: heatherjayne

Survey program for Dot Project - BIT
"""
import pandas as pd
import csv
import Tkinter as tk
from Tkinter import *
import ttk
#import pyttsx
#import time
from Tkinter import *
import tkMessageBox
import tkSimpleDialog

import struct
import sys, glob # for listing serial ports

try:
    import serial
except ImportError:
    tkMessageBox.showerror('Import error', 'Please install pyserial.')
    raise

connection = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
#connectuon = None

TEXTWIDTH = 40 # window width, in characters
TEXTHEIGHT = 16 # window height, in lines

VELOCITYCHANGE = 200
ROTATIONCHANGE = 300

helpText = """\
Supported Keys:
P\tPassive
S\tSafe
F\tFull
C\tClean
D\tDock
R\tReset
Space\tBeep
Arrows\tMotion

If nothing happens after you connect, try pressing 'P' and then 'S' to get into safe mode.
"""

from AnimatedGif import AnimatedGif

    

class Survey(tk.Frame):
    # static variables for keyboard callback -- I know, this is icky
    callbackKeyUp = False
    callbackKeyDown = False
    callbackKeyLeft = False
    callbackKeyRight = False
    callbackKeyLastDriveCommand = ''
    
    def __init__(self, file, root, canvas):
        self.file = file
        self.questions = []
        self.readIn()
        self.root = root
        self.canvas = canvas
        self.current_answer = StringVar()
        self.setup()
        #self.strtButton = Button(self.root, text='Start',command = self.hide_and_start) 
        self.fullScreenBtn = Button(self.root, text='Enable Fullscreen Mode', command = self.enable_fullscreen)
        
        self.root.bind("<Key>", self.callbackKey)
        self.root.bind("<KeyRelease>", self.callbackKey)
 
    def readIn(self):
        self.questions = pd.read_csv(self.file)         #reads in the questions file


    def startScreen(self):
        self.resetValues()
        
        #self.strtButton.configure(width = 50,height=5, activebackground = "#33B5E5", relief = RAISED)
        #self.strtButton.place(relx=0.5,rely=0.8,anchor=CENTER)
        self.fullScreenBtn.place(relx=0.01, rely=0.01)
        self.lbl_with_my_gif.place(relx=0.5,rely=0.5,anchor=CENTER)# Packing the label with the animated gif (grid works just as well)
        self.lbl_with_my_gif.configure(bg='black')#change background to match
        self.lbl_with_my_gif.start()  # Shows gif at first frame and we are ready to go
        self.lbl_with_my_gif.bind("<Button-1>", self.leftclick)
        
        
    def ask_questions(self):#asks questions
        self.easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1) 
        self.ques.place(relx=0.5,rely=0.2,anchor=CENTER)           
        self.nextQuestion.place(relx=0.5,rely=0.7,anchor=CENTER)
        self.yes_choice.place(relx=0.43,rely=0.45,anchor=CENTER)
        self.no_choice.place(relx=0.56,rely=0.45,anchor=CENTER)
        self.bar.place(relx=0.5,rely=0.9,anchor=CENTER)
        self.root.mainloop()
        

    def display(self):
        self.answers.append(self.current_answer.get())
        print(self.answers)
        number_of_questions = len(self.questions)
        self.bar['value'] = float(self.count+1)/number_of_questions*100
        self.count = self.count + 1
        
        if self.count == number_of_questions:
            print("count == to number of questions")
                #e.destroy()
                #showMark(score)
        elif self.count == (number_of_questions-1):
            self.nextQuestion.configure(text='finish',command=self.finish)
            
        if self.count <= number_of_questions:
            self.ques.configure(text =self.questions["question"][self.count])
            
    
    def finish(self):#shows thankyou love gif
        self.write_answers_to_file(self.answers)
        #self.bar['value'] = 100
        #self.ques.configure(text = "Thankyou for taking the time to complete this short survey")
        self.hide_question_components()
        self.lbl_finish_gif = AnimatedGif(self.root, 'emotions/loveOptimised.gif', 0.3)  # (tkinter.parent, filename, delay between frames)
        self.lbl_finish_gif.place(relx=0.5,rely=0.5,anchor=CENTER)# Packing the label with the animated gif (grid works just as well)
        self.lbl_finish_gif.configure(bg='black')#change background to match
        self.lbl_finish_gif.start()  # Shows gif at first frame and we are ready to go
        self.lbl_finish_gif.bind("<Button-1>", self.restart)     
        #self.nextQuestion.configure(text = "GoodBye", command=self.startScreen)
        #self.tts()
        #time.wait(15)
        #self.startScreen()
        
        
    def tts(self):
        #trying out tts
        engine = pyttsx.init()
        engine.setProperty('voice', u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
        engine.say("Thankyou so much!")
        engine.runAndWait()
        engine.stop()
        print("talk")
        
    def write_answers_to_file(self, answers):           #writes answers to csv
        with open('answers.csv', 'ab') as write_obj:
            writer = csv.writer(write_obj)
            #was throwing Error: iterable expected, not NoneType
            #added a try catch as it was working even with error, we should keep note however
            #just in case it causes issues down the line
            try:
                writer.writerow(answers)
            except:
                pass
            

    def hide_and_start(self):
        #self.strtButton.lower()
        self.setup()
        self.lbl_with_my_gif.destroy()
        self.ask_questions()
    
    
    def hide_question_components(self):
        self.easy_frame.destroy()
    
    
    def resetValues(self):
        #self.hide_question_components()
        #self.strtButton.lift()
        self.lbl_finish_gif.destroy()
        self.lbl_with_my_gif = AnimatedGif(self.root, 'emotions/happyOptimised.gif', 0.8)  # (tkinter.parent, filename, delay between frames)

        
    def setup(self):
        self.count = 0
        self.answers = []
        self.easy_frame = Frame(self.canvas,bg="white")
        self.bar = ttk.Progressbar(self.easy_frame, length=200, style='black.Horizontal.TProgressbar')
        self.ques = Label(self.easy_frame,text =self.questions["question"][self.count],font="calibri 50",bg="white", wraplength = 800)
        self.nextQuestion = Button(self.easy_frame,command=self.display,text="Next", width = 102,height=2,)
        self.yes_choice = Radiobutton(self.easy_frame,text="yes",font="calibri 30",value="yes",  tristatevalue= 0 ,variable = self.current_answer,bg="white")
        self.no_choice = Radiobutton(self.easy_frame,text="No",font="calibri 30",value="no", tristatevalue = 0, variable = self.current_answer,bg="white")
        self.lbl_finish_gif = AnimatedGif(self.root, 'emotions/loveOptimised.gif', 0.8)  # (tkinter.parent, filename, delay between frames)


    def enable_fullscreen(self):
        self.root.attributes('-fullscreen', True)
        self.fullScreenBtn.configure(text="Disable Fullscreen", command=self.disable_fullscreen)
        #root.bind("<F11>",lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
        #root.bind("<Escape>",lambda event: root.attributes("-fullscreen",False))
        
    def disable_fullscreen(self):
        self.root.attributes('-fullscreen', False)
        self.fullScreenBtn.configure(text="Enable Fullscreen", command=self.enable_fullscreen)

    def leftclick(self,event):
        print("left")
        self.hide_and_start()

    def restart(self,event):
        print("left")
        self.startScreen()

    # sendCommandASCII takes a string of whitespace-separated, ASCII-encoded base 10 values to send
    def sendCommandASCII(self, command):
        cmd = ""
        for v in command.split():
            cmd += chr(int(v))

        self.sendCommandRaw(cmd)

    # sendCommandRaw takes a string interpreted as a byte array
    def sendCommandRaw(self, command):
        global connection

        try:
            if connection is not None:
                connection.write(command)
        except serial.SerialException:
            print "Lost connection"
            tkMessageBox.showinfo('Uh-oh', "Lost connection to the robot!")
            connection = None

        print ' '.join([ str(ord(c)) for c in command ])
        self.text.insert(END, ' '.join([ str(ord(c)) for c in command ]))
        self.text.insert(END, '\n')
        self.text.see(END)

    # getDecodedBytes returns a n-byte value decoded using a format string.
    # Whether it blocks is based on how the connection was set up.
    def getDecodedBytes(self, n, fmt):
        global connection
        
        try:
            return struct.unpack(fmt, connection.read(n))[0]
        except serial.SerialException:
            print "Lost connection"
            tkMessageBox.showinfo('Uh-oh', "Lost connection to the robot!")
            connection = None
            return None
        except struct.error:
            print "Got unexpected data from serial port."
            return None

    # get8Unsigned returns an 8-bit unsigned value.
    def get8Unsigned(self):
        return getDecodedBytes(1, "B")

    # get8Signed returns an 8-bit signed value.
    def get8Signed(self):
        return getDecodedBytes(1, "b")

    # get16Unsigned returns a 16-bit unsigned value.
    def get16Unsigned(self):
        return getDecodedBytes(2, ">H")

    # get16Signed returns a 16-bit signed value.
    def get16Signed(self):
        return getDecodedBytes(2, ">h")

    # A handler for keyboard events. Feel free to add more!
    def callbackKey(self, event):
        k = event.keysym.upper()
        motionChange = False

        if event.type == '2': # KeyPress; need to figure out how to get constant
            if k == 'P':   # Passive
                self.sendCommandASCII('128')
            elif k == 'S': # Safe
                self.sendCommandASCII('131')
            elif k == 'F': # Full
                self.sendCommandASCII('132')
            elif k == 'C': # Clean
                self.sendCommandASCII('135')
            elif k == 'D': # Dock
                self.sendCommandASCII('143')
            elif k == 'SPACE': # Beep
                self.sendCommandASCII('141 3')
            elif k == 'O': # BOOB
                self.sendCommandASCII('164 66 79 79 66')
            elif k == 'R': # Reset
                self.sendCommandASCII('7')
            elif k == 'UP':
                self.callbackKeyUp = True
                motionChange = True
            elif k == 'DOWN':
                self.callbackKeyDown = True
                motionChange = True
            elif k == 'LEFT':
                self.callbackKeyLeft = True
                motionChange = True
            elif k == 'RIGHT':
                self.callbackKeyRight = True
                motionChange = True
            else:
                print repr(k), "not handled"
        elif event.type == '3': # KeyRelease; need to figure out how to get constant
            if k == 'UP':
                self.callbackKeyUp = False
                motionChange = True
            elif k == 'DOWN':
                self.callbackKeyDown = False
                motionChange = True
            elif k == 'LEFT':
                self.callbackKeyLeft = False
                motionChange = True
            elif k == 'RIGHT':
                self.callbackKeyRight = False
                motionChange = True
            
        if motionChange == True:
            velocity = 0
            velocity += VELOCITYCHANGE if self.callbackKeyUp is True else 0
            velocity -= VELOCITYCHANGE if self.callbackKeyDown is True else 0
            rotation = 0
            rotation += ROTATIONCHANGE if self.callbackKeyLeft is True else 0
            rotation -= ROTATIONCHANGE if self.callbackKeyRight is True else 0

            # compute left and right wheel velocities
            vr = velocity + (rotation/2)
            vl = velocity - (rotation/2)

            # create drive command
            cmd = struct.pack(">Bhh", 145, vr, vl)
            if cmd != self.callbackKeyLastDriveCommand:
                self.sendCommandRaw(cmd)
                self.callbackKeyLastDriveCommand = cmd


def main():
    root = tk.Tk()
    
    #main.ask_questions()
    #survey.write_answers_to_file(answers)
    #main.pack(side="top", fill="both", expand=True)
    canvas = Canvas(root,width = 1024,height = 614, bg = 'black')
    main = Survey('testQuestions.csv', root, canvas)
    canvas.grid(column = 0 , row = 1)
    #img = PhotoImage(file="smiley.gif")
    #canvas.create_image(50,10,image=img,anchor=NW)
    main.startScreen()
    root.mainloop()
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
