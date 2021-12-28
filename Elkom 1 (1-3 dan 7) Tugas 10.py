# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:51:24 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

import sys

name_list, value_list = [], []

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
    
    elif option == "7":
        print("""\n [7. EXIT]
    SELAMAT TINGGAL DAN TERIMAKASIH TELAH BERKUNJUNG""")
        sys.exit()