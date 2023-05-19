# Ad - Soyad : Sema Nur Ekmekci
# Numara : 21100011050
# Ödev2 Kruskal's - Prim's Algoritması

import  pydot
import pandas as pd

class KruskalandPrimAlgorithm:
    
    def __init__(self):
        self.neighbordList=[]
        self.neighbordListDict={}
        self.alphabet = "ABCDEFGHIJKLMNOPRSTUVYZ"
        self.minToMaxDict={}
        self.visitNode = []
        self.visitNodeWeight = []

    
        # Dosya Okuma Yaptım 
        with open("komsulukMatrisi.txt","r") as file:
            matrix = file.readlines()

      

        # Dosyayı okuduktan sonra uygun formatta    verileri aldım.
        for i in range(len(matrix)):
                line = matrix[i].replace("\n","")
                self.neighbordList.append(matrix[i].replace  ("\n","").split(","))
                if i==0:
                    numberEdge = matrix[0]
                else:
                    self.neighbordListDict[self.alphabet[i-1]] =  self.neighbordList[i]


        # Komşuluk matrisinden edgeleri ve nodeları alarak yolları karışık bi şekilde minToMaxDict  sözlüğüne ekledim.
        # sayac = 0
        for i in self.neighbordListDict:
            for j in range(int(numberEdge)):
                if self.neighbordListDict[i][j] != '0':
                    key = i + " - " +self.alphabet[j]
                    self.minToMaxDict[key] = self.neighbordListDict[i][j]
                    
        df = pd.DataFrame(self.neighbordListDict,index = self.neighbordListDict.keys())

        
        print(df.transpose())    # Komşuluk matrisini oluşturdum.


    def graphCreate(self ,visitNode,minimumDict):
            
           
            graph = pydot.Dot(graph_type="graph",   strict=True)
            sayac = 0
            
            for i in visitNode:
            # Graph çiz.
                sayac+=1
                graph.add_edge(pydot.Edge(i.split(" - ")[0],i.split(" - ")[1],color="blue", fontcolor="red",label = minimumDict[i]))
                self.visitNodeWeight.append(minimumDict[i])
                # self.graph.add_edge(parent, node, label='subclass')
                # graph.edge(i.split(" - ")[0], i.split(" - ")[1], label='nfdsagasd', len='1.00')
                graph.write_png("graphImg\\"+str(sayac)+".png")
            # print("Ağırlıklar--->",self.visitNodeWeight)
            
            return self.visitNodeWeight


    def kruskalAlgorithm(self):
        self.visitNode = []
        algorithName = "Kruskal's Algorithm"
        # nodeSayaci = 0
        registerNode = 0
        # minToMaxDict sözlüğündeki verileri sıralı hale getirdim.
        sayac = 0
        minimumDict = dict()
        for j in range(len(self.minToMaxDict)):
            for i in self.minToMaxDict.keys():
                if sayac == 0:
                    minimum = self.minToMaxDict[i]
                    minKey = i
                if int(minimum) > int(self.minToMaxDict  [i]):
                    minimum = self.minToMaxDict[i] 
                    minKey = i
                sayac+=1
            sayac = 0 
            self.minToMaxDict.pop(minKey)
            minimumDict[minKey] = minimum

   
       
        for i in minimumDict:
            left = i.split(" - ")[0]
            right = i.split(" - ")[1]
            ekle = 1
            
            sayac = 2
            while sayac>0:

                if sayac == 2:
                    ara = left
                    controlNode = right
                else:
                    ara = right
                    controlNode = left
                tempVisitNode = []
                for a in self.visitNode:
                    tempVisitNode.append(a)
                while True:

                    controlDevammı = 0

                    if controlNode != ara:
                        for j in tempVisitNode[::-1]:
                            if ara == j.split(" - ")[0]:
                                ara = j.split(" - ")[1]
                                if controlNode == ara:
                                    ekle = 0
                                    break
                                tempVisitNode.remove(j)
                                controlDevammı = 1
                            elif ara == ara == j.split(" - ")[1]:
                                ara = j.split(" - ")[0]
                                if controlNode == ara:
                                    ekle = 0
                                    break
                                tempVisitNode.remove(j)
                                controlDevammı = 1
                        if controlDevammı == 0:
                            break
                    else:
                        ekle = 0
                        break
                sayac-=1
            if ekle == 1:
                self.visitNode.append(i)       
        weightDict = KruskalandPrimAlgorithm.graphCreate(self,self.visitNode,minimumDict)
        return (len(self.visitNode),weightDict)

    def primsAlgorithm(self):
        startNode = input("Başlangıç Node'u Seçiniz: ")
        gelinenNode = startNode
        self.visitNode = []
        weightDict = []
        acikYollar = {}
        
        for j in self.minToMaxDict:
            for i in self.minToMaxDict:  # Başlanıç nodeunun yollarını acikyollar sözlüğüne koydum.
                if startNode in i:
                    acikYollar[i] = self.minToMaxDict[i]
            print(acikYollar)

            for i in acikYollar:  # Karşılaştırma yapabilmek için minEdge oluşturdum.
                minEdge = acikYollar[i]
                minNode = i
                break
            
            for i in acikYollar:
                if minEdge < acikYollar[i]:
                    minEdge = acikYollar[i]
                    minNode = i

            left = minNode.split(" - ")[0]
            right = minNode.split(" - ")[1]
            leftSayac = 0
            rightSayac = 0
            
            for i in self.visitNode:  # circle kontrolü 
                if left in i:
                    leftSayac += 1
                if right in i:
                    rightSayac += 1
            ekle = 1
            if leftSayac == 2 or rightSayac == 2:
                ekle = 0

            if ekle == 1:
                self.visitNode.append(minNode)
                weightDict.append(self.minToMaxDict[minNode])
                acikYollar.pop(minNode)

            left = minNode.split(" - ")[0]
            right = minNode.split(" - ")[1]
            if left == gelinenNode:
                gidilenNode = right
            elif right == gelinenNode:
                gidilenNode = left

            startNode = gidilenNode

        return (self.visitNode,weightDict)