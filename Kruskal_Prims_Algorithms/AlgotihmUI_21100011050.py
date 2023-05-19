# Ad - Soyad : Sema Nur Ekmekci
# Numara : 21100011050
# Ödev2 Kruskal's - Prim's Algoritması

import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QPixmap
# from KruskalandPrimAlgorithm import KruskalandPrimAlgorithm
from KruskalandPrimAlgorithm_21100011050 import KruskalandPrimAlgorithm

class AlgorithmUI(QMainWindow):
    def __init__(self,algorithmName,sayac,weightDict):
        super(AlgorithmUI,self).__init__()
        self.sayacStart = 0
        self.sayacEnd = sayac
        self.algorithmName = algorithmName
        self.weightDict = weightDict
        self.setWindowTitle(self.algorithmName)
        self.setGeometry(500,500,900,900)
        self.initUi()
        

    def initUi(self):

        self.title = QtWidgets.QLabel(self)
        self.title.setText(self.algorithmName)
        self.title.setStyleSheet("color:red")
        self.title.setFont(QtGui.QFont("Sanserif " , 20))
        self.title.move(95,25)
        self.title.resize(300,50)

        self.prevBtn = QtWidgets.QPushButton(self)
        self.prevBtn.setText('Prev')
        self.prevBtn.move(70,75)
        self.prevBtn.resize(150,35)
        self.prevBtn.clicked.connect(self.prevBtnClicked)

        self.nextBtn = QtWidgets.QPushButton(self)
        self.nextBtn.setText('Next')
        self.nextBtn.move(230,75)
        self.nextBtn.resize(150,35)
        self.nextBtn.clicked.connect(self.nextBtnClicked)

        self.stepLabel = QtWidgets.QLabel(self)
        self.stepLabel.move(450,30)
        self.stepLabel.resize(100,100)
        self.stepLabel.setStyleSheet("color:green")
        self.stepLabel.setFont(QtGui.QFont("Sanserif " , 20))
        self.stepLabel.resize(150,50)


        self.weightLabel = QtWidgets.QLabel(self)
        self.weightLabel.move(450,60)
        self.weightLabel.resize(100,100)
        self.weightLabel.setStyleSheet("color:blue")
        self.weightLabel.setFont(QtGui.QFont("Sanserif " , 20))
        self.weightLabel.resize(150,80)

        self.imgLabel = QtWidgets.QLabel(self)
        self.imgLabel.move(50,100)
        self.imgLabel.resize(800,800)
    
    def prevBtnClicked(self):
        print("Tıklandı Prev")
        print(self.sayacStart)

        if self.sayacStart > 0:
            
            img="graphImg\\"+str(self.sayacStart)+".png"
            qpixmap = QPixmap(img)
            self.imgLabel.setPixmap(qpixmap)
            self.sayacStart-=1
            self.stepLabel.setText(str(self.sayacStart+1)+".Adım")
            
            sumWeight = 0
            for i in range(self.sayacStart):
                sumWeight += int(self.weightDict[i])
            self.weightLabel.setText("Ağırlık: "+ str(sumWeight))

    
    def nextBtnClicked(self):
        print("Tıklandı Next")
        print(self.sayacStart)
        print("SayacEnd: ",self.sayacEnd)
        if self.sayacEnd != self.sayacStart:
            self.stepLabel.setText(str(self.sayacStart+1)+".Adım")

            self.sayacStart+=1
            img="graphImg\\"+str(self.sayacStart)+".png"
            qpixmap = QPixmap(img)
            self.imgLabel.setPixmap(qpixmap)
            sumWeight = 0
            for i in range(self.sayacStart):
                sumWeight += int(self.weightDict[i])
            self.weightLabel.setText("Ağırlık: "+ str(sumWeight))


    def app(algorithmName,sayac,weightDict):
    
        app = QApplication(sys.argv)
        win = AlgorithmUI(algorithmName,sayac,weightDict)
        win.show()
        sys.exit(app.exec_())

