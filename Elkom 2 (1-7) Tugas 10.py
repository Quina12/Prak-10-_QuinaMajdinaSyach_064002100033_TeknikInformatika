# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:44:11 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

import sys

value_list, name_list = [], []

while True:
    print("\nProgram List")
    option = input(''' 1. Input Data
 2. View Data
 3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa
 4. Hitung Nilai Rata-Rata Tiap Praktikum
 5. Mencari Nilai Rata-Rata Praktikum Mahasiswa
 6. Update Nilai Praktikum Mahasiswa
 7. Exit 
              
 Pilih menu yang tersedia: ''')

    if option == "1":
        practice = []
        name_list.append(input(''' [1. INPUT DATA]
     Masukkan nama mahasiswa: '''))
        for i in range(3):
            practice.append(int(input("     Masukkan nilai praktikum {}: " .format(i+1))))
        value_list.append(practice)
    
    elif option == "2":
        print('''\n [2. VIEW DATA]
    NAMA  |  PRAK 1  |  PRAK 2  |  PRAK3
    ------------------------------------''')
        for name, value in zip(name_list, value_list):
            pract1, pract2, pract3 = value
            print(f"\t{name}\t|\t{pract1}\t\t|\t{pract2}\t\t|\t{pract3}")
    
    elif option == "3":
        print("\n [3.HITUNG PRAK TIAP MAHASISWA]")
        for name in name_list:
            value_data = value_list[name_list.index(name)]
            average = sum(value_data)/len(value_data)
            print(f"\t{name}\t = {average}")
    
    elif option == "4":
        print("\n [4. HITUNG RATA-RATA TIAP PRAK]")
        pract1, pract2, pract3 = [], [], []
        for value in value_list:
            pract1.append(value[0])
            pract2.append(value[1])
            pract3.append(value[2])
        average1 = sum(pract1)/len(pract1)
        print(f"\tRata-rata Prak 1 = {average1}")
        average2 = sum(pract2)/len(pract2)
        print(f"\tRata-rata Prak 2 = {average2}")
        average3 = sum(pract3)/len(pract3) 
        print(f"\tRata-rata Prak 3 = {average3}")
        
    elif option == "5":
        print("\n[5. MENCARI NILAI RATA-RATA PRAK TIAP MAHASISWA]")
        name = input("\tMasukkan nama mahasiswa: ")
        value = value_list[name_list.index(name)]
        average = sum(value)/len(value)
        print(f"\tRata-rata nilai praktikum {name} = {average}")
    
    elif option == "6":
        print("\n [6. UPDATE NILAI PRAK MAHASISWA]")
        title = input("\tMasukkan nama mahasiswa: ")
        value_to = int(input("\tIngin update nilai praktikum ke-: "))
        new_value = int(input("\tNilai baru: "))
        for i in value_list:
            if i [0] == title:
                i[value_to] = new_value
        value_list[name_list.index(title)][value_to - 1] = new_value
    
    elif option == "7":
        print("""\n [7. EXIT]
    SELAMAT TINGGAL DAN TERIMAKASIH TELAH BERKUNJUNG""")
        sys.exit()
    
    else:
        print("\n\tINVALID INPUT, SILAHKAN MASUKKAN ULANG (hanya terdapat pilihan (1-7))")