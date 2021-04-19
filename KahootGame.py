import sys
import pygame
from pygame.locals import *
from pygame import *
from playsound import playsound


class Game(object):
    points = ["11,000", "10,000", "9,000", "8,000", "7,000",
              "6,000", "5,000", "4,000", "3,000", "2,000", "1,000"]
    questionList = [
        {
            "question": "A module definition consists of the module. header and the module ________?",
            "options": ["A) Statements" , "B) Body ", "C) Call", "D) Arguments"],
            "answer": 1
        },
        {
            "question": "What term is used in the ending terminal. symbol of a function flowchart?",
            "options": ["A) End", "B) Function Return", "C) Function End", "D) Return"],
            "answer": 3
        },
        {
            "question": "Which of the following errors occur. when a real value is attempted to "
                        "be assigned to an integer variable?",
            "options": ["A)Integer value", "B)Conversion", "C)Type mismatch", "D)None of these"],
            "answer": 2
        },
        {
            "question": "A ________ is a module that returns a value back to. the part of the program that called it?",
            "options": ["A)Loop", "B)For", "C)Function", "D)None of these"],
            "answer": 2
        },
        {
            "question": "192_168_1_5 is an .example of a(n) _____?",
            "options": ["A) TCP", "B) IAC", "C) DNN", "D) IP"],
            "answer": 3
        },
        {
            "question": "All character entities end with _____ to signal the browser. that everything in between is an entity representing a symbol?",
            "options": ["A) ;", "B) &", "C) <<", "D) !"],
            "answer": 0
        },
        {
            "question": "An internal style sheet is. also known as a(n) _____ style sheet?",
            "options": ["A) inline", "B) embedded", "C) insync", "D) Sequential"],
            "answer": 1
        },

        {
            "question": "_____ shrink and grow based. on the size of a viewport?",
            "options": ["A) Stable images", "B) Closed images", "C) Flexible images", "D) Indexed images"],
            "answer": 2
        },
        {
            "question": "Which of the following properties and values should be used. if the navigation links should appear within the main area of a website?",
            "options": ["A) clear: right;", "B) float: left;", "C) padding: right;", "D) margin-left: 1%;"],
            "answer": 1
        },
        {
            "question": "A _____ is the line that defines. the perimeter of a table?",
            "options": ["A) table border", "B) table mark", "C) table ruler", "D) table frame"],
            "answer": 0
        },
        {
            "question": "The _____ CSS3 property can be used. to create multiple columns?",
            "options": ["A) column-count", "B) column-add", "C) column-type", "D) column-multiply"],
            "answer": 0
        },
    ]
