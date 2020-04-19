# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:36:44 2020

@author: heatherjayne

Survey program for Dot Project - BIT
"""
import pandas as pd
import csv

class Survey:
    def __init__(self, file):
        self.file = file
        self.questions = []
        self.readIn()
        
    def readIn(self):
        self.questions = pd.read_csv(self.file)         #reads in the questions file

    def ask_questions(self):                            #asks questions
        answers = []
        for index, row in self.questions.iterrows():    #goes through asking each question
            while True:                                 #loops through asking same question until user says Y or N(temperary while console based)
                print(row['question'] + ":")            #prints question
                ans = input('Type Y(yes) or N(n): ')    #asks for input
                if ans[0].upper() == 'Y':               #checks first letter of input and capitilizes
                    answers.append('Yes')               #appends to answers list
                    break                               #breaks out of while loop to answer next question(temp)
                elif ans[0].upper() =='N':
                    answers.append('No')
                    break
                else:
                    print('Please type either \'Y\' or \'N\'') #asks user to type y or n(temp)
        self.write_answers_to_file(answers)             #send answers list to be written to answers csv

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
       

def main():
    survey = Survey('testQuestions.csv')
    answers = survey.ask_questions()
    survey.write_answers_to_file(answers)
    
    
if __name__ == '__main__':
    main()