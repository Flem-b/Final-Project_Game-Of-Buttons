import sys
from PySide.QtGui import *
from random import randint

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label3 = QLabel ("Hi", self)
        qf = QFont ("Arial",2,QFont.Bold )
        self.label3.setFont(qf)
        self.label3.move(40,550)
        self.label4 = QLabel ("hello", self)
        self.label4.setFont(qf)
        self.label4.move(500,70)
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))
        self.but1 = QPushButton("Innitiate Program", self)
        self.but1.setGeometry(self.width()/2-150,self.height()/2-100,300,100)
        self.but1.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))
        self.label4.setPixmap(QPixmap('push-button-icon-png-2.png'))
        self.label4.move(180,100)

    def handleButton(self):
            self.w = MyWindowa()
            self.w.show()
            self.hide()


class MyWindowa(QWidget):
    def __init__(self):
        super(MyWindowa, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("Games of Buttons", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.Bold)
        self.label.setFont(qf)
        self.label.move(350,50)
        self.label2 = QLabel ("Welcome to the Games of Buttons,\na game created to show you the dimensions of your trust\nin software. \nPlease enter all the information that is requested. \n \nEnjoy.", self)
        qf = QFont ("Bradley Hand ITC",18,QFont.Bold )
        self.label2.setFont(qf)
        self.label2.move(100,150)
        self.but1 = QPushButton("Continue", self)
        self.but1.setToolTip('Let the Game begin')
        self.but1.setGeometry(self.width()/2-130,self.height()/1.5,300,100)
        self.but1.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def handleButton(self):
        self.w = MyWindowc()
        self.w.show()
        self.hide()


class MyWindowc(QWidget):
    def __init__(self):
        super(MyWindowc, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel ("soldier",self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(120,120)
        self.label.setPixmap(QPixmap('frau.png'))
        self.label.move(500,00)
        self.label2 = QLabel("Private C. had always been reckless\nwith her information\noutput online.\nShe never cared about\nprivacy or anonymity on the Internet.\nOne day her transperency\nbecame her doom. She got caught\nby the evil Dr. Browser.\nAll her information was captured\nand she has been stuck\nin Dr. Browser's prison,\nthe Cloud, ever since.\n\nExperience yourself how she got caught.", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label2.setFont(qf)
        self.label2.move(30,10)
        self.but1 = QPushButton ("Let the Flashback begin", self)
        self.but1.setToolTip("Experience Private C's horror story")
        self.but1.setGeometry(30,495,250,70)
        self.but1.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))


    def handleButton(self):
        self.w = MyWindow2()
        self.w.show()
        self.hide()

class MyWindow2(QWidget):
    def __init__(self):
        super(MyWindow2, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("This program uses cookies to enable\na better playing experience.\n\n\nFind out more about cookies\nby googling 'Cookies'.", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label.setFont(qf)
        self.label.move(250,100)
        self.but = QPushButton("I accept cookies", self)
        self.but.setToolTip('Yes, you do')
        self.but.setGeometry(self.width()/2-120,self.height()/2+70,100,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("I refuse cookies", self)
        self.but1.setToolTip("No, you don't")
        self.but1.setGeometry(self.width()/2,self.height()/2+70,100,50)
        self.but1.clicked.connect(self.otherButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        sender = self.sender()
        sender.move(20,20)


    def handleButton(self):
        self.w = MyWindowf()
        self.w.show()
        self.hide()


class MyWindowu(QWidget):
    def __init__(self):
        super(MyWindowu, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("Initiating Program", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label.setFont(qf)
        self.label.move(100,50)
        self.label2 = QLabel ("Please enter your information to have access\nto the following Program.\nClick on the button to open up the input field.\nEvery field has to be filled out\notherwise the program won't run properly.", self)
        qf = QFont ("Arial",20,QFont.Bold )
        self.label2.setFont(qf)
        self.label2.move(100,150)
        self.but1 = QPushButton("Continue", self)
        self.but1.setToolTip('Carry on')
        self.but1.setGeometry(self.width()/2-130,self.height()/1.25,300,70)
        self.but1.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

        self.w = QComboBox(self)
        self.w.move(770,400)
        self.w.addItem("Male")
        self.w.addItem("Female")
        self.w.addItem("Transgender")
        self.w.currentIndexChanged.connect(self.clicked)

        self.a = QComboBox(self)
        self.a.move(640,400)
        self.a.addItem("10-20 years old")
        self.a.addItem("20-30 years old")
        self.a.addItem("30-40 years old")
        self.a.addItem("40-50 years old")
        self.a.addItem("50 years old +")
        self.a.currentIndexChanged.connect(self.clicked2)

        self.p = QComboBox(self)
        self.p.move(490,400)
        self.p.addItem("Blonde Hair")
        self.p.addItem("Brown Hair")
        self.p.addItem("Ginger Hair")
        self.p.addItem("Black Hair")
        self.p.addItem("Bold")
        self.p.addItem("Undefinable/Other")
        self.a.currentIndexChanged.connect(self.clicked7)

        self.l = QComboBox(self)
        self.l.move(390,400)
        self.l.addItem("Donkey")
        self.l.addItem("Elephant")
        self.a.currentIndexChanged.connect(self.clicked8)

        self.o = QPushButton("Location", self)
        self.o.move(290,400)
        self.o.clicked.connect(self.clicked5)

        self.o = QPushButton("Full Name", self)
        self.o.move(190,400)
        self.o.clicked.connect(self.clicked3)

        self.o = QPushButton("Height", self)
        self.o.move(90,400)
        self.o.clicked.connect(self.clicked6)

    def handleButton(self):
        self.w = MyWindow3()
        self.w.show()
        self.hide()


    def clicked(self, i):
        print(self.w.currentText())

    def clicked8(self, i):
        print(self.w.currentText())

    def clicked7(self, i):
        print(self.w.currentText())

    def clicked2(self, i):
        print(self.a.currentText())

    def clicked3(self):
        text, ok = QInputDialog.getText(self, 'Name', 'What is your name?')

        if ok:
            print(text)


    def clicked6(self):
        text, ok = QInputDialog.getText(self, 'Height', 'How tall are you (in cm.)?')

        if ok:
            print(text)


    def clicked5(self):
        text, ok = QInputDialog.getText(self, 'Location', 'What is your current location?')

        if ok:
            print(text)


class MyWindowf(QWidget):
    def __init__(self):
        super(MyWindowf, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label2 = QLabel("Terms of Agreement\n\nPLEASE READ THIS SOFTWARE LICENSE AGREEMENT\nCAREFULLY BEFORE USING THIS SOFTWARE.\nBY USING THIS SOFTWARE\nYOU ARE AGREEING TO BE BOUND\nBY THE TERMS OF THIS LICENSE.\nIF YOU DO NOT AGREE TO THE TERMS\nOF THIS LICENSE YOU CANNOT USE THIS SOFTWARE.\n", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label = QLabel("By clicking Innitate Program you accept our Terms of Agreement.All data is stored on our servers and will be used for commercial purposes. You'll most likely get Spam, E-Mails,\nPop-up Windows - which you fear to click. You just did exactly what Dr.Browser wanted you to do.\nYou have just become a slave to Dr.Browser.\nYou are now imprisoned in the Cloud. Alongside millions of other people due to your lack of caution online. By clicking Innitate Program you accept our Terms of Agreement.\nAll data is stored on our servers and will be used for commercial purposes. You'll most likely get Spam, E-Mails, Pop-up Windows - which you fear to click. You just did exactly what Dr.Browser wanted you to do.You have just become a slave to Dr.Browser.\nYou are now imprisoned in the Cloud.\nAlongside millions of other people due to your lack of caution online. By clicking Innitate Program you accept our Terms of Agreement.All data is stored on our servers and will be used for commercial purposes. You'll most likely get Spam, E-Mails, Pop-up Windows - which\nyou fear to click.\nYou just did exactly what Dr.Browser wanted you to do.\nYou have just become a slave to Dr.Browser.\nYou are now imprisoned in the Cloud. Alongside millions of other people due to your lack of caution online.By clicking Innitate Program you accept our Terms of Agreement.\nAll data is stored on our servers and will be used for commercial purposes. You'll most likely get Spam, E-Mails, Pop-up Windows - which\nyou fear to click.\nYou just did exactly what Dr.Browser wanted you to do.\nYou have just become a slave to Dr.Browser.\nYou are now imprisoned in the Cloud.\nAlongside millions of other people due to your lack of caution online.You have just become a slave to Dr.Browser.\nYou are now imprisoned in the Cloud.\nAlongside millions of other people due to your lack of caution online.", self)
        qf = QFont("Arial", 4,QFont.Bold)
        self.label.setFont(qf)
        self.label.move(50,440)
        self.but = QPushButton("Agree", self)
        self.but.setToolTip('Yes, you do')
        self.but.setGeometry(self.width()/2-120,self.height()/2+70,100,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Decline", self)
        self.but1.setToolTip("No, you don't")
        self.but1.setGeometry(self.width()/2,self.height()/2+70,100,50)
        self.but1.setCheckable(True)
        self.but1.clicked[bool].connect(self.otherButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def handleButton(self):
        self.w = MyWindowb()
        self.w.show()
        self.hide()


    def otherButton(self, down):
        if down:
            print('Sorry')
        else:
            print("Problem in System")

class MyWindowb(QWidget):
    def __init__(self):
        super(MyWindowb, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("Thank you for agreeing to our Terms of Agreement", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label.setFont(qf)
        self.label.move(110,50)
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))
        self.but1 = QPushButton("Continue", self)
        self.but1.setToolTip('DO IT')
        self.but1.setGeometry(self.width()/2-200,self.height()/2-120,300,100)
        self.but1.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))
        self.label2 = QLabel("Thank you for agreeing to our Terms of Agreement", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label2.setPixmap(QPixmap('Thumb-up.png'))
        self.label2.move(440,95)

    def handleButton(self):
            self.w = MyWindowu()
            self.w.show()
            self.hide()


class MyWindow3(QWidget):
    def __init__(self):
        super(MyWindow3, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("You are      doomed.        Welcome         to the            Cloud.", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label.setFont(qf)
        self.label.move(35,200)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))
        self.label4 = QLabel ("prisonbars", self)
        self.label4.setFont(qf)
        self.label4.move(500,70)
        self.label4.setPixmap(QPixmap('priso.png'))
        self.label4.move(00,30)
        self.but = QPushButton("Go Back", self)
        self.but.setToolTip('Not Accepted')
        self.but.setGeometry(self.width()/2-250,self.height()/2,100,50)
        self.but.setCheckable(True)
        self.but.clicked[bool].connect(self.handleButton)
        self.but1 = QPushButton("Ok", self)
        self.but1.setGeometry(self.width()/2+110,self.height()/2,100,50)
        self.but1.clicked.connect(self.otherButton)


    def otherButton(self):
        self.w = MyWindow4()
        self.w.show()
        self.hide()

    def handleButton(self, down):
        if down:
            print('Sorry')
        else:
            print("Problem in System")


class MyWindow4(QWidget):
    def __init__(self):
        super(MyWindow4, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("As you can imagine, Private C.\nentered all the Information\n- just as you did.\nHer digital entity was now completed.\nDr. Browser now had all the information\nneeded to find out where she was,\nwhat she looked like and\nwhat her intentions were.\nCaptured in the cloud, Private C.\nnow is a slave to Dr. Browser's corperation 'Transparency'.\nIt is your task now to free Private C.\nand to defeat Dr.Browser once and for all!", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,50)
        self.but = QPushButton("Continue", self)
        self.but.setGeometry(self.width()/2-350,self.height()/2+180,150,70)
        self.but.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))


    def handleButton(self):
        self.w = MyWindow5()
        self.w.show()
        self.hide()


class MyWindow5(QWidget):
    def __init__(self):
        super(MyWindow5, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("In order to free Private C.\nyou have to solve Dr. Browser's riddels.\nNo one has ever solved them before.\nYou will encounter questions with\nfour given answers,\nonly one of them is correct.\nIf you fail to find the correct answer\nPrivate C. will suffer great pain.\nSo good luck and\nmay the force be with you.", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,50)
        self.but = QPushButton("Accept", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-350,self.height()/2+160,100,50)
        self.but.clicked.connect(self.otherButton)
        self.but1 = QPushButton("Deny", self)
        self.but1.setGeometry(self.width()/2-230,self.height()/2+160,100,50)
        self.but1.setCheckable(True)
        self.but1.clicked[bool].connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        self.w = MyWindow9()
        self.w.show()
        self.hide()

    def handleButton(self, down):
        if down:
            print('You have to continue')
        else:
            print("Free her!")

class MyWindow9(QWidget):
    def __init__(self):
        super(MyWindow9, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label2 = QLabel("RIDDLE", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label2.setPixmap(QPixmap('u.png'))
        self.label2.move(570,120)
        self.label = QLabel("What is the answer\nto the Ultimate Question\nof Life,\nThe Universe,\nand Everything?", self)
        qf = QFont("AR CHRISTY", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,120)
        self.but = QPushButton("Faith", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-300,self.height()/2+120,130,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("42", self)
        self.but1.setGeometry(self.width()/2,self.height()/2+200,130,50)
        self.but1.clicked.connect(self.otherButton)
        self.but2 = QPushButton("Empathy",self)
        self.but2.setToolTip("HELP ME")
        self.but2.setGeometry(self.width()/2-300,self.height()/2+200,130,50)
        self.but2.clicked.connect(self.differentButton)
        self.but3 = QPushButton("Success", self)
        self.but3.setToolTip("HELP ME")
        self.but3.setGeometry(self.width()/2,self.height()/2+120,130,50)
        self.but3.clicked.connect(self.lastButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        self.w = MyWindowj()
        self.w.show()
        self.hide()

    def handleButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def differentButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def lastButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

class MyWindowj(QWidget):
    def __init__(self):
        super(MyWindowj, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label4 = QLabel ("deethough", self)
        self.label4.move(500,70)
        self.label4.setPixmap(QPixmap('d.png'))
        self.label4.move(50,-50)
        self.but = QPushButton("Continue", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-390,self.height()/2+235,100,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Go Back", self)
        self.but1.setGeometry(self.width()/2-270,self.height()/2+235,100,50)
        self.but1.clicked.connect(self.otherButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        sender = self.sender()
        sender.move(700,20)

    def handleButton(self):
        self.w = MyWindowo()
        self.w.show()
        self.hide()


class MyWindowo(QWidget):
    def __init__(self):
        super(MyWindowo, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label2 = QLabel("RIDDLE", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label2.setPixmap(QPixmap('u.png'))
        self.label2.move(570,120)
        self.label = QLabel("Agent C. got hacked one Sunday morning\nThe Police knows who they are going to arrest\nfrom this bit of Information:\n\nApril was getting the mail\nAlyssa was doing laundry\nReggie was cooking\nMark was planting flowers in the garden\nWho hacked Agent C.? ", self)
        qf = QFont("AR CHRISTY", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,60)
        self.but = QPushButton("Reggie", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-300,self.height()/2+120,130,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Mark", self)
        self.but1.setGeometry(self.width()/2,self.height()/2+200,130,50)
        self.but1.clicked.connect(self.otherButton)
        self.but2 = QPushButton("April",self)
        self.but2.setToolTip("HELP ME")
        self.but2.setGeometry(self.width()/2-300,self.height()/2+200,130,50)
        self.but2.clicked.connect(self.differentButton)
        self.but3 = QPushButton("Alyssa", self)
        self.but3.setToolTip("HELP ME")
        self.but3.setGeometry(self.width()/2,self.height()/2+120,130,50)
        self.but3.clicked.connect(self.lastButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def handleButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def differentButton(self):
        self.w = MyWindows()
        self.w.show()
        self.hide()

    def lastButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()


class MyWindows(QWidget):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("Correct,\nThe Police was able to track down the hacking\nto April, because there is no mail on Sundays!\nYou got one step closer to freeing Private C.\nKeep going!\n\nYou made Agent C. very proud.", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,120)
        self.but = QPushButton("Continue", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-350,self.height()/2+160,100,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Go Back", self)
        self.but1.setGeometry(self.width()/2-230,self.height()/2+160,100,50)
        self.but1.clicked.connect(self.otherButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        sender = self.sender()
        sender.move(700,20)

    def handleButton(self):
        self.w = MyWindowv()
        self.w.show()
        self.hide()


class MyWindowv(QWidget):
    def __init__(self):
        super(MyWindowv, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label2 = QLabel("RIDDLE", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label2.setPixmap(QPixmap('u.png'))
        self.label2.move(570,120)
        self.label = QLabel("A famous chemist was found murdered in his kitchen.\nThe police have narrowed it down to six suspects.\nThey know it was a two man job.\nTheir names:\nFelice, Maxwell, Archibald,\nNicolas, Jordan, and Xavier.\nA note was also found with the body:\n'26-3-58/28-27-57-16'.\n\nWho are the killers?", self)
        qf = QFont("AR CHRISTY", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,20)
        self.but = QPushButton("Felice and Maxwell", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-300,self.height()/2+120,130,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Jordan and Archibald", self)
        self.but1.setGeometry(self.width()/2,self.height()/2+200,130,50)
        self.but1.clicked.connect(self.otherButton)
        self.but2 = QPushButton("Felice and Nicholas",self)
        self.but2.setToolTip("HELP ME")
        self.but2.setGeometry(self.width()/2-300,self.height()/2+200,130,50)
        self.but2.clicked.connect(self.differentButton)
        self.but3 = QPushButton("Xavier and Maxwell", self)
        self.but3.setToolTip("HELP ME")
        self.but3.setGeometry(self.width()/2,self.height()/2+120,130,50)
        self.but3.clicked.connect(self.lastButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def handleButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def differentButton(self):
        self.w = MyWindowy()
        self.w.show()
        self.hide()

    def lastButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

class MyWindowy(QWidget):
    def __init__(self):
        super(MyWindowy, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("Correct,\nFelice and Nicholas are the murderers. The numbers\n\n'26-3-58/28-27-57-16'\n\ncorrespond\nto the atomic numbers on the periodic table\n of elements:\n\n'Fe-Li-Ce/Ni-Co-La-S'", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,30)
        self.label4 = QLabel ("chemistry", self)
        self.label4.setFont(qf)
        self.label4.move(500,70)
        self.label4.setPixmap(QPixmap('chemist.png'))
        self.label4.move(620,350)
        self.but = QPushButton("Continue", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-350,self.height()/2+160,100,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Go Back", self)
        self.but1.setGeometry(self.width()/2-230,self.height()/2+160,100,50)
        self.but1.clicked.connect(self.otherButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        sender = self.sender()
        sender.move(700,20)

    def handleButton(self):
        self.w = MyWindowm()
        self.w.show()
        self.hide()


class MyWindowm(QWidget):
    def __init__(self):
        super(MyWindowm, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label2 = QLabel("RIDDLE", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label2.setPixmap(QPixmap('u.png'))
        self.label2.move(570,120)
        self.label = QLabel("How many Internet Users\nin Germany\nwho have been victims\nto data abuse before,\nchange their passwords\non a regular basis?", self)
        qf = QFont("AR CHRISTY", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,120)
        self.but = QPushButton("28%", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-300,self.height()/2+120,130,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("23%", self)
        self.but1.setGeometry(self.width()/2,self.height()/2+200,130,50)
        self.but1.clicked.connect(self.otherButton)
        self.but2 = QPushButton("47%",self)
        self.but2.setToolTip("HELP ME")
        self.but2.setGeometry(self.width()/2-300,self.height()/2+200,130,50)
        self.but2.clicked.connect(self.differentButton)
        self.but3 = QPushButton("8%", self)
        self.but3.setToolTip("HELP ME")
        self.but3.setGeometry(self.width()/2,self.height()/2+120,130,50)
        self.but3.clicked.connect(self.lastButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        self.w = MyWindowi()
        self.w.show()
        self.hide()

    def handleButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def differentButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

    def lastButton(self):
        self.w = MyWindow8()
        self.w.show()
        self.hide()

class MyWindowi(QWidget):
    def __init__(self):
        super(MyWindowi, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("Correct,\nThe Handelsblatt has\nconducted research on said topic\nand came to the shocking\nresult that only 23%\nof people who have experienced\ndata abuse\ndeem it necessary to take action.\nIt is your resonsibility to make sure\nyour data is safe!", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(110,50)
        self.but = QPushButton("Continue", self)
        self.but.setToolTip("HELP ME")
        self.but.setGeometry(self.width()/2-350,self.height()/2+160,100,50)
        self.but.clicked.connect(self.handleButton)
        self.but1 = QPushButton("Go Back", self)
        self.but1.setGeometry(self.width()/2-230,self.height()/2+160,100,50)
        self.but1.clicked.connect(self.otherButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))

    def otherButton(self):
        sender = self.sender()
        sender.move(700,20)

    def handleButton(self):
        self.w = MyWindowl()
        self.w.show()
        self.hide()

class MyWindowl(QWidget):
    def __init__(self):
        super(MyWindowl, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label2 = QLabel("PARTY", self)
        qf = QFont("Arial", 20,QFont.Bold)
        self.label2.setFont(qf)
        self.label2.move(50,50)
        self.label2.setPixmap(QPixmap('c.png'))
        self.label2.move(180,20)
        self.label = QLabel("You did it, you freed Private C.\nCongratulations!\nData is a powerful resource\nand can be used in both ways\ngood and bad,\nNever underestimate the power\nof Dr. Browser,\nwho in this demonstration stands for\nanyone abusing your data\nfor purposes you didn't intend.\n Value your data, value your privacy!", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(295,150)
        self.but = QPushButton("Play again", self)
        self.but.setGeometry(self.width()/2-30,self.height()/2+230,100,50)
        self.but.clicked.connect(self.handleButton)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))


    def handleButton(self):
        self.w = MyWindow()
        self.w.show()
        self.hide()


class MyWindow8(QWidget):
    def __init__(self):
        super(MyWindow8, self).__init__()
        self.setGeometry(230,70,900,600)
        self.label = QLabel("*SCREAMS*\n\nPrivate C. suffers\nbecause you are\nnot focusing.\n\n\nConcentrate!", self)
        qf = QFont("Bradley Hand ITC", 20,QFont.StyleItalic)
        self.label.setFont(qf)
        self.label.move(35,50)
        self.setWindowTitle("Game of Buttons")
        self.setWindowIcon(QIcon('push-button-icon-png-2.png'))
        self.label4 = QLabel ("smileys", self)
        self.label4.setFont(qf)
        self.label4.move(800,50)
        self.label4.setPixmap(QPixmap('smiley.png'))
        self.label4.move(350,30)
        self.but = QPushButton("Try again", self)
        self.but.setToolTip('Free Private C.')
        self.but.setGeometry(self.width()/2-400,self.height()/2+150,120,80)
        self.but.clicked.connect(self.handleButton)

    def handleButton(self):
        self.w = MyWindow9()
        self.w.show()
        self.hide()


if __name__== '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    mywin.show()
    sys.exit(app.exec_())