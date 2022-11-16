import sys
import numpy as np
import random
import time
import threading
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

class Patient:
  def __init__(self, x, y, illness, age, height):
    self.x=x
    self.y=y
    self.illness = illness
    self.age = age
    self.height=height

p1=Patient(3,11,"Schizofrenie paranoida",25,170)
p2=Patient(14,7,"Alzheimer",51,157)
p3=Patient(6,9,"Tulburare bipolara",33,164)
p4=Patient(12,16,"Parkinson",70,149)
dpg.highlight_table_cell(table_id, p1.x, p1.y, [123, 15, 200])
dpg.highlight_table_cell(table_id, p2.x, p2.y, [23, 45, 20])
dpg.highlight_table_cell(table_id, p3.x, p3.y, [3, 67, 2])
dpg.highlight_table_cell(table_id, p4.x, p4.y, [67, 198, 29])

#avem cntsteps si o data la 3 stepsi sta o secunda ca are halucinatii si se uita prin jur emoji fancy stelute pt schizofrenie

def incetiniri(p=Patient(x,y,ill,a,h)):
    if p.ill=="Schizofrenie paranoida":
        if cntsteps%3==0: 
            time.sleep(1) #%3 inseamna din3 in 3 sec
    if p.ill=="Parkinson":
        #for fiecare pas!!!
        time.sleep(0.2) #merge cu 0.2 mai incet decat restul pt ca are probleme motorii slay
    if p.ill=="Tulburare bipolara":
        if cntsteps%5==0:
            p.x=p.x-1
            p.y=p.y-1 #actualele coordonate scad cu 1? face pas inapoi pt ca are faza maniacala si nu mai e lucid si rational si idk
    if p.ill=="Alzheimer": 
        if cntsteps%4==0:
            time.sleep(1) #uita saracu ca vrea sa iasa din spital si face o pauza sa si aminteasca

#ar putea fi plantati asistenti prin spital si daca vrea sa treaca pacientul pe casuta cu asistent ii prins si endgame pt el