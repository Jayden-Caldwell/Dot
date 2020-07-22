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
        self.readIn()
        self.root = root
        self.canvas = canvas
        
    def readIn(self):
        self.questions = pd.read_csv(self.file)         #reads in the questions file

    def ask_questions(self):#asks questions
        
    
    
        easy_frame = Frame(self.canvas,bg="white")
        easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)            
        answers = []
        
        nextQuestion = Button(easy_frame,command=display,text="Next")
        nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
        
        self.root.mainloop()
        
        
        
        for index, row in self.questions.iterrows():    #goes through asking each question
            
            '''text.insert(tk.INSERT, row['question'] + ":")  
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
        self.write_answers_to_file(answers) '''            #send answers list to be written to answers csv

    def display(self):
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            print(li) 
    
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
    
    
    
    
    
    
    
    
    