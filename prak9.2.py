# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:30:48 2024

@author: Fairuz Maulidya
"""

class P9E2:
    @staticmethod
    def methodTambah(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return P9E2.tambah_int(x, y)
        elif isinstance(x, float) or isinstance(y, float):
            return P9E2.tambah_float(x, y)
        else:
            return "Tipe data tidak didukung"
    
    @staticmethod
    def tambah_int(x, y):
        return x + y
    
    @staticmethod
    def tambah_float(x, y):
        return x + y

# Contoh penggunaan
myNum1 = P9E2.methodTambah(8, 5)
myNum2 = P9E2.methodTambah(4.5, 6.5)
print("int:", myNum1)
print("float:", myNum2)
