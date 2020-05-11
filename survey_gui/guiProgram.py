# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:39:49 2020

@author: joelg

GUI program for Dot Project - BIT
"""


from guizero import App, Text, PushButton, CheckBox
import pandas as pd
import csv

# Survey code
class Survey:
    def __init__(self, file):
        self.file = file
        self.questions = []
        self.readIn()
        
    def readIn(self):
        self.questions = pd.read_csv(self.file)         #reads in the questions file

    def ask_questions(self):                            #asks questions
        answers = []      # Stores the answers to the questions 
        for index, row in self.questions.iterrows():
             Text(app, text=(f"{row['question']}"))
             
             PushButton(app, command=lambda : answers.append('Yes'), text="Yes")
             
             PushButton(app, command=lambda : answers.append('No'), text="No")
             
             nextQuestion = PushButton(app, command=lambda : self.write_answers_to_file(answers), text="Save answers")

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
       
# GUI code
app = App(title="Dot interface", layout="auto")

survey = Survey('testQuestions.csv')
answers = survey.ask_questions()

app.display()