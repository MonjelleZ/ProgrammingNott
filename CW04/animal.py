#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:05:27 2021

@author: txa
"""

def ask(text) :
    while True :
        ans = input(text+" ")
        if ans=="yes" :
            return True
        elif ans=="no" :
            return False
        else :
            print("Please answer yes or no!")


class Knowledge :
    pass

class Question (Knowledge):
    
    def __init__(self,text,ifyes,ifno) :
        self.text = text
        self.ifyes = ifyes
        self.ifno = ifno
        
    def play(self) :
        if ask(self.text):
            self.ifyes = self.ifyes.play()
        else :
            self.ifno = self.ifno.play()
        return self
        
class Answer(Knowledge) :
    
    def __init__(self,text) :
        self.text = text
  
    def play(self) :
        if ask(f"Is it a {self.text}?") :
            print("I knew it!")
            return self
        else :
            newanimal = input("What animal were you thinking of?")
            newquestion = input("Tell me a question to differentiate your animal?")
            if input(f"What would the answer be for {newanimal}"):
                return Question(newquestion,Answer(newanimal),
                                self)
            else :
                return Question(newquestion,self ,
                                Answer(text))
            
  
import pickle


try :
    file = open("animal.kb","rb") # read binary
    kb = pickle.load(file)
    file.close()
except FileNotFoundError:
    #kb = Question("Has it got 4 legs?",
     #     Question("Does it bark?",
     #              Answer("Dog"),
     #              Answer("Cat")),
     #     Answer("Chicken"))
    kb = Question("Does it bark?",
                   Answer("Dog"),
                   Answer("Cat"))
while(True) :
    if not ask("Do you want to play? "):
        break
    kb = kb.play()
file = open("animal.kb","wb") # write binary
pickle.dump(kb,file)
file.close()
        
        
        
        
        
        
        
        
        
        
        
        
    