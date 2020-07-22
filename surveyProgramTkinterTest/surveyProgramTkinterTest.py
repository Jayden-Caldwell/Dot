# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:36:44 2020

@author: heatherjayne

Survey program for Dot Project - BIT
"""
import pandas as pd
import csv
import tkinter as tk
from tkinter import *

    

class Survey(tk.Frame):
    def __init__(self, file, root, canvas):
        self.file = file
        self.questions = []
        self.answers = []
        self.readIn()
        self.root = root
        self.canvas = canvas
        self.count = 0
        self.current_answer = StringVar()
        self.easy_frame = Frame(self.canvas,bg="white")
        self.ques = Label(self.easy_frame,text =self.questions["question"][self.count],font="calibri 12",bg="white")
        self.nextQuestion = Button(self.easy_frame,command=self.display,text="Next")
        self.yes_choice = Radiobutton(self.easy_frame,text="yes",font="calibri 10",value="yes",variable = self.current_answer,bg="white")
        self.no_choice = Radiobutton(self.easy_frame,text="No",font="calibri 10",value="no",variable = self.current_answer,bg="white")
        
        
    def readIn(self):
        self.questions = pd.read_csv(self.file)         #reads in the questions file


    def ask_questions(self):#asks questions
        
        self.easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1) 
        
        self.ques.place(relx=0.5,rely=0.2,anchor=CENTER)           
        
        self.nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
        self.yes_choice.place(relx=0.5,rely=0.42,anchor=CENTER)
        self.no_choice.place(relx=0.5,rely=0.52,anchor=CENTER)
        
        self.root.mainloop()
        
        
        
    """for index, row in self.questions.iterrows():    goes through asking each question
            
           text.insert(tk.INSERT, row['question'] + ":")  
            text.pack()     
            ans = input('Type Y(yes) or N(n): ')    #asks for input
            if ans[0].upper() == 'Y':               #checks first letter of input and capitilizes
                answers.append('Yes')               #appends to answers list
                break                               #breaks out of while loop to answer next question(temp)
            elif ans[0].upper() =='N':
                answers.append('No')  
                break
            else:
                print('Please type either \'Y\' or \'N\'') #asks user to type y or n(temp)
        self.write_answers_to_file(answers) """           #send answers list to be written to answers csv

    def display(self):
        
        self.answers.append(self.current_answer.get())
        print(self.answers)
        number_of_questions = len(self.questions)
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
        
                   
            
    
    def write_answers_to_file(self, answers):           #writes answers to csv
        with open('answers.csv', 'a+', newline='') as write_obj:
            writer = csv.writer(write_obj)
            #was throwing Error: iterable expected, not NoneType
            #added a try catch as it was working even with error, we should keep note however
            #just in case it causes issues down the line
            try:
                writer.writerow(answers)
            except:
                pass
            

def hide_and_start():
    strtButton.lower()
    main.ask_questions()

def hide_me(event):
    event.widget.pack_forget()
       

def main():
    root = tk.Tk()
    
    #main.ask_questions()
    #survey.write_answers_to_file(answers)
    #main.pack(side="top", fill="both", expand=True)
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    global main
    main = Survey('testQuestions.csv', root, canvas)
    canvas.grid(column = 0 , row = 1)
    global strtButton
    strtButton = Button(root, text='Start',command = hide_and_start) 
    strtButton.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    strtButton.grid(column = 0 , row = 1)
    root.mainloop()
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    