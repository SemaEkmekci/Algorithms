
# Sema Nur Ekmekci
# 21100011050
# Ödev 1: Komşuluk matrisi çözümü




import pandas as pd
nodeDict = {}
alphabet = "ABCDEFGHIJKLMNOPRSTUVYZ"
kontrol = 1

def fileReading():
    print("\nDosya Okunuyor...\n")
    with open("neighborhoodMatrix.txt","r") as file:
                fileRead=file.readlines()
    numberEdge = int(fileRead[0])
    for i in range(numberEdge):   # Doğruluk matrisi dataFrame'i oluşturmak için sözlük yapısına uygun  formatta yerleştirdim. 

        matrixValue = []
        fileRead[i+1] = fileRead[i+1].replace("\n","")
        fileRead[i+1] = fileRead[i+1].split(",")
        for j in range(numberEdge):
            if(fileRead[i+1][j] == '-'):
                matrixValue.append(fileRead[i+1][j]+fileRead[i+1][j+1])
            elif(fileRead[i+1][j-1] == '-'):
                  matrixValue.append(fileRead[i+1][j+1])
            else:
                matrixValue.append(fileRead[i+1][j])
        nodeDict[alphabet[i]] = []
        nodeDict[alphabet[i]] = matrixValue    
    # print(nodeDict)
    df = pd.DataFrame(nodeDict,index=nodeDict.keys())    # Komşuluk matrisini oluşturdum.
    print("Komşuluk Matrisi\n~~~~~~~~~~~~~~~")
    print(df.transpose())    # Ekrana DataFrame'in tranpozunu yazdırıyor. Fakat arka planda saf hali ile işlem yapıyorum.
    # # print(df)
    return numberEdge,df

def dijkstraAlgorithm(numberEdge):
    newDf = {}
    nodes = []  # Başlangıç node'u hariç diğer nodeları ekledim.
    lines = []
    minimum = 0
    visitNode = []
    visitNodeValue = 0
    sayac = 0
    print("Dijkstra Algoritması Çalışıyor...")
    print("Nereden Nereye Gitmek İstiyorsunuz?\n")
    startNode = input("Başlangıç Node'u Seçiniz: ")
    finishNode = input("Bitiş Node'u Seçiniz: ")
    visitNode.append(startNode)
    startNodeLine = ['0']
    print(nodeDict)
    for i in range(numberEdge):
        if alphabet[i] != startNode:
            nodes.append(alphabet[i])
    newDf[startNode] = startNodeLine
    for i in nodes:
        newDf[i] = ['∞']
    j = startNode
    for k in range(len(nodeDict.keys())-2):
        if sayac == 0:
            a = -1
        else:
            a = -2
        newDf[startNode] = startNodeLine
        for i in range(len(nodeDict[j])):
            lines = newDf[alphabet[i]]
            if(alphabet[i] != startNode):
                if(nodeDict[j][i] == "0"):
                    if(newDf[alphabet[i]][a] != "∞"):
                        eklenecek = newDf[alphabet[i]][a : ]
                        lines.append(eklenecek[0])
                        lines.append(eklenecek[1])
                    else:
                        lines.append(newDf[alphabet[i]][a])
                        lines.append("-")
                    newDf[alphabet[i]] = lines
                elif(nodeDict[j][i] != "0"):
                    summ = visitNodeValue + int(nodeDict[j][i])
                    if( (newDf[alphabet[i]][a] == "∞") or summ < int(newDf[alphabet[i]][a])):
                        lines.append(str(summ))
                        lines.append(j)

                    else:
                        eklenecek = newDf[alphabet[i]][a : ]
                        lines.append(eklenecek[0])
                        lines.append(eklenecek[1])
                    newDf[alphabet[i]] = lines                 
                    
        kontrol = 0
        for m in range(len(nodes)):
            if len(visitNode) == numberEdge-1:
                if newDf[nodes[m]][-1] == '∞':
                    minimum = 0
                    break 
            if nodes[m] not in visitNode:
               kontrol = 1
               minimum = newDf[nodes[m]][-2]
               minNode = nodes[m]
               if minimum!="∞" and kontrol == 1:
                 break

        for k in range(len(nodes)):
            if nodes[k] not in visitNode:
               if(newDf[nodes[k]][-2]!="∞"):               
                    if(int(minimum) > int(newDf[nodes[k]][-2])):
                        minimum = newDf[nodes[k]][-2]
                        minNode = nodes[k]
        if (minimum == '∞'):
            break
        visitNode.append("Parent")
        visitNode.append(minNode)
        visitNodeValue = int(minimum)
        j = minNode

        
        writeDf = pd.DataFrame(newDf,index=visitNode)  # Komşuluk     matrisini oluşturdum.
        sayac+=1
        print(f"{sayac}.Adım\n-----------------------------\n{writeDf}\n\n")
        if(visitNode[-1] == finishNode):
            break
    # visitNodeLenght = len(visitNode)
    sayac = 0
    for i in visitNode:
        if i != "Parent":
            if (newDf[i][-1] in alphabet):
                sayac+=1
    resultList = []
    a = visitNode[-1]
    resultList.append(a)
    sayac-=1
    while sayac > 0:
        if(newDf[a][-1] != startNode):
            resultList.append(newDf[a][-1])
        a = newDf[a][-1]
        sayac-=1
    resultList = resultList[::-1]

    print("En kısa yol sonucu:",end=" ")
    print(f"{startNode} -->",end=" ")
    for i in resultList:
            print(i+" -->",end=" ")
    
    print(f"\nEn kısa yol uzunluğu: {newDf[visitNode[-1]][-2]}")


            


def bellmanFordAlgorithm():
    transposeDf = df.transpose()
    print(transposeDf)
    edgeWeight = {}
    edgeWeightBefore={}
    newDf = {}
    parentDf = {}
    startNodeParent = []
    sortList = []
    startNodeLine = []
    sayac = 0
    for i in nodeDict.keys():    # Edge ve Weight değerlerini bularak algoritmada kullanmak için bir sözlük yapısı oluşturdum.
        for j in nodeDict.keys():           
            if transposeDf[i][j] != '0':      
                edgeWeightParent = j + "-" + i
                sortList.append(edgeWeightParent)
                edgeWeightBefore[edgeWeightParent] = transposeDf[i][j]
                # print(transposeDf[i][j])
    sortList.sort()  
    for i in range(len(edgeWeightBefore)): # Edge - Weight sözlüğünü sıralı hale getirdim.
        edgeWeight[sortList[i]] = edgeWeightBefore[sortList[i]]
    control = True
    while control:
        startNode = input("Başlangıç Node'u seçiniz")
        if startNode in nodeDict.keys():
            print("Olmayan Node Girdiniz\n")
            control = False

    startNodeLine.append(0)
    newDf[startNode] = startNodeLine
    for i in nodeDict:
        lines = []
        if i !=startNode:
            lines.append('∞')
            newDf[i] = lines
    # print(edgeWeight)     
    print(newDf)

    startNodeParent.append('-')
    parentDf[startNode] = startNodeParent
    for i in nodeDict:
        lines = []
        if i != startNode:
            lines.append('-')
            parentDf[i] = lines
    print(parentDf)

    for i in range(len(nodeDict)-1):
        startNodeLine.append(0)
        kontrol = 0
        visitNode = [startNode]
        for j in edgeWeight.keys():
            parentControl = 0
            appendList = []
            edge = j.split("-")
            if(edge[1]!=startNode):
                if(newDf[edge[0]][-1] != '∞'):
                    edgeSum =  int(newDf[edge[0]][-1]) + int(edgeWeight[j])
                    if(newDf[edge[1]][-1] == '∞'):
                        for m in range(len(newDf[edge[1]])):
                            appendList.append(newDf[edge[1]][m])
                        appendList.append(str(edgeSum))
                        # minimum = str(edgeSum)
                        visitNode.append(edge[1])
                        newDf[edge[1]] = appendList                
                        parentControl = 1
                    else:
                        if(edgeSum < int(newDf[edge[1]][-1])):
                            if(len(newDf[edge[1]]) == sayac+2):
                                newDf[edge[1]].pop()
                                parentDf[edge[1]].pop()
                            for m in range(len(newDf[edge[1]])):
                                appendList.append(newDf[edge[1]][m])
                            appendList.append(str(edgeSum))    
                            visitNode.append(edge[1])
                            newDf[edge[1]] = appendList
                            parentControl = 1


            if parentControl == 1:
                lines = []
                for a in parentDf[edge[1]]:
                    lines.append(a)
                lines.append(edge[0])
                parentDf[edge[1]] = lines
   

        for l in nodeDict.keys():
            appendList = []
            if (l not in visitNode) :
                for n in newDf[l]:
                    appendList.append(n)
                appendList.append(newDf[l][-1])
                newDf[l] = appendList
        
        
        
        for a in parentDf.keys():
            lines = []
            if (((a not in visitNode) or (a == startNode)) and (len(parentDf[a]) != len(newDf[startNode]))):
                if(parentDf[a][-1] == '-'):
                    for b in parentDf[a]:
                        lines.append(b)
                    lines.append('-')
                    parentDf[a] = lines
                else:  
                    lines = []
                    for c in parentDf[a]:
                        lines.append(c)
                    lines.append(parentDf[a][-1])
                    parentDf[a] = lines
    
                    
        writeDf = pd.DataFrame(newDf)  # Komşuluk matrisini oluşturdum.
        writeParentDf = pd.DataFrame(parentDf)
        print(f"{sayac+1}.Adım\n---------------")
        print(f"\n{writeDf}")
        print(f"\nParent Table\n-----------------\n\n{writeParentDf}\n----------------") 
        sayac+=1    

numberEdge,df = fileReading()        # Kod çalıştığında ilk olarak dosyayı okuyor.

# Giriş Menüsü
while True:

    print("\n\n1) Dosya Okuma Yap\n2) Dijkstra Algoritması Çalıştır\n3)Bellman - Ford Algoritması Çalıştır\n4) Çıkış")
    secim = input("Seçim: ")

    if secim == '1':     # Kullanıcı dosyada güncelleme yapmış ise bu kod satırını çalıştırabilir.
        fileReading()
    elif secim == '2':
        dijkstraAlgorithm(numberEdge)
    elif secim == '3':
        bellmanFordAlgorithm()
    elif secim == '4':
         exit()
    else:
        print("Hatalı işlem yaptınız.")