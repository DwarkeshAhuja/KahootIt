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

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    currentQuestion = 0
    selectedAnswer = -1
    red = (200, 20, 20)
    #green = (0, 255, 0)
    green = (114, 180, 58)
    blue = (0, 0, 128)
    orange = (255, 128, 0)
    navyBlue = (156, 101, 226)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Kahoot Lets play and get some Points ')
        self.screen = pygame.display.set_mode((1366, 768), 0, 32)
        self.addBackgroudPic()
        self.font = pygame.font.SysFont('Arial', 25)
        self.bigFont = pygame.font.SysFont('Arial', 50)

    def addBackgroudPic(self):
        bg = pygame.image.load("kahootit.jpeg")
        bg = pygame.transform.scale(bg, (1366, 768))
        self.screen.blit(bg, (0, 0))

    def RoundedRectangle(self, rect, color, radius=0.4):
        rect = Rect(rect)
        color = Color(*color)
        alpha = color.a
        color.a = 0
        pos = rect.topleft
        rect.topleft = 0, 0
        rectangle = Surface(rect.size, SRCALPHA)
        circle = Surface([min(rect.size)*3]*2, SRCALPHA)
        draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle = transform.smoothscale(circle, [int(min(rect.size)*radius)]*2)
        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)
        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)
        return self.screen.blit(rectangle, pos)

