# Ad - Soyad : Sema Nur Ekmekci
# Numara : 21100011050
# Ödev2 Kruskal's - Prim's Algoritması


# from AlgotihmUI import AlgorithmUI as ai
# from KruskalandPrimAlgorithm import KruskalandPrimAlgorithm
from AlgotihmUI_21100011050 import AlgorithmUI as ai
from KruskalandPrimAlgorithm_21100011050 import KruskalandPrimAlgorithm

def menu():
    alg = KruskalandPrimAlgorithm()
    print("1-) Kruskal's Algorithm\n2-) Prim's Algorithm\n3-) Çıkış")
    selection = input("Seçim: ")
    if selection == '1':
        a = alg.kruskalAlgorithm()
        ai.app("Kruskal's Algorithm",a[0],a[1])
    elif selection == '2':
        a =  alg.primsAlgorithm()
        ai.app("Prim's Algorithm",a[0],a[1])
    elif selection == "3":
        exit()
    else:
        print("Hatalı Seçim")

menu()