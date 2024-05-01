# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:22:51 2024

@author: Fairuz Maulidya
"""

import math

class HitungVolume:
    @staticmethod
    def hitung_volume(bentuk, *args):
        if bentuk == "kubus":
            return HitungVolume.volume_kubus(*args)
        elif bentuk == "balok":
            return HitungVolume.volume_balok(*args)
        elif bentuk == "tabung":
            return HitungVolume.volume_tabung(*args)
        else:
            return "Bentuk bangun ruang tidak valid"
    
    @staticmethod
    def volume_kubus(sisi):
        return sisi ** 3
    
    @staticmethod
    def volume_balok(panjang, lebar, tinggi):
        return panjang * lebar * tinggi
    
    @staticmethod
    def volume_tabung(jari_jari, tinggi):
        return math.pi * jari_jari ** 2 * tinggi

# Contoh penggunaan
if __name__ == "__main__":
    hitung = HitungVolume()
    print('''====================
    Nama: Fairuz Maulidya      
    Nim: 064002300018          
    ================''')
    print("Volume kubus dengan sisi 5 adalah:", hitung.hitung_volume("kubus", 5), "cm^3")
    print("Volume balok dengan panjang 4, lebar 3, dan tinggi 6 adalah:", hitung.hitung_volume("balok", 4, 3, 6), "cm^3")
    print("Volume tabung dengan jari-jari 2 dan tinggi 8 adalah:", hitung.hitung_volume("tabung", 2, 8), "cm^3")
