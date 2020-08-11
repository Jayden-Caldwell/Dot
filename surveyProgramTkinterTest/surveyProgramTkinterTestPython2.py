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



from AnimatedGif import AnimatedGif

    

class Survey(tk.Frame):
    def __init__(self, file, root, canvas):
        self.file = file
        self.questions = []
        self.readIn()
        self.root = root
        self.canvas = canvas
        self.current_answer = StringVar()
        self.setup()
        self.strtButton = Button(self.root, text='Start',command = self.hide_and_start) 
        self.fullScreenBtn = Button(self.root, text='Enable Fullscreen Mode', command = self.enable_fullscreen)


 
    def readIn(self):
        self.questions = pd.read_csv(self.file)         #reads in the questions file


    def startScreen(self):
        self.resetValues()
        
        self.strtButton.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
        self.strtButton.place(relx=0.5,rely=0.9,anchor=CENTER)
        self.fullScreenBtn.place(relx=0.01, rely=0.01)
        self.lbl_with_my_gif.place(relx=0.5,rely=0.4,anchor=CENTER)# Packing the label with the animated gif (grid works just as well)
        self.lbl_with_my_gif.configure(bg='black')#change background to match
        self.lbl_with_my_gif.start()  # Shows gif at first frame and we are ready to go
        
        
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
            
    
    def finish(self):
        self.write_answers_to_file(self.answers)
        self.bar['value'] = 100
        self.ques.configure(text = "Thankyou for taking the time to complete this short survey")
        self.nextQuestion.configure(text = "GoodBye", command=self.startScreen)           
            
    
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
        self.strtButton.lower()
        self.setup()
        self.lbl_with_my_gif.destroy()
        self.ask_questions()
    
    
    def hide_question_components(self):
        self.easy_frame.destroy()
    
    
    def resetValues(self):
        self.hide_question_components()
        self.strtButton.lift()
        self.lbl_with_my_gif = AnimatedGif(self.root, 'emotions/kawaii.gif', 0.03)  # (tkinter.parent, filename, delay between frames)

        
    def setup(self):
        self.count = 0
        self.answers = []
        self.easy_frame = Frame(self.canvas,bg="white")
        self.bar = ttk.Progressbar(self.easy_frame, length=200, style='black.Horizontal.TProgressbar')
        self.ques = Label(self.easy_frame,text =self.questions["question"][self.count],font="calibri 50",bg="white", wraplength = 800)
        self.nextQuestion = Button(self.easy_frame,command=self.display,text="Next", width = 102,height=2,)
        self.yes_choice = Radiobutton(self.easy_frame,text="yes",font="calibri 30",value="yes",  tristatevalue= 0 ,variable = self.current_answer,bg="white")
        self.no_choice = Radiobutton(self.easy_frame,text="No",font="calibri 30",value="no", tristatevalue = 0, variable = self.current_answer,bg="white")

    def enable_fullscreen(self):
        self.root.attributes('-fullscreen', True)
        self.fullScreenBtn.configure(text="Disable Fullscreen", command=self.disable_fullscreen)
        #root.bind("<F11>",lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
        #root.bind("<Escape>",lambda event: root.attributes("-fullscreen",False))
        
    def disable_fullscreen(self):
        self.root.attributes('-fullscreen', False)
        self.fullScreenBtn.configure(text="Enable Fullscreen", command=self.enable_fullscreen)


def main():
    root = tk.Tk()
    
    #main.ask_questions()
    #survey.write_answers_to_file(answers)
    #main.pack(side="top", fill="both", expand=True)
    canvas = Canvas(root,width = 1064,height = 600, bg = 'black')
    main = Survey('testQuestions.csv', root, canvas)
    canvas.grid(column = 0 , row = 1)
    #img = PhotoImage(file="smiley.gif")
    #canvas.create_image(50,10,image=img,anchor=NW)
    main.startScreen()
    root.mainloop()
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
