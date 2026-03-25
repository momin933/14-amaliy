import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.son_tekshir import musbatmi
from utils.son_tekshir import musbatmi
from utils.juft_toq import juftmi
from utils.hisoblash import hisobla
from utils.orta_qiymat import orta
from utils.eng_katta import top
from utils.matn_uzunlik import uzunlik
from utils.teskari_matn import teskari
from utils.parol_tekshir import kuchlimi
from utils.musbat_sonlar import filtr

def menu():
    while True:
        print("\n" + "="*30)
        print("      LOYIHA MENYUSI")
        print("="*30)
        print("1 — Son musbat yoki manfiyligini tekshirish")
        print("2 — Juft yoki toq sonni aniqlash")
        print("3 — Ikki son ustida amal bajarish")
        print("4 — Sonlar ro'yxatining o'rtacha qiymati")
        print("5 — Ro'yxatdan eng katta sonni topish")
        print("6 — Matn uzunligini aniqlash")
        print("7 — Matnni teskari qilish")
        print("8 — Parol kuchliligini tekshirish")
        print("9 — Musbat sonlarni ajratib olish")
        print("0 — Dasturdan chiqish")
        print("="*30)

        tanlov = input("Tanlovingizni kiriting: ")

        if tanlov == "1":
            s = float(input("Sonni kiriting: "))
            natija = "Musbat" if musbatmi(s) else "Manfiy yoki nol"
            print(f"Natija: {natija}")

        elif tanlov == "2":
            s = int(input("Butun son kiriting: "))
            print(f"Natija: {juftmi(s)}")

        elif tanlov == "3":
            a = float(input("Birinchi sonni kiriting: "))
            b = float(input("Ikkinchi sonni kiriting: "))
            am = input("Amalni tanlang (+, -, *, /): ")
            print(f"Natija: {hisobla(a, b, am)}")

        elif tanlov == "4":
            data = input("Sonlarni bo'shliq (probel) bilan kiriting: ")
            lst = [float(x) for x in data.split()]
            print(f"O'rtacha qiymat: {orta(lst)}")

        elif tanlov == "5":
            data = input("Sonlarni bo'shliq bilan kiriting: ")
            lst = [float(x) for x in data.split()]
            print(f"Eng katta son: {top(lst)}")

        elif tanlov == "6":
            t = input("Matnni kiriting: ")
            print(f"Natija: {uzunlik(t)}")

        elif tanlov == "7":
            t = input("Matnni kiriting: ")
            print(f"Teskari matn: {teskari(t)}")

        elif tanlov == "8":
            p = input("Tekshirish uchun parolni kiriting: ")
            print(f"Parol holati: {kuchlimi(p)}")

        elif tanlov == "9":
            data = input("Sonlarni bo'shliq bilan kiriting: ")
            lst = [float(x) for x in data.split()]
            print(f"Faqat musbat sonlar: {filtr(lst)}")

        elif tanlov == "0":
            print("Dastur tugatildi. Xayr!")
            break

        else:
            print("Xato: Bunday menyu mavjud emas! Iltimos, 0-9 oralig'ida tanlang.")

if __name__ == "__main__":
    menu()
