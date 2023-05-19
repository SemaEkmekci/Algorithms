import pandas as pd
import time

# Ad-Soyad: Sema Nur Ekmekci
# Numara: 21100011050
# LZW algoritmama file.txt dosyasından girdiyi alıyor. LZW.txt olarak çıktı veriyor.


# abacadabacaabaaca -> Derste yapılan örnek (lzw algorithm)


# Dataframe olarak çıktı vermek için sözlük oluşturdum.
dfSozluk = {
    "STEP": [],
    "INPUT": [],
    "STRİNG+CHAR": [],
    "INTABLE": [],
    "TEMP": [],
    "ATD": [],
    "OUTPUT": [],
}


# Dosya okuma
def dosyaOkuma():
    with open("file.txt", "r") as file:
        metin = file.read()
    print(metin)
    print(len(metin))
    return metin


def boyutHesapla(elemanSayisi, metinElemanSayisi):
    us = 0
    # Her karakter kaç bitle temsil edilebilir?
    while True:
        if elemanSayisi >= 2**us:
            us += 1
        else:
            break
    print(us)
    boyut = us * metinElemanSayisi
    return boyut


# İlk boyut hesaplama


# LZW Algorithm
def lzwAlgorithm():
    metin = dosyaOkuma()
    # Metinde kaç karakter var?
    sozluk = {}
    sayac = 0
    for i in metin:
        if i not in sozluk:
            sayac += 1
            sozluk[i] = sayac
    print(sozluk)
    print(len(sozluk))

    ilkBoyut = boyutHesapla(len(sozluk), len(metin))
    print("İlk Boyut: ", ilkBoyut)

    global baslangic
    baslangic = time.perf_counter()
    stepSayac = 1
    temp = ""
    for i in metin:
        dfSozluk["STEP"].append(stepSayac)
        stepSayac += 1
        dfSozluk["INPUT"].append(i)
        stringChar = temp + i
        dfSozluk["STRİNG+CHAR"].append(stringChar)
        if stringChar in sozluk:
            dfSozluk["INTABLE"].append("Y")
            dfSozluk["ATD"].append("-")
            dfSozluk["OUTPUT"].append("-")
            temp = stringChar  # !!
            dfSozluk["TEMP"].append(temp)
        else:
            sozluk[stringChar] = len(sozluk) + 1
            dfSozluk["INTABLE"].append("N")
            dfSozluk["ATD"].append(stringChar)
            sozluk[stringChar] = len(sozluk) + 1
            dfSozluk["OUTPUT"].append(stringChar[:-1])
            temp = i
            dfSozluk["TEMP"].append(temp)

    # Son satırı oluşturdum.
    dfSozluk["INPUT"].append("-")
    dfSozluk["INTABLE"].append("-")
    dfSozluk["ATD"].append("-")
    dfSozluk["STEP"].append("-")
    dfSozluk["STRİNG+CHAR"].append("-")
    dfSozluk["TEMP"].append("-")
    dfSozluk["OUTPUT"].append(temp)
    writeDf = pd.DataFrame(dfSozluk)
    global bitis
    bitis = time.perf_counter()
    print(writeDf)
    # Son boyut hesaplama.
    sonElemanSayisi = 0
    for i in dfSozluk["OUTPUT"]:
        if i == "-":
            continue
        else:
            sonElemanSayisi += 1
    global sonBoyut
    sonBoyut = boyutHesapla(len(sozluk), sonElemanSayisi)
    print("Son Boyut: ", sonBoyut)
    print("Sözlük", sozluk)
    # Dosyaya yazma işlemi
    with open("LZW.txt", "w", encoding="utf-8") as file:
        file.write(
            f"Dosyanın Sıkıştırılmadan Önceki Boyutu: {ilkBoyut} bit\nDosyanın Sıkıştırıldıktan Sonraki Boyutu: {sonBoyut} bit\nLZW Algoritmasının Çalışma Süresi:  + {str((bitis-baslangic))} ms\n"
        )


# Huffman Algorithm
def huffmanAlgorithm():
    metin = dosyaOkuma()
    # Karakter frekansı buldum.
    global sozluk
    sozluk = {}
    for i in metin:  # frekans buldum.
        if i not in sozluk:
            sozluk[i] = 1
        else:
            sozluk[i] += 1
    print(sozluk)
    agacYapisiKokler = (
        []
    )  # agacYapisi class ından oluşturduğum her nesneyi burada tutacağım.
    while len(sozluk) != 0:
        # Ağaç yapısını kolay bir şekilde oluşturabilmek için agacYapisi sınıfını oluşturdum. Bu class dan her bir node için    nesne oluşturarak ağaç yapısını oluştarağım
        class agacYapisi(object):
            # constructer yapısı
            def __init__(self, node, left=None, right=None):
                self.node = node
                self.sol = left
                self.sag = right

        # Kıyaslama yapabilmek için 2 tane minimum değer belirledim
        sayac = 1
        for j, i in sozluk.items():
            if sayac == 1:
                min1 = i
                min1Key = j
            elif sayac == 2:
                min2 = i
                min2Key = j
            sayac += 1
        # Sözlükteki diğer değerlerle kıyaslayarak 2 tane minimum değeri aldım.
        for i, j in sozluk.items():
            if j < min1:
                min1 = j
                min1Key = i
        for i, j in sozluk.items():
            if j < min2:
                if min1Key != i:
                    min2 = j
                    min2Key = i
        if min1Key == min2Key:
            for i in agacYapisiKokler:  # İkinci Tur
                sozluk[i.node] = i.node

        print(
            f"sol çocuk frekans: {min1}\nsol çocuk node ismi: {min1Key}\nsağ çocuk: {min2}\nsağ çocuk node ismi: {min2Key}"
        )
        sozluk.pop(min1Key)
        try:
            sozluk.pop(min2Key)
        except:
            pass
        kokAdi = min1 + min2
        print(f"Kök Adı: {kokAdi}\n")
        kok = agacYapisi(kokAdi, min1Key, min2Key)
        # sozluk[str(kokAdi)] = kokAdi
        agacYapisiKokler.append(kok)


while True:
    secim = input("1) Huffman Algoritması\n2) LZW Algoritması\n3) Çıkış\nSeçim: ")

    if secim == "1":
        huffmanAlgorithm()
    elif secim == "2":
        lzwAlgorithm()
    elif secim == "3":
        exit()
    else:
        print("Hatalı Seçim")
