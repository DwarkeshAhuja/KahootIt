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

    def addPointsTile(self):
        yCordinate = 50
        yCordinateText = 75
        for index in range(11):
            if 10-index == self.currentQuestion:
                self.RoundedRectangle(
                    (50, yCordinate, 200, 50), self.red, 0.5)
            else:
                self.RoundedRectangle(
                    (50, yCordinate, 200, 50), self.navyBlue, 0.5)
            self.displayText(self.points[index],
                             self.WHITE, 150, yCordinateText)
            yCordinate += 60
            yCordinateText += 60

    def addQuestionBox(self):
        self.RoundedRectangle(
            (320, 450, 950, 100), self.navyBlue, 0.5)
        a = " "
        b = " "
        a,b = self.questionList[self.currentQuestion]["question"].split('.')
        self.displayText(a, self.BLACK, 825, 480)
        self.displayText(b, self.BLACK, 825, 520)

    def addOptionBox(self, isCorrect=False):
        yCordinate = 560
        yCordinateText = 580
        xCordinate = 320
        xCordinateText = 450
        options = self.questionList[self.currentQuestion]["options"]
        for index in range(len(options)):
            if self.selectedAnswer == index:
                if isCorrect:
                    self.RoundedRectangle(
                        (xCordinate, yCordinate, 300, 50), self.green, 0.5)
                else:
                    self.RoundedRectangle(
                        (xCordinate, yCordinate, 300, 50), self.red, 0.5)
            else:
                self.RoundedRectangle(
                    (xCordinate, yCordinate, 300, 50), self.navyBlue, 0.5)
            self.displayText(
                options[index], self.BLACK, xCordinateText, yCordinateText)
            if(index % 2 == 0):
                xCordinate = 950
                xCordinateText = 1070
            else:
                xCordinate = 320
                yCordinate = 620
                xCordinateText = 450
                yCordinateText = 640

    def validateAnswer(self, correctAnswer, keyPressed):
        print("correctAnswer==>{0}".format(correctAnswer))
        isValid = False
        if keyPressed == pygame.K_a:
            self.selectedAnswer = 0
            if correctAnswer == 0:
                isValid = True
            else:
                isValid = False
        if keyPressed == pygame.K_b:
            self.selectedAnswer = 1
            if correctAnswer == 1:
                isValid = True
            else:
                isValid = False
        if keyPressed == pygame.K_c:
            self.selectedAnswer = 2
            if correctAnswer == 2:
                isValid = True
            else:
                isValid = False
        if keyPressed == pygame.K_d:
            self.selectedAnswer = 3
            if correctAnswer == 3:
                isValid = True
            else:
                isValid = False
        return isValid

    def gameRules(self):
        self.addBackgroudPic()
        readRules = True
        isPlay=True
        while readRules:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        readRules = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.displayText("Press A/B/C/D to select corresponding options",
                             self.WHITE,
                             680, 100, True)
            self.displayText("Press P to play or Q to quit.",
                             self.WHITE,
                             680, 150, True)

            pygame.display.update()

    def displayText(self, text, color, xCordinate, yCordinate=0, isBig=False):
        if isBig:
            textSurface = self.bigFont.render(text, True, color)
        else:
            textSurface = self.font.render(text, True, color)
        textRectangle = textSurface.get_rect()
        textRectangle.center = (xCordinate, yCordinate)
        self.screen.blit(textSurface, textRectangle)

    def resultScreen(self, isLost=False):
        isPlay = True
        self.addBackgroudPic()
        readRules = True
        while readRules:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        readRules = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            points = 0
            if self.currentQuestion > 0:
                points = self.points[10-(self.currentQuestion-1)]
            if isLost:
                self.displayText("Oops You have lost the game!!! ",
                                 self.red,
                                 630, 50, True
                                 )
                self.displayText("Better luck next time",
                                 self.green,
                                 680, 100, True)
            else:
                self.displayText("Well Played!!!",
                                 self.red,
                                 630, 50, True
                                 )
                self.displayText("You have won:-"+str(points) + " Points",
                                 self.green,
                                 680, 100, True)
            self.displayText("Press P to play again or Q to end the game.",
                             self.WHITE,
                             660, 650, True)
            pygame.display.update()
            if isPlay:
                #playsound("kahoot_lobby_music.mp3")
                playsound("kahoot_answer.mp3")
                isPlay = False
        self.currentQuestion = 0
        self.selectedAnswer = -1
        self.playGame()
