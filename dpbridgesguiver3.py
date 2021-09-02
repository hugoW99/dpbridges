import sys

import tkinter as tk
import tkinter as ttk
from tkinter import filedialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import rc
import matplotlib.ticker
from matplotlib.font_manager import FontProperties

import mysql.connector as mysql
from mysql.connector import Error

import matplotlib.dates as md
import numpy as np
import pandas as pd
import datetime as dt
import time

from tkscrolledframe import ScrolledFrame
from tkcalendar import Calendar

from datetime import date


window = tk.Tk()
window.lift()
window.title('MOS Douglas Park Bridges Data')
window.state('zoomed')
#window.resizable(width=False, height=False)
#window.grid_propogate(0)

# border
frm_top = tk.Frame(window, bg='grey26', height=10)
frm_right = tk.Frame(window, bg='grey26', width=10)
frm_left = tk.Frame(window, bg='grey26', width=10)
frm_bottom = tk.Frame(window, bg='grey26', height=10)

# Chart Frame - Scrolled Frame - add inner_frame to populate with graphs
canvasFrame = ScrolledFrame(window, bg="grey45", width = 640)
inner_frame = canvasFrame.display_widget(tk.Frame, fit_width=True)


# Welcome
frm_welcome = tk.Frame(inner_frame)
frm_welcome.pack(side=tk.TOP)

lbl_welcome = tk.Label(frm_welcome, text="Douglas Park Bridges Monitoring System Data")
lbl_welcome.config(font=("Courier", 16), fg='blue')
lbl_welcome.pack(side=tk.TOP)

welcome = "Welcome to the Douglas Park Monitoring System Database. The page contains daily averaged data, unaveraged data and diagnostic information. Full data overviews are shown at the bottom of the page."
txt_welcome = tk.Label(frm_welcome, text=welcome)
txt_welcome.pack(side=tk.TOP)


# Averaged Data Frame
frm_avg = tk.Frame(inner_frame)
frm_avg.pack(side=tk.TOP)

# Text
lbl_avg = tk.Label(frm_avg, text="Averaged Data")
lbl_avg.config(font=("Courier", 16), fg='blue')
lbl_avg.pack(side=tk.TOP)

#txt_avg.pack(side=tk.TOP)

txt = "The Following section contains the daily averaged data. Please select the dates and sensor(s) you would like to access. All data is relative to time. if you want the unaveraged data, please scroll down to the second section"
txt_avg = tk.Label(frm_avg, text=txt)
txt_avg.pack(side=tk.TOP)
#txt_avg.insert(tk.END, txt)

# Dates
#lbl_dates = tk.Label(frm_avg, text="Dates:")
#lbl_dates.pack(padx=20, side=tk.TOP, anchor='nw')

date_frm_avg = tk.Frame(frm_avg)
date_frm_avg.pack(side=tk.TOP)

lbl_from = tk.Label(date_frm_avg, text="From:")
lbl_from.pack(padx=20, side=tk.LEFT)

today_from = date.today()
today_from = today_from.strftime("%d%m%Y")
day_from = int(today_from[:2])
month_from = int(today_from[2:4])
year_from = int(today_from[4:])
cal_from = Calendar(date_frm_avg, selectmode='day',
                    year = year_from, month = month_from, day = day_from)

cal_from.pack(pady=5, side=tk.LEFT)

lbl_to = tk.Label(date_frm_avg, text="To:")
lbl_to.pack(padx=20, side=tk.LEFT)

today_to = date.today()
today_to = today_to.strftime("%d%m%Y")
day_to = int(today_to[:2])
month_to = int(today_to[2:4])
year_to = int(today_to[4:])
cal_to = Calendar(date_frm_avg, selectmode='day',
                    year = year_to, month = month_to, day = day_to)

cal_to.pack(pady=5, side=tk.LEFT)

lbl_sensor = tk.Label(date_frm_avg, text="Sensor:")
lbl_sensor.pack(padx=20, side=tk.LEFT)



sns_frame_avg = tk.Frame(date_frm_avg)
sns_frame_avg.pack(side=tk.LEFT)


sensors = ['S_NB_S2W', 'S_NB_S2E', 'S_NB_S1E', 'S_NB_S1W', 'S_SB_S2W', 'S_SB_S2E',
           'S_SB_S1E', 'S_SB_S1W', 'T_NB_S2W', 'T_NB_S2E', 'T_NB_S1E', 'T_NB_S1W',
           'T_SB_S2W', 'T_SB_S2E', 'T_SB_S1E', 'T_SB_S1W', 'TP_NB_S2W', 'TP_NB_S2E',
           'TP_NB_S1E', 'TP_NB_S1W', 'TP_SB_S2W', 'TP_SB_S2E', 'TP_SB_S1E', 'TP_SB_S1W']

vars_avg = []

var_avg1 = tk.IntVar()
chk_avg1 = tk.Checkbutton(sns_frame_avg, text=sensors[0], variable=var_avg1)
chk_avg1.grid(row=0, column=0)
vars_avg.append(var_avg1)

var_avg2 = tk.IntVar()
chk_avg2 = tk.Checkbutton(sns_frame_avg, text=sensors[1], variable=var_avg2)
chk_avg2.grid(row=0, column=1)
vars_avg.append(var_avg2)

var_avg3 = tk.IntVar()
chk_avg3 = tk.Checkbutton(sns_frame_avg, text=sensors[2], variable=var_avg3)
chk_avg3.grid(row=0, column=2)
vars_avg.append(var_avg3)

var_avg4 = tk.IntVar()
chk_avg4 = tk.Checkbutton(sns_frame_avg, text=sensors[3], variable=var_avg4)
chk_avg4.grid(row=0, column=3)
vars_avg.append(var_avg4)

var_avg5 = tk.IntVar()
chk_avg5 = tk.Checkbutton(sns_frame_avg, text=sensors[4], variable=var_avg5)
chk_avg5.grid(row=0, column=4)
vars_avg.append(var_avg5)

var_avg6 = tk.IntVar()
chk_avg6 = tk.Checkbutton(sns_frame_avg, text=sensors[5], variable=var_avg6)
chk_avg6.grid(row=0, column=5)
vars_avg.append(var_avg6)

var_avg7 = tk.IntVar()
chk_avg7 = tk.Checkbutton(sns_frame_avg, text=sensors[6], variable=var_avg7)
chk_avg7.grid(row=0, column=6)
vars_avg.append(var_avg7)

var_avg8 = tk.IntVar()
chk_avg8 = tk.Checkbutton(sns_frame_avg, text=sensors[7], variable=var_avg8)
chk_avg8.grid(row=0, column=7)
vars_avg.append(var_avg8)

var_avg9 = tk.IntVar()
chk_avg9 = tk.Checkbutton(sns_frame_avg, text=sensors[8], variable=var_avg9)
chk_avg9.grid(row=1, column=0)
vars_avg.append(var_avg9)

var_avg10 = tk.IntVar()
chk_avg10 = tk.Checkbutton(sns_frame_avg, text=sensors[9], variable=var_avg10)
chk_avg10.grid(row=1, column=1)
vars_avg.append(var_avg10)

var_avg11 = tk.IntVar()
chk_avg11 = tk.Checkbutton(sns_frame_avg, text=sensors[10], variable=var_avg11)
chk_avg11.grid(row=1, column=2)
vars_avg.append(var_avg11)

var_avg12 = tk.IntVar()
chk_avg12 = tk.Checkbutton(sns_frame_avg, text=sensors[11], variable=var_avg12)
chk_avg12.grid(row=1, column=3)
vars_avg.append(var_avg12)

var_avg13 = tk.IntVar()
chk_avg13 = tk.Checkbutton(sns_frame_avg, text=sensors[12], variable=var_avg13)
chk_avg13.grid(row=1, column=4)
vars_avg.append(var_avg13)

var_avg14 = tk.IntVar()
chk_avg14 = tk.Checkbutton(sns_frame_avg, text=sensors[13], variable=var_avg14)
chk_avg14.grid(row=1, column=5)
vars_avg.append(var_avg14)

var_avg15 = tk.IntVar()
chk_avg15 = tk.Checkbutton(sns_frame_avg, text=sensors[14], variable=var_avg15)
chk_avg15.grid(row=1, column=6)
vars_avg.append(var_avg15)

var_avg16 = tk.IntVar()
chk_avg16 = tk.Checkbutton(sns_frame_avg, text=sensors[15], variable=var_avg16)
chk_avg16.grid(row=1, column=7)
vars_avg.append(var_avg16)

var_avg17 = tk.IntVar()
chk_avg17 = tk.Checkbutton(sns_frame_avg, text=sensors[16], variable=var_avg17)
chk_avg17.grid(row=2, column=0)
vars_avg.append(var_avg17)

var_avg18 = tk.IntVar()
chk_avg18 = tk.Checkbutton(sns_frame_avg, text=sensors[17], variable=var_avg18)
chk_avg18.grid(row=2, column=1)
vars_avg.append(var_avg18)

var_avg19 = tk.IntVar()
chk_avg19 = tk.Checkbutton(sns_frame_avg, text=sensors[18], variable=var_avg19)
chk_avg19.grid(row=2, column=2)
vars_avg.append(var_avg19)

var_avg20 = tk.IntVar()
chk_avg20 = tk.Checkbutton(sns_frame_avg, text=sensors[19], variable=var_avg20)
chk_avg20.grid(row=2, column=3)
vars_avg.append(var_avg20)

var_avg21 = tk.IntVar()
chk_avg21 = tk.Checkbutton(sns_frame_avg, text=sensors[20], variable=var_avg21)
chk_avg21.grid(row=2, column=4)
vars_avg.append(var_avg21)

var_avg22 = tk.IntVar()
chk_avg22 = tk.Checkbutton(sns_frame_avg, text=sensors[21], variable=var_avg22)
chk_avg22.grid(row=2, column=5)
vars_avg.append(var_avg22)

var_avg23 = tk.IntVar()
chk_avg23 = tk.Checkbutton(sns_frame_avg, text=sensors[22], variable=var_avg23)
chk_avg23.grid(row=2, column=6)
vars_avg.append(var_avg23)

var_avg24 = tk.IntVar()
chk_avg24 = tk.Checkbutton(sns_frame_avg, text=sensors[23], variable=var_avg24)
chk_avg24.grid(row=2, column=7)
vars_avg.append(var_avg24)

graph_frm_avg = tk.Frame(frm_avg)
graph_frm_avg.pack(side=tk.TOP, fill="both", expand=True)

def close_avg():
    for widget in graph_frm_avg.winfo_children():
        widget.destroy()
    

def query_avg(sensors, start, finish):
    conn = mysql.connect(host='localhost',
                         database='douglas park bridges',
                         username='root',
                         password='zk89peTN')
    
    cursor = conn.cursor()
    sensors_joined = ', '.join(sensors)
    query = f"SELECT Timestamp, {sensors_joined} FROM averaged WHERE Timestamp > '{start}' and Timestamp < '{finish}';"
    
    #print(query)
    
    cursor.execute(query)
    records = cursor.fetchall()
    #print(records)
    
    timestamp = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    
    alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
    
    
    for row in records:
        timestamp.append(row[0])
        i = 1
        while i < len(row):
            alphabet[i].append(row[i])
            i += 1
    
    #print("appended rows")
    
    filled = []
    for lst in alphabet:
        if len(lst) > 0:
            filled.append(lst)
    
    rc('mathtext', default='regular')
    
    fig = plt.figure(figsize=(5,4))
    ax1 = fig.add_subplot(111)
    
    plt.subplots_adjust(left=0.112, top=0.9, bottom=0.198, right=0.84)
    
    xfmt = md.DateFormatter('%Y-%m-%d')
    ax1.xaxis.set_major_formatter(xfmt)
    
    lns1 = ''
    lns2 = ''
    lns3 = ''
    lns4 = ''
    lns5 = ''
    lns6 = ''
    lns7 = ''
    lns8 = ''
    lns9 = ''
    lns10 = ''
    lns11 = ''
    lns12 = ''
    lns13 = ''
    lns14 = ''
    lns15 = ''
    lns16 = ''
    lns17 = ''
    lns18 = ''
    lns19 = ''
    lns20 = ''
    lns21 = ''
    lns22 = ''
    lns23 = ''
    lns24 = ''
    
    lnsx = [lns1, lns2, lns3, lns4, lns5, lns6, lns7, lns8, lns9, lns10, lns11, lns12,
            lns13, lns14, lns15, lns16, lns17, lns18, lns19, lns20, lns21, lns22,
            lns23, lns24]
    
    
    
    i = 0
    while i < len(filled):
        lnsx[i] = ax1.plot(md.date2num(timestamp), filled[i], '-', label=sensors[i])
        i += 1
    
    lns = []
    for l in lnsx:
        if len(l) > 0:
            lns.append(l)
    
    #nticksX = 10
    #ax1.yaxis.set_major_locator(matplotlib.ticker.LineraLocator(nticksX))
    
    #nticksY = 10
    #ax1.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticksX))
    
    #labs = [l.get_label() for l in lns]
    
    L = ax1.legend()
    i = 0
    while i < len(lns):
        L.get_texts()[i].set_text(sensors[i])
        i += 1
    
    lined = {}
    for legline, origline in zip(leg.get_lines(), lns):
        legline.set_picker(True)
        lined[legline] = origline

    def on_pick(event):
        legline = event.artist
        origline = lined[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()


    ax1.grid(color='w', linestyle='solid')
    ax1.set_facecolor('#E6E6E6')
    ax1.set_axisbelow(True)


    # specify the master            
    canvas = FigureCanvasTkAgg(fig, master=graph_frm_avg)
    fig.canvas.mpl_connect('pick_event', on_pick)
    canvas.draw()

    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha='right')

    canvas.get_tk_widget().pack(side=tk.TOP, fill="both", expand=True)
    
    tk.Button(graph_frm_avg, text="Clear", command=close_avg).pack(side=tk.TOP, anchor='nw')


def getChecked():
    selected_avg = []
    count = 0
    for var in vars_avg:
        #print(var.get())
        if var.get():
            selected_avg.append(sensors[count])
        count += 1
    #print(selected_avg)
    ##print(vars)
    
    date_from = cal_from.get_date()
    if len(date_from) == 7:
        if date_from[1] == '/':
            month = f"0{date_from[0]}"
            day = date_from[2:4]
            year = date_from[5:]
        else:
            month = date_from[:2]
            day = f"0{date_from[3]}"
            year = date_from[5:]
    elif len(date_from) == 6:
        month = f"0{date_from[0]}"
        day = f"0{date_from[2]}"
        year = date_from[4:]
    else:
        month = date_from[0:2]
        day = date_from[3:5]
        year = date_from[6:]
    date_from = f"20{year}-{month}-{day}"
    #print("< 8", date_from)
    
    date_to = cal_to.get_date()
    if len(date_to) == 7:
        if date_to[1] == '/':
            month = f"0{date_to[0]}"
            day = date_to[2:4]
            year = date_to[5:]
        else:
            month = date_to[:2]
            day = f"0{date_to[3]}"
            year = date_to[5:]
    elif len(date_to) == 6:
        month = f"0{date_to[0]}"
        day = f"0{date_to[2]}"
        year = date_to[4:]
    else:
        month = date_to[0:2]
        day = date_to[3:5]
        year = date_to[6:]
    date_to = f"20{year}-{month}-{day}"
    #print("< 8", date_to)
    
    query_avg(selected_avg, date_from, date_to)


go_avg = tk.Button(date_frm_avg, text="Go", command=getChecked)
go_avg.pack(padx=15, side=tk.LEFT)


# Unaveraged Data Frame
frm_unavg = tk.Frame(inner_frame)
frm_unavg.pack(side=tk.TOP)

# Text
lbl_unavg = tk.Label(frm_unavg, text="Unaveraged Data")
lbl_unavg.config(font=("Courier", 16), fg='blue')
lbl_unavg.pack(side=tk.TOP)

#txt_avg.pack(side=tk.TOP)

unaveraged = "The Following section contains the daily unaveraged data. Please select the dates and sensor(s) you would like to access. All data is relative to time."
txt_unavg = tk.Label(frm_avg, text=unaveraged)
txt_unavg.pack(side=tk.TOP)
#txt_avg.insert(tk.END, txt)

# Dates
#lbl_dates = tk.Label(frm_avg, text="Dates:")
#lbl_dates.pack(padx=20, side=tk.TOP, anchor='nw')

date_frm_unavg = tk.Frame(frm_unavg)
date_frm_unavg.pack(side=tk.TOP)

lbl_from_unavg = tk.Label(date_frm_unavg, text="From:")
lbl_from_unavg.pack(padx=20, side=tk.LEFT)

today_from_unavg = date.today()
today_from_unavg = today_from_unavg.strftime("%d%m%Y")
day_from_unavg = int(today_from_unavg[:2])
month_from_unavg = int(today_from_unavg[2:4])
year_from_unavg = int(today_from_unavg[4:])
cal_from_unavg = Calendar(date_frm_unavg, selectmode='day',
                    year = 2017, month = 1, day = 1)

cal_from_unavg.pack(pady=5, side=tk.LEFT)

lbl_to_unavg = tk.Label(date_frm_unavg, text="To:")
lbl_to_unavg.pack(padx=20, side=tk.LEFT)

today_to_unavg = date.today()
today_to_unavg = today_to_unavg.strftime("%d%m%Y")
day_to_unavg = int(today_to_unavg[:2])
month_to_unavg = int(today_to_unavg[2:4])
year_to_unavg = int(today_to_unavg[4:])
cal_to_unavg = Calendar(date_frm_unavg, selectmode='day',
                    year = year_to_unavg, month = month_to_unavg, day = day_to_unavg)

cal_to_unavg.pack(pady=5, side=tk.LEFT)

lbl_sensor_unavg = tk.Label(date_frm_unavg, text="Sensor:")
lbl_sensor_unavg.pack(padx=20, side=tk.LEFT)



sns_frame_unavg = tk.Frame(date_frm_unavg)
sns_frame_unavg.pack(side=tk.LEFT)


sensors_unavg = ['S_NB_S2W', 'S_NB_S2E', 'S_NB_S1E', 'S_NB_S1W', 'S_SB_S2W', 'S_SB_S2E',
           'S_SB_S1E', 'S_SB_S1W', 'T_NB_S2W', 'T_NB_S2E', 'T_NB_S1E', 'T_NB_S1W',
           'T_SB_S2W', 'T_SB_S2E', 'T_SB_S1E', 'T_SB_S1W', 'TP_NB_S2W', 'TP_NB_S2E',
           'TP_NB_S1E', 'TP_NB_S1W', 'TP_SB_S2W', 'TP_SB_S2E', 'TP_SB_S1E', 'TP_SB_S1W']

vars_unavg = []

var_unavg1 = tk.IntVar()
chk_unavg1 = tk.Checkbutton(sns_frame_unavg, text=sensors[0], variable=var_unavg1)
chk_unavg1.grid(row=0, column=0)
vars_unavg.append(var_unavg1)

var_unavg2 = tk.IntVar()
chk_unavg2 = tk.Checkbutton(sns_frame_unavg, text=sensors[1], variable=var_unavg2)
chk_unavg2.grid(row=0, column=1)
vars_unavg.append(var_unavg2)

var_unavg3 = tk.IntVar()
chk_unavg3 = tk.Checkbutton(sns_frame_unavg, text=sensors[2], variable=var_unavg3)
chk_unavg3.grid(row=0, column=2)
vars_unavg.append(var_unavg3)

var_unavg4 = tk.IntVar()
chk_unavg4 = tk.Checkbutton(sns_frame_unavg, text=sensors[3], variable=var_unavg4)
chk_unavg4.grid(row=0, column=3)
vars_unavg.append(var_unavg4)

var_unavg5 = tk.IntVar()
chk_unavg5 = tk.Checkbutton(sns_frame_unavg, text=sensors[4], variable=var_unavg5)
chk_unavg5.grid(row=0, column=4)
vars_unavg.append(var_unavg5)

var_unavg6 = tk.IntVar()
chk_unavg6 = tk.Checkbutton(sns_frame_unavg, text=sensors[5], variable=var_unavg6)
chk_unavg6.grid(row=0, column=5)
vars_unavg.append(var_unavg6)

var_unavg7 = tk.IntVar()
chk_unavg7 = tk.Checkbutton(sns_frame_unavg, text=sensors[6], variable=var_unavg7)
chk_unavg7.grid(row=0, column=6)
vars_unavg.append(var_unavg7)

var_unavg8 = tk.IntVar()
chk_unavg8 = tk.Checkbutton(sns_frame_unavg, text=sensors[7], variable=var_unavg8)
chk_unavg8.grid(row=0, column=7)
vars_unavg.append(var_unavg8)

var_unavg9 = tk.IntVar()
chk_unavg9 = tk.Checkbutton(sns_frame_unavg, text=sensors[8], variable=var_unavg9)
chk_unavg9.grid(row=1, column=0)
vars_unavg.append(var_unavg9)

var_unavg10 = tk.IntVar()
chk_unavg10 = tk.Checkbutton(sns_frame_unavg, text=sensors[9], variable=var_unavg10)
chk_unavg10.grid(row=1, column=1)
vars_unavg.append(var_unavg10)

var_unavg11 = tk.IntVar()
chk_unavg11 = tk.Checkbutton(sns_frame_unavg, text=sensors[10], variable=var_unavg11)
chk_unavg11.grid(row=1, column=2)
vars_unavg.append(var_unavg11)

var_unavg12 = tk.IntVar()
chk_unavg12 = tk.Checkbutton(sns_frame_unavg, text=sensors[11], variable=var_unavg12)
chk_unavg12.grid(row=1, column=3)
vars_unavg.append(var_unavg12)

var_unavg13 = tk.IntVar()
chk_unavg13 = tk.Checkbutton(sns_frame_unavg, text=sensors[12], variable=var_unavg13)
chk_unavg13.grid(row=1, column=4)
vars_unavg.append(var_unavg13)

var_unavg14 = tk.IntVar()
chk_unavg14 = tk.Checkbutton(sns_frame_unavg, text=sensors[13], variable=var_unavg14)
chk_unavg14.grid(row=1, column=5)
vars_unavg.append(var_unavg14)

var_unavg15 = tk.IntVar()
chk_unavg15 = tk.Checkbutton(sns_frame_unavg, text=sensors[14], variable=var_unavg15)
chk_unavg15.grid(row=1, column=6)
vars_unavg.append(var_unavg15)

var_unavg16 = tk.IntVar()
chk_unavg16 = tk.Checkbutton(sns_frame_unavg, text=sensors[15], variable=var_unavg16)
chk_unavg16.grid(row=1, column=7)
vars_unavg.append(var_unavg16)

var_unavg17 = tk.IntVar()
chk_unavg17 = tk.Checkbutton(sns_frame_unavg, text=sensors[16], variable=var_unavg17)
chk_unavg17.grid(row=2, column=0)
vars_unavg.append(var_unavg17)

var_unavg18 = tk.IntVar()
chk_unavg18 = tk.Checkbutton(sns_frame_unavg, text=sensors[17], variable=var_unavg18)
chk_unavg18.grid(row=2, column=1)
vars_unavg.append(var_unavg18)

var_unavg19 = tk.IntVar()
chk_unavg19 = tk.Checkbutton(sns_frame_unavg, text=sensors[18], variable=var_unavg19)
chk_unavg19.grid(row=2, column=2)
vars_unavg.append(var_unavg19)

var_unavg20 = tk.IntVar()
chk_unavg20 = tk.Checkbutton(sns_frame_unavg, text=sensors[19], variable=var_unavg20)
chk_unavg20.grid(row=2, column=3)
vars_unavg.append(var_unavg20)

var_unavg21 = tk.IntVar()
chk_unavg21 = tk.Checkbutton(sns_frame_unavg, text=sensors[20], variable=var_unavg21)
chk_unavg21.grid(row=2, column=4)
vars_unavg.append(var_unavg21)

var_unavg22 = tk.IntVar()
chk_unavg22 = tk.Checkbutton(sns_frame_unavg, text=sensors[21], variable=var_unavg22)
chk_unavg22.grid(row=2, column=5)
vars_unavg.append(var_unavg22)

var_unavg23 = tk.IntVar()
chk_unavg23 = tk.Checkbutton(sns_frame_unavg, text=sensors[22], variable=var_unavg23)
chk_unavg23.grid(row=2, column=6)
vars_unavg.append(var_unavg23)

var_unavg24 = tk.IntVar()
chk_unavg24 = tk.Checkbutton(sns_frame_unavg, text=sensors[23], variable=var_unavg24)
chk_unavg24.grid(row=2, column=7)
vars_unavg.append(var_unavg24)

graph_frm_unavg = tk.Frame(frm_unavg)
graph_frm_unavg.pack(side=tk.TOP, fill="both", expand=True)

def clearCharts_unavg():
        for widget in graph_frm_unavg.winfo_children():
            widget.destroy()

def query_unavg(sensors, start, finish):
    conn = mysql.connect(host='localhost',
                         database='douglas park bridges',
                         username='root',
                         password='zk89peTN')
    
    cursor = conn.cursor()
    sensors_joined = ', '.join(sensors)
    query = f"SELECT Timestamp, {sensors_joined} FROM unaveraged WHERE Timestamp >= '{start}' and Timestamp <= '{finish}';"
    
    #print(query)
    
    cursor.execute(query)
    records = cursor.fetchall()
    #print(records)
    
    timestamp = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    
    alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
    
    
    for row in records:
        timestamp.append(row[0])
        i = 1
        while i < len(row):
            alphabet[i].append(row[i])
            i += 1
    
    #print("appended rows")
    
    filled = []
    for lst in alphabet:
        if len(lst) > 0:
            filled.append(lst)
    
    rc('mathtext', default='regular')
    
    fig = plt.figure(figsize=(5,4))
    ax1 = fig.add_subplot(111)
    
    plt.subplots_adjust(left=0.112, top=0.9, bottom=0.198, right=0.84)
    
    xfmt = md.DateFormatter('%Y-%m-%d')
    ax1.xaxis.set_major_formatter(xfmt)
    
    lns1 = ''
    lns2 = ''
    lns3 = ''
    lns4 = ''
    lns5 = ''
    lns6 = ''
    lns7 = ''
    lns8 = ''
    lns9 = ''
    lns10 = ''
    lns11 = ''
    lns12 = ''
    lns13 = ''
    lns14 = ''
    lns15 = ''
    lns16 = ''
    lns17 = ''
    lns18 = ''
    lns19 = ''
    lns20 = ''
    lns21 = ''
    lns22 = ''
    lns23 = ''
    lns24 = ''
    
    lnsx = [lns1, lns2, lns3, lns4, lns5, lns6, lns7, lns8, lns9, lns10, lns11, lns12,
            lns13, lns14, lns15, lns16, lns17, lns18, lns19, lns20, lns21, lns22,
            lns23, lns24]
    
    
    
    i = 0
    while i < len(filled):
        lnsx[i] = ax1.plot(md.date2num(timestamp), filled[i], '-', label=sensors[i])
        i += 1
    
    lns = []
    for l in lnsx:
        if len(l) > 0:
            lns.append(l)
    
    #labels = '+'.join(lns)
    #nticksX = 10
    #ax1.yaxis.set_major_locator(matplotlib.ticker.LineraLocator(nticksX))
    
    #nticksY = 10
    #ax1.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticksX))
    
    labs = [sensors]
    
    fontP = FontProperties()
    fontP.set_size('small')

    L = ax1.legend()
    i = 0
    while i < len(lns):
        L.get_texts()[i].set_text(sensors[i])
        i += 1
    
    lined = {}
    for legline, origline in zip(leg.get_lines(), lns):
        legline.set_picker(True)
        lined[legline] = origline

    def on_pick(event):
        legline = event.artist
        origline = lined[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()


    ax1.grid(color='w', linestyle='solid')
    ax1.set_facecolor('#E6E6E6')
    ax1.set_axisbelow(True)


    # specify the master            
    canvas = FigureCanvasTkAgg(fig, master=graph_frm_unavg)
    fig.canvas.mpl_connect('pick_event', on_pick)
    canvas.draw()

    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha='right')

    canvas.get_tk_widget().pack(side=tk.TOP, fill="both", expand=True)
    
    tk.Button(graph_frm_unavg, text='Clear', command=clearCharts_unavg).pack(side=tk.TOP)


def getChecked_unavg():
    selected_unavg = []
    count = 0
    for var in vars_unavg:
        #print(var.get())
        if var.get():
            selected_unavg.append(sensors[count])
        count += 1
    #print(selected_unavg)
    ##print(vars)
    
    date_from_unavg = cal_from_unavg.get_date()
    if len(date_from_unavg) == 7:
        if date_from_unavg[1] == '/':
            month = f"0{date_from_unavg[0]}"
            day = date_from_unavg[2:4]
            year = date_from_unavg[5:]
        else:
            month = date_from_unavg[:2]
            day = f"0{date_from_unavg[3]}"
            year = date_from_unavg[5:]
    elif len(date_from_unavg) == 6:
        month = f"0{date_from_unavg[0]}"
        day = f"0{date_from_unavg[2]}"
        year = date_from_unavg[4:]
    else:
        month = date_from_unavg[0:2]
        day = date_from_unavg[3:5]
        year = date_from_unavg[6:]
    date_from_unavg = f"20{year}-{month}-{day}"
    #print("< 8", date_from_unavg)
    
    date_to_unavg = cal_to_unavg.get_date()
    if len(date_to_unavg) == 7:
        if date_to_unavg[1] == '/':
            month = f"0{date_to_unavg[0]}"
            day = date_to_unavg[2:4]
            year = date_to_unavg[5:]
        else:
            month = date_to_unavg[:2]
            day = f"0{date_to_unavg[3]}"
            year = date_to_unavg[5:]
    elif len(date_to_unavg) == 6:
        month = f"0{date_to_unavg[0]}"
        day = f"0{date_to_unavg[2]}"
        year = date_to_unavg[4:]
    else:
        month = date_to_unavg[0:2]
        day = date_to_unavg[3:5]
        year = date_to_unavg[6:]
    date_to_unavg = f"20{year}-{month}-{day}"
    #print("< 8", date_to_unavg)
    
    query_unavg(selected_unavg, date_from_unavg, date_to_unavg)


go_unavg = tk.Button(date_frm_unavg, text="Go", command=getChecked_unavg)
go_unavg.pack(padx=15, side=tk.LEFT)


# FBG Health Frame
frm_fbg = tk.Frame(inner_frame)
frm_fbg.pack(side=tk.TOP)

date_frm_fbg = tk.Frame(frm_fbg)
date_frm_fbg.pack(side=tk.TOP)

# Text
lbl_fbg = tk.Label(date_frm_fbg, text="FBG Health")
lbl_fbg.config(font=("Courier", 16), fg='blue')
lbl_fbg.pack(side=tk.TOP)

#txt_avg.pack(side=tk.TOP)

txt = "This Section shows the FBG peak range and power level for the specified dates. This information is used to understand whether there is a risk of erroneous data from FBGs being too close to each other, and whether an FBG peak level is deterioraing over time. All data is relative to time."
txt_fbg = tk.Label(date_frm_fbg, text=txt)
txt_fbg.pack(side=tk.TOP)
#txt_avg.insert(tk.END, txt)

# Dates
#lbl_dates = tk.Label(frm_fbg, text="Dates:")
#lbl_dates.pack(padx=20, side=tk.TOP, anchor='nw')

lbl_from_fbg = tk.Label(date_frm_fbg, text="From:")
lbl_from_fbg.pack(padx=20, side=tk.LEFT)

today_from_fbg = date.today()
today_from_fbg = today_from_fbg.strftime("%d%m%Y")
day_from_fbg = int(today_from_fbg[:2])
month_from_fbg = int(today_from_fbg[2:4])
year_from_fbg = int(today_from_fbg[4:])
cal_from_fbg = Calendar(date_frm_fbg, selectmode='day',
                    year = year_from_fbg, month = month_from_fbg, day = day_from_fbg)

cal_from_fbg.pack(pady=5, side=tk.LEFT)

lbl_to_fbg = tk.Label(date_frm_fbg, text="To:")
lbl_to_fbg.pack(padx=20, side=tk.LEFT)

today_to_fbg = date.today()
today_to_fbg = today_to_fbg.strftime("%d%m%Y")
day_to_fbg = int(today_to_fbg[:2])
month_to_fbg = int(today_to_fbg[2:4])
year_to_fbg = int(today_to_fbg[4:])
cal_to_fbg = Calendar(date_frm_fbg, selectmode='day',
                    year = year_to_fbg, month = month_to_fbg, day = day_to_fbg)

cal_to_fbg.pack(pady=5, side=tk.LEFT)

lbl_sensor_fbg = tk.Label(date_frm_fbg, text="Sensor:")
lbl_sensor_fbg.pack(padx=20, side=tk.LEFT)



sns_frame_fbg = tk.Frame(date_frm_fbg)
sns_frame_fbg.pack(side=tk.LEFT)

sensors_fbg = ['S_NB_S2W', 'S_NB_S2E', 'S_NB_S1E', 'S_NB_S1W', 'S_SB_S2W', 'S_SB_S2E',
           'S_SB_S1E', 'S_SB_S1W', 'T_NB_S2W', 'T_NB_S2E', 'T_NB_S1E', 'T_NB_S1W',
           'T_SB_S2W', 'T_SB_S2E', 'T_SB_S1E', 'T_SB_S1W', 'TP_NB_S2W', 'TP_NB_S2E',
           'TP_NB_S1E', 'TP_NB_S1W', 'TP_SB_S2W', 'TP_SB_S2E', 'TP_SB_S1E', 'TP_SB_S1W']

vars = []

var1 = tk.IntVar()
chk1 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[0], variable=var1)
chk1.grid(row=0, column=0)
vars.append(var1)

var2 = tk.IntVar()
chk2 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[1], variable=var2)
chk2.grid(row=0, column=1)
vars.append(var2)

var3 = tk.IntVar()
chk3 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[2], variable=var3)
chk3.grid(row=0, column=2)
vars.append(var3)

var4 = tk.IntVar()
chk4 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[3], variable=var4)
chk4.grid(row=0, column=3)
vars.append(var4)

var5 = tk.IntVar()
chk5 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[4], variable=var5)
chk5.grid(row=0, column=4)
vars.append(var5)

var6 = tk.IntVar()
chk6 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[5], variable=var6)
chk6.grid(row=0, column=5)
vars.append(var6)

var7 = tk.IntVar()
chk7 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[6], variable=var7)
chk7.grid(row=0, column=6)
vars.append(var7)

var8 = tk.IntVar()
chk8 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[7], variable=var8)
chk8.grid(row=0, column=7)
vars.append(var8)

var9 = tk.IntVar()
chk9 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[8], variable=var9)
chk9.grid(row=1, column=0)
vars.append(var9)

var10 = tk.IntVar()
chk10 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[9], variable=var10)
chk10.grid(row=1, column=1)
vars.append(var10)

var11 = tk.IntVar()
chk11 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[10], variable=var11)
chk11.grid(row=1, column=2)
vars.append(var11)

var12 = tk.IntVar()
chk12 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[11], variable=var12)
chk12.grid(row=1, column=3)
vars.append(var12)

var13 = tk.IntVar()
chk13 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[12], variable=var13)
chk13.grid(row=1, column=4)
vars.append(var13)

var14 = tk.IntVar()
chk14 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[13], variable=var14)
chk14.grid(row=1, column=5)
vars.append(var14)

var15 = tk.IntVar()
chk15 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[14], variable=var15)
chk15.grid(row=1, column=6)
vars.append(var15)

var16 = tk.IntVar()
chk16 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[15], variable=var16)
chk16.grid(row=1, column=7)
vars.append(var16)

var17 = tk.IntVar()
chk17 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[16], variable=var17)
chk17.grid(row=2, column=0)
vars.append(var17)

var18 = tk.IntVar()
chk18 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[17], variable=var18)
chk18.grid(row=2, column=1)
vars.append(var18)

var19 = tk.IntVar()
chk19 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[18], variable=var19)
chk19.grid(row=2, column=2)
vars.append(var19)

var20 = tk.IntVar()
chk20 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[19], variable=var20)
chk20.grid(row=2, column=3)
vars.append(var20)

var21 = tk.IntVar()
chk21 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[20], variable=var21)
chk21.grid(row=2, column=4)
vars.append(var21)

var22 = tk.IntVar()
chk22 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[21], variable=var22)
chk22.grid(row=2, column=5)
vars.append(var22)

var23 = tk.IntVar()
chk23 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[22], variable=var23)
chk23.grid(row=2, column=6)
vars.append(var23)

var24 = tk.IntVar()
chk24 = tk.Checkbutton(sns_frame_fbg, text=sensors_fbg[23], variable=var24)
chk24.grid(row=2, column=7)
vars.append(var24)

graph_frm_fbg = tk.Frame(frm_fbg)
graph_frm_fbg.pack(side=tk.TOP, fill="both", expand=True)

def query_fbg(sensors, start, finish):
    conn = mysql.connect(host='localhost',
                         database='douglas park bridges',
                         username='root',
                         password='zk89peTN')
    
    cursor = conn.cursor()
    sensors_joined = ', '.join(sensors)
    query_power = f"SELECT {sensors_joined} FROM power WHERE Timestamp >= '{start}' and Timestamp <= '{finish}' limit 1;"
    
    #print(query_power)
    
    cursor.execute(query_power)
    power = cursor.fetchall()
    #print(power)
    
    timestamp = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    
    alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
    
    
    for row in power:
        #timestamp.append(row[0])
        i = 0
        while i < len(row):
            alphabet[i].append(row[i])
            i += 1
    
    #print("appended rows")
    
    filled = []
    for lst in alphabet:
        if len(lst) > 0:
            filled.append(lst)
    
    query_wav = f"SELECT {sensors_joined} FROM wavelengths WHERE Timestamp >= '{start}' and Timestamp <= '{finish}';"
    
    cursor.execute(query_wav)
    wav = cursor.fetchall()
    print('records:', wav)
    
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    
    alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
    
    
    for row in wav:
        #timestamp.append(row[0])
        i = 0
        while i < len(wav[0]):
            alphabet[i].append(row[i])
            i += 1
    
    #print("appended rows")
    
    filled_wav = []
    for lst in alphabet:
        if len(lst) > 0:
            filled_wav.append(lst)
    
    print("Filled:", filled_wav)
    
    wav_avg = []
    wav_max = []
    wav_min = []
    for w in filled_wav:
        wav_avg.append(float(sum(w)/len(w)))
        wav_max.append(float(max(w)))
        wav_min.append(float(min(w)))
    
    print('average:', wav_avg)
    print('max:', wav_max)
    print('min:', wav_min)
    
    fig = plt.figure(figsize=(5, 4))

    ax = fig.add_subplot(111)

    plt.subplots_adjust(left=0.1, bottom=0.195)

    width = 0.35
    width_max = 0.1
    ax.bar(wav_avg, filled, width, align='center', color='r')
    ax.bar(wav_max, filled, width_max, align='center', color='b')
    ax.bar(wav_min, filled, width_max, align='center', color='b')
    ax.set_xlabel('Wavelengths (nm)')
    ax.set_ylabel('Power (db)')
    ax.set_xticks(filled_wav)
    ax.set_yticks(np.arange(0, 61, 10))
    ax.set_title('NB Wavelengths and Power')

    canvas = FigureCanvasTkAgg(fig, master=graph_frm_fbg)
    canvas.draw()

    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')

    canvas.get_tk_widget().pack(fill="both", expand=True)


def getChecked_fbg():
    selected_fbg = []
    count = 0
    for var in vars:
        if var.get():
            selected_fbg.append(sensors_fbg[count])
        count += 1
    #print(selected_fbg)
    
    date_from_fbg = cal_from_fbg.get_date()
    if len(date_from_fbg) == 7:
        if date_from_fbg[1] == '/':
            month = f"0{date_from_fbg[0]}"
            day = date_from_fbg[2:4]
            year = date_from_fbg[5:]
        else:
            month = date_from_fbg[:2]
            day = f"0{date_from_fbg[3]}"
            year = date_from_fbg[5:]
    elif len(date_from_fbg) == 6:
        month = f"0{date_from_fbg[0]}"
        day = f"0{date_from_fbg[2]}"
        year = date_from_fbg[4:]
    else:
        month = date_from_fbg[0:2]
        day = date_from_fbg[3:5]
        year = date_from_fbg[6:]
    date_from_fbg = f"20{year}-{month}-{day}"
    #print("< 8", date_from_fbg)
    
    date_to_fbg = cal_to_fbg.get_date()
    if len(date_to_fbg) == 7:
        if date_to_fbg[1] == '/':
            month = f"0{date_to_fbg[0]}"
            day = date_to_fbg[2:4]
            year = date_to_fbg[5:]
        else:
            month = date_to_fbg[:2]
            day = f"0{date_to_fbg[3]}"
            year = date_to_fbg[5:]
    elif len(date_to_fbg) == 6:
        month = f"0{date_to_fbg[0]}"
        day = f"0{date_to_fbg[2]}"
        year = date_to_fbg[4:]
    else:
        month = date_to_fbg[0:2]
        day = date_to_fbg[3:5]
        year = date_to_fbg[6:]
    date_to_fbg = f"20{year}-{month}-{day}"
    #print("< 8", date_to_fbg)
    
    query_fbg(selected_fbg, date_from_fbg, date_to_fbg)


go_fbg = tk.Button(date_frm_fbg, text="Go", command=getChecked_fbg)
go_fbg.pack(padx=15, side=tk.LEFT)


# DP Bridges Overview
frm_overview = tk.Frame(inner_frame)
frm_overview.pack(side=tk.TOP)

lbl_overview = tk.Label(frm_overview, text="DP Bridges Overview")
lbl_overview.config(font=("Courier", 16), fg='blue')
lbl_overview.pack(side=tk.TOP)

overview = "The below graphs show an overview of all FBG data since the monitoring system began, and a snapshot of the most recent FBG peak and power level data."
txt_overview = tk.Label(frm_overview, text=overview)
txt_overview.pack(side=tk.TOP)

frm_graph_overview = tk.Frame(frm_overview)
frm_graph_overview.pack(side=tk.TOP)

timer_id = None

def start_loading(n=0):
    global timer_id
    gif = giflist[n%len(giflist)]
    canvas.create_image(gif.width()//2, gif.height()//2, image=gif)
    timer_id = root.after(100, start_loading, n+1)

def stop_loading():
    if timer_id:
        root.after_cancel(timer_id)
        canvas.delet(ALL)

canvas1 = tk.Canvas(master=frm_graph_overview)

canvas2 = tk.Canvas(master=frm_graph_overview, bg='red')

canvas3 = tk.Canvas(master=frm_graph_overview, bg='yellow')

canvas4 = tk.Canvas(master=frm_graph_overview, bg='blue')        


#ent_frmInDepth.grid(row=1, column=1, columnspan=2, sticky="ew")
canvas1.grid(row=0, column=0, sticky='nswe')
canvas2.grid(row=0, column=1, sticky='nswe')

canvas3.grid(row=1, column=0, sticky='nswe')
canvas4.grid(row=1, column=1, sticky='nswe')



#frm_menu.grid(row=1, column=1, padx=(5,0), sticky="nsew")
#frm_space_left.grid(row=3, column=1, sticky="nsew")
#frm_query.grid(row=3, column=1, sticky="ew")
#toolbarFrameInDepth.grid(row=3,column=2)

frm_graph_overview.grid_rowconfigure([0,1], weight=1)
frm_graph_overview.grid_columnconfigure([0,1], weight=1)


conn = mysql.connect(host='localhost',
             database='Douglas Park Bridges',
             username='root',
             password='zk89peTN')

cursor = conn.cursor()

#print('getting NB_Avg data')
start = time.time()

DatesNB_avg = []
S_NB_S2W_avg = []
S_NB_S2E_avg = []
S_NB_S1E_avg = []
S_NB_S1W_avg = []
T_NB_S2W_avg = []
T_NB_S2E_avg = []
T_NB_S1E_avg = []
T_NB_S1W_avg = []
TP_NB_S2W_avg = []
TP_NB_S2E_avg = []
TP_NB_S1E_avg = []
TP_NB_S1W_avg = []

cursor.execute('SELECT timestamp, s_nb_s2w, s_nb_s2e, s_nb_s1e, s_nb_s1w, t_nb_s2w, t_nb_s2e, t_nb_s1e, t_nb_s1w, tp_nb_s2w, tp_nb_s2e, tp_nb_s1e, tp_nb_s1w FROM Averaged')
nb_avg_data = cursor.fetchall()

for row in nb_avg_data:
    DatesNB_avg.append(row[0])
    S_NB_S2W_avg.append(row[1])
    S_NB_S2E_avg.append(row[2])
    S_NB_S1E_avg.append(row[3])
    S_NB_S1W_avg.append(row[4])
    T_NB_S2W_avg.append(row[5])
    T_NB_S2E_avg.append(row[6])
    T_NB_S1E_avg.append(row[7])
    T_NB_S1W_avg.append(row[8])
    TP_NB_S2W_avg.append(row[9])
    TP_NB_S2E_avg.append(row[10])
    TP_NB_S1E_avg.append(row[11])
    TP_NB_S1W_avg.append(row[12])

#print(time.time() - start)

#print('getting SB_Avg data')
start = time.time()

DatesSB_avg = []
S_SB_S2W_avg = []
S_SB_S2E_avg = []
S_SB_S1E_avg = []
S_SB_S1W_avg = []
T_SB_S2W_avg = []
T_SB_S2E_avg = []
T_SB_S1E_avg = []
T_SB_S1W_avg = []
TP_SB_S2W_avg = []
TP_SB_S2E_avg = []
TP_SB_S1E_avg = []
TP_SB_S1W_avg = []

cursor.execute('SELECT timestamp, s_sb_s2w, s_sb_s2e, s_sb_s1e, s_sb_s1w, t_sb_s2w, t_sb_s2e, t_sb_s1e, t_sb_s1w, tp_sb_s2w, tp_sb_s2e, tp_sb_s1e, tp_sb_s1w FROM averaged')
sb_avg_data = cursor.fetchall()

for row in sb_avg_data:
    DatesSB_avg.append(row[0])
    S_SB_S2W_avg.append(row[1])
    S_SB_S2E_avg.append(row[2])
    S_SB_S1E_avg.append(row[3])
    S_SB_S1W_avg.append(row[4])
    T_SB_S2W_avg.append(row[5])
    T_SB_S2E_avg.append(row[6])
    T_SB_S1E_avg.append(row[7])
    T_SB_S1W_avg.append(row[8])
    TP_SB_S2W_avg.append(row[9])
    TP_SB_S2E_avg.append(row[10])
    TP_SB_S1E_avg.append(row[11])
    TP_SB_S1W_avg.append(row[12])

#print(time.time() - start)

#print('getting NB data')
start = time.time()

DatesNB = []
S_NB_S2W = []
S_NB_S2E = []
S_NB_S1E = []
S_NB_S1W = []
T_NB_S2W = []
T_NB_S2E = []
T_NB_S1E = []
T_NB_S1W = []
TP_NB_S2W = []
TP_NB_S2E = []
TP_NB_S1E = []
TP_NB_S1W = []

cursor.execute('SELECT timestamp, s_nb_s2w, s_nb_s2e, s_nb_s1e, s_nb_s1w, t_nb_s2w, t_nb_s2e, t_nb_s1e, t_nb_s1w, tp_nb_s2w, tp_nb_s2e, tp_nb_s1e, tp_nb_s1w FROM unaveraged')
nb_data = cursor.fetchall()

for row in nb_data:
    DatesNB.append(row[0])
    S_NB_S2W.append(row[1])
    S_NB_S2E.append(row[2])
    S_NB_S1E.append(row[3])
    S_NB_S1W.append(row[4])
    T_NB_S2W.append(row[5])
    T_NB_S2E.append(row[6])
    T_NB_S1E.append(row[7])
    T_NB_S1W.append(row[8])
    TP_NB_S2W.append(row[9])
    TP_NB_S2E.append(row[10])
    TP_NB_S1E.append(row[11])
    TP_NB_S1W.append(row[12])

#print(time.time() - start)

#print('getting SB data')
start = time.time()

DatesSB = []
S_SB_S2W = []
S_SB_S2E = []
S_SB_S1E = []
S_SB_S1W = []
T_SB_S2W = []
T_SB_S2E = []
T_SB_S1E = []
T_SB_S1W = []
TP_SB_S2W = []
TP_SB_S2E = []
TP_SB_S1E = []
TP_SB_S1W = []

cursor.execute('SELECT timestamp, s_sb_s2w, s_sb_s2e, s_sb_s1e, s_sb_s1w, t_sb_s2w, t_sb_s2e, t_sb_s1e, t_sb_s1w, tp_sb_s2w, tp_sb_s2e, tp_sb_s1e, tp_sb_s1w FROM unaveraged')
sb_data = cursor.fetchall()

for row in sb_data:
    DatesSB.append(row[0])
    S_SB_S2W.append(row[1])
    S_SB_S2E.append(row[2])
    S_SB_S1E.append(row[3])
    S_SB_S1W.append(row[4])
    T_SB_S2W.append(row[5])
    T_SB_S2E.append(row[6])
    T_SB_S1E.append(row[7])
    T_SB_S1W.append(row[8])
    TP_SB_S2W.append(row[9])
    TP_SB_S2E.append(row[10])
    TP_SB_S1E.append(row[11])
    TP_SB_S1W.append(row[12])

#print(time.time() - start)

#print('getting NB_Wav data')
start = time.time()


start = time.time()

FBG_T_NB_S2W = []
FBG_S_NB_S2W = []
FBG_T_NB_S2E = []
FBG_S_NB_S2E = []
FBG_T_NB_S1E = []
FBG_S_NB_S1E = []
FBG_T_NB_S1W = []
FBG_S_NB_S1W = []
FBG_TP_NB_S2W = []
FBG_TP_NB_S2E = []
FBG_TP_NB_S1E = []
FBG_TP_NB_S1W = []

cursor.execute("SELECT s_nb_s2w, s_nb_s2e, s_nb_s1e, s_nb_s1w, t_nb_s2w, t_nb_s2e, t_nb_s1e, t_nb_s1w, tp_nb_s2w, tp_nb_s2e, tp_nb_s1e, tp_nb_s1w FROM wavelengths where Timestamp > '2017-05-02' and Timestamp < '2017-05-04'")
nb_wav_data = cursor.fetchall()
#print(nb_wav_data)

#DatesNB_wav.append(row[0])
for row in nb_wav_data:
    FBG_T_NB_S2W.append(row[0])
    FBG_S_NB_S2W.append(row[1])
    FBG_T_NB_S2E.append(row[2])
    FBG_S_NB_S2E.append(row[3])
    FBG_T_NB_S1E.append(row[4])
    FBG_S_NB_S1E.append(row[5])
    FBG_T_NB_S1W.append(row[6])
    FBG_S_NB_S1W.append(row[7])
    FBG_TP_NB_S2W.append(row[8])
    FBG_TP_NB_S2E.append(row[9])
    FBG_TP_NB_S1E.append(row[10])
    FBG_TP_NB_S1W.append(row[11])

#print(time.time() - start)

FBG_T_NB_S2W_avg = sum(FBG_T_NB_S2W) / len(FBG_T_NB_S2W)
FBG_S_NB_S2W_avg = sum(FBG_S_NB_S2W) / len(FBG_S_NB_S2W)
FBG_T_NB_S2E_avg = sum(FBG_T_NB_S2E) / len(FBG_T_NB_S2E)
FBG_S_NB_S2E_avg = sum(FBG_S_NB_S2E) / len(FBG_S_NB_S2E)
FBG_T_NB_S1E_avg = sum(FBG_T_NB_S1E) / len(FBG_T_NB_S1E)
FBG_S_NB_S1E_avg = sum(FBG_S_NB_S1E) / len(FBG_S_NB_S1E)
FBG_T_NB_S1W_avg = sum(FBG_T_NB_S1W) / len(FBG_T_NB_S1W)
FBG_S_NB_S1W_avg = sum(FBG_S_NB_S1W) / len(FBG_S_NB_S1W)
FBG_TP_NB_S2W_avg = sum(FBG_TP_NB_S2W) / len(FBG_TP_NB_S2W)
FBG_TP_NB_S2E_avg = sum(FBG_TP_NB_S2E) / len(FBG_TP_NB_S2E)
FBG_TP_NB_S1E_avg = sum(FBG_TP_NB_S1E) / len(FBG_TP_NB_S1E)
FBG_TP_NB_S1W_avg = sum(FBG_TP_NB_S1W) / len(FBG_TP_NB_S1W)

FBG_T_NB_S2W_max = max(FBG_T_NB_S2W)
FBG_S_NB_S2W_max = max(FBG_S_NB_S2W)
FBG_T_NB_S2E_max = max(FBG_T_NB_S2E)
FBG_S_NB_S2E_max = max(FBG_S_NB_S2E)
FBG_T_NB_S1E_max = max(FBG_T_NB_S1E)
FBG_S_NB_S1E_max = max(FBG_S_NB_S1E)
FBG_T_NB_S1W_max = max(FBG_T_NB_S1W)
FBG_S_NB_S1W_max = max(FBG_S_NB_S1W)
FBG_TP_NB_S2W_max = max(FBG_TP_NB_S2W)
FBG_TP_NB_S2E_max = max(FBG_TP_NB_S2E)
FBG_TP_NB_S1E_max = max(FBG_TP_NB_S1E)
FBG_TP_NB_S1W_max = max(FBG_TP_NB_S1W)

FBG_T_NB_S2W_min = min(FBG_T_NB_S2W)
FBG_S_NB_S2W_min = min(FBG_S_NB_S2W)
FBG_T_NB_S2E_min = min(FBG_T_NB_S2E)
FBG_S_NB_S2E_min = min(FBG_S_NB_S2E)
FBG_T_NB_S1E_min = min(FBG_T_NB_S1E)
FBG_S_NB_S1E_min = min(FBG_S_NB_S1E)
FBG_T_NB_S1W_min = min(FBG_T_NB_S1W)
FBG_S_NB_S1W_min = min(FBG_S_NB_S1W)
FBG_TP_NB_S2W_min = min(FBG_TP_NB_S2W)
FBG_TP_NB_S2E_min = min(FBG_TP_NB_S2E)
FBG_TP_NB_S1E_min = min(FBG_TP_NB_S1E)
FBG_TP_NB_S1W_min = min(FBG_TP_NB_S1W)

wavelengthsNB_avg = (FBG_T_NB_S2W_avg, FBG_S_NB_S2W_avg, FBG_T_NB_S2E_avg,
                     FBG_S_NB_S2E_avg, FBG_T_NB_S1E_avg, FBG_S_NB_S1E_avg,
                     FBG_T_NB_S1W_avg, FBG_S_NB_S1W_avg, FBG_TP_NB_S2W_avg,
                     FBG_TP_NB_S2E_avg, FBG_TP_NB_S1E_avg, FBG_TP_NB_S1W_avg)

wavelengthsNB_max = (FBG_T_NB_S2W_max, FBG_S_NB_S2W_max, FBG_T_NB_S2E_max,
                     FBG_S_NB_S2E_max, FBG_T_NB_S1E_max, FBG_S_NB_S1E_max,
                     FBG_T_NB_S1W_max, FBG_S_NB_S1W_max, FBG_TP_NB_S2W_max,
                     FBG_TP_NB_S2E_max, FBG_TP_NB_S1E_max, FBG_TP_NB_S1W_max)

wavelengthsNB_min = (FBG_T_NB_S2W_min, FBG_S_NB_S2W_min, FBG_T_NB_S2E_min,
                     FBG_S_NB_S2E_min, FBG_T_NB_S1E_min, FBG_S_NB_S1E_min,
                     FBG_T_NB_S1W_min, FBG_S_NB_S1W_min, FBG_TP_NB_S2W_min,
                     FBG_TP_NB_S2E_min, FBG_TP_NB_S1E_min, FBG_TP_NB_S1W_min)

#print('getting SB_Wav data')
start = time.time()


start = time.time()

FBG_T_SB_S2W = []
FBG_S_SB_S2W = []
FBG_T_SB_S2E = []
FBG_S_SB_S2E = []
FBG_T_SB_S1E = []
FBG_S_SB_S1E = []
FBG_T_SB_S1W = []
FBG_S_SB_S1W = []
FBG_TP_SB_S2W = []
FBG_TP_SB_S2E = []
FBG_TP_SB_S1E = []
FBG_TP_SB_S1W = []

cursor.execute("SELECT s_sb_s2w, s_sb_s2e, s_sb_s1e, s_sb_s1w, t_sb_s2w, t_sb_s2e, t_sb_s1e, t_sb_s1w, tp_sb_s2w, tp_sb_s2e, tp_sb_s1e, tp_sb_s1w FROM wavelengths where Timestamp > '2017-05-02' and Timestamp < '2017-05-04'")
sb_wav_data = cursor.fetchall()
#print(sb_wav_data)

#DatesNB_wav.append(row[0])
for row in nb_wav_data:
    FBG_T_SB_S2W.append(row[0])
    FBG_S_SB_S2W.append(row[1])
    FBG_T_SB_S2E.append(row[2])
    FBG_S_SB_S2E.append(row[3])
    FBG_T_SB_S1E.append(row[4])
    FBG_S_SB_S1E.append(row[5])
    FBG_T_SB_S1W.append(row[6])
    FBG_S_SB_S1W.append(row[7])
    FBG_TP_SB_S2W.append(row[8])
    FBG_TP_SB_S2E.append(row[9])
    FBG_TP_SB_S1E.append(row[10])
    FBG_TP_SB_S1W.append(row[11])

#print(time.time() - start)

FBG_T_SB_S2W_avg = sum(FBG_T_SB_S2W) / len(FBG_T_SB_S2W)
FBG_S_SB_S2W_avg = sum(FBG_S_SB_S2W) / len(FBG_S_SB_S2W)
FBG_T_SB_S2E_avg = sum(FBG_T_SB_S2E) / len(FBG_T_SB_S2E)
FBG_S_SB_S2E_avg = sum(FBG_S_SB_S2E) / len(FBG_S_SB_S2E)
FBG_T_SB_S1E_avg = sum(FBG_T_SB_S1E) / len(FBG_T_SB_S1E)
FBG_S_SB_S1E_avg = sum(FBG_S_SB_S1E) / len(FBG_S_SB_S1E)
FBG_T_SB_S1W_avg = sum(FBG_T_SB_S1W) / len(FBG_T_SB_S1W)
FBG_S_SB_S1W_avg = sum(FBG_S_SB_S1W) / len(FBG_S_SB_S1W)
FBG_TP_SB_S2W_avg = sum(FBG_TP_SB_S2W) / len(FBG_TP_SB_S2W)
FBG_TP_SB_S2E_avg = sum(FBG_TP_SB_S2E) / len(FBG_TP_SB_S2E)
FBG_TP_SB_S1E_avg = sum(FBG_TP_SB_S1E) / len(FBG_TP_SB_S1E)
FBG_TP_SB_S1W_avg = sum(FBG_TP_SB_S1W) / len(FBG_TP_SB_S1W)

FBG_T_SB_S2W_max = max(FBG_T_SB_S2W)
FBG_S_SB_S2W_max = max(FBG_S_SB_S2W)
FBG_T_SB_S2E_max = max(FBG_T_SB_S2E)
FBG_S_SB_S2E_max = max(FBG_S_SB_S2E)
FBG_T_SB_S1E_max = max(FBG_T_SB_S1E)
FBG_S_SB_S1E_max = max(FBG_S_SB_S1E)
FBG_T_SB_S1W_max = max(FBG_T_SB_S1W)
FBG_S_SB_S1W_max = max(FBG_S_SB_S1W)
FBG_TP_SB_S2W_max = max(FBG_TP_SB_S2W)
FBG_TP_SB_S2E_max = max(FBG_TP_SB_S2E)
FBG_TP_SB_S1E_max = max(FBG_TP_SB_S1E)
FBG_TP_SB_S1W_max = max(FBG_TP_SB_S1W)

FBG_T_SB_S2W_min = min(FBG_T_SB_S2W)
FBG_S_SB_S2W_min = min(FBG_S_SB_S2W)
FBG_T_SB_S2E_min = min(FBG_T_SB_S2E)
FBG_S_SB_S2E_min = min(FBG_S_SB_S2E)
FBG_T_SB_S1E_min = min(FBG_T_SB_S1E)
FBG_S_SB_S1E_min = min(FBG_S_SB_S1E)
FBG_T_SB_S1W_min = min(FBG_T_SB_S1W)
FBG_S_SB_S1W_min = min(FBG_S_SB_S1W)
FBG_TP_SB_S2W_min = min(FBG_TP_SB_S2W)
FBG_TP_SB_S2E_min = min(FBG_TP_SB_S2E)
FBG_TP_SB_S1E_min = min(FBG_TP_SB_S1E)
FBG_TP_SB_S1W_min = min(FBG_TP_SB_S1W)

wavelengthsSB_avg = (FBG_T_SB_S2W_avg, FBG_S_SB_S2W_avg, FBG_T_SB_S2E_avg,
                     FBG_S_SB_S2E_avg, FBG_T_SB_S1E_avg, FBG_S_SB_S1E_avg,
                     FBG_T_SB_S1W_avg, FBG_S_SB_S1W_avg, FBG_TP_SB_S2W_avg,
                     FBG_TP_SB_S2E_avg, FBG_TP_SB_S1E_avg, FBG_TP_SB_S1W_avg)

wavelengthsSB_max = (FBG_T_SB_S2W_max, FBG_S_SB_S2W_max, FBG_T_SB_S2E_max,
                     FBG_S_SB_S2E_max, FBG_T_SB_S1E_max, FBG_S_SB_S1E_max,
                     FBG_T_SB_S1W_max, FBG_S_SB_S1W_max, FBG_TP_SB_S2W_max,
                     FBG_TP_SB_S2E_max, FBG_TP_SB_S1E_max, FBG_TP_SB_S1W_max)

wavelengthsSB_min = (FBG_T_SB_S2W_min, FBG_S_SB_S2W_min, FBG_T_SB_S2E_min,
                     FBG_S_SB_S2E_min, FBG_T_SB_S1E_min, FBG_S_SB_S1E_min,
                     FBG_T_SB_S1W_min, FBG_S_SB_S1W_min, FBG_TP_SB_S2W_min,
                     FBG_TP_SB_S2E_min, FBG_TP_SB_S1E_min, FBG_TP_SB_S1W_min)


#print('getting NB power data')
start = time.time()


cursor.execute('SELECT timestamp, T_NB_S2W, S_NB_S2W, T_NB_S2E, S_NB_S2E, T_NB_S1E, S_NB_S1E, T_NB_S1W, S_NB_S1W, TP_NB_S2W, TP_NB_S2E, TP_NB_S1E, TP_NB_S1W FROM power order by Timestamp desc limit 1')
nb_power_data = cursor.fetchall()

#DatesNB_db.append(nb_power_data[0][0])
FBG_T_NB_S2W_db = abs(nb_power_data[0][1])
FBG_S_NB_S2W_db = abs(nb_power_data[0][2])
FBG_T_NB_S2E_db = abs(nb_power_data[0][3])
FBG_S_NB_S2E_db = abs(nb_power_data[0][4])
FBG_T_NB_S1E_db = abs(nb_power_data[0][5])
FBG_S_NB_S1E_db = abs(nb_power_data[0][6])
FBG_T_NB_S1W_db = abs(nb_power_data[0][7])
FBG_S_NB_S1W_db = abs(nb_power_data[0][8])
FBG_TP_NB_S2W_db = abs(nb_power_data[0][9])
FBG_TP_NB_S2E_db = abs(nb_power_data[0][10])
FBG_TP_NB_S1E_db = abs(nb_power_data[0][11])
FBG_TP_NB_S1W_db = abs(nb_power_data[0][12])

#print(time.time() - start)
powerLevelsNB = (FBG_T_NB_S2W_db, FBG_S_NB_S2W_db, FBG_T_NB_S2E_db,
               FBG_S_NB_S2E_db, FBG_T_NB_S1E_db, FBG_S_NB_S1E_db,
               FBG_T_NB_S1W_db, FBG_S_NB_S1W_db, FBG_TP_NB_S2W_db,
               FBG_TP_NB_S2E_db, FBG_TP_NB_S1E_db, FBG_TP_NB_S1W_db)


#print('getting SB_power data')
start = time.time()

cursor.execute('SELECT timestamp, s_sb_s2w, s_sb_s2e, s_sb_s1e, s_sb_s1w, t_sb_s2w, t_sb_s2e, t_sb_s1e, t_sb_s1w, tp_sb_s2w, tp_sb_s2e, tp_sb_s1e, tp_sb_s1w FROM power order by Timestamp desc limit 1')
sb_power_data = cursor.fetchall()

#DatesSB_db = sb_power_data[0][0])
FBG_T_SB_S2W_db = abs(sb_power_data[0][1])
FBG_S_SB_S2W_db = abs(sb_power_data[0][2])
FBG_T_SB_S2E_db = abs(sb_power_data[0][3])
FBG_S_SB_S2E_db = abs(sb_power_data[0][4])
FBG_T_SB_S1E_db = abs(sb_power_data[0][5])
FBG_S_SB_S1E_db = abs(sb_power_data[0][6])
FBG_T_SB_S1W_db = abs(sb_power_data[0][7])
FBG_S_SB_S1W_db = abs(sb_power_data[0][8])
FBG_TP_SB_S2W_db = abs(sb_power_data[0][9])
FBG_TP_SB_S2E_db = abs(sb_power_data[0][10])
FBG_TP_SB_S1E_db = abs(sb_power_data[0][11])
FBG_TP_SB_S1W_db = abs(sb_power_data[0][12])

#print(time.time() - start)
powerLevelsSB = (FBG_T_SB_S2W_db, FBG_S_SB_S2W_db, FBG_T_SB_S2E_db,
               FBG_S_SB_S2E_db, FBG_T_SB_S1E_db, FBG_S_SB_S1E_db,
               FBG_T_SB_S1W_db, FBG_S_SB_S1W_db, FBG_TP_SB_S2W_db,
               FBG_TP_SB_S2E_db, FBG_TP_SB_S1E_db, FBG_TP_SB_S1W_db)


# NB strain
rc('mathtext', default='regular')

fig = plt.figure(figsize=(5, 4))

ax1 = fig.add_subplot(111)


plt.subplots_adjust(left=0.112, top=0.9, bottom=0.198, right=0.84)

xfmt = md.DateFormatter('%Y-%m-%d')
ax1.xaxis.set_major_formatter(xfmt)

ax1.set_title('North Bound Strain')

lns1 = ax1.plot(md.date2num(DatesNB), S_NB_S2W, '-', label="S_NB_S2W")
lns2 = ax1.plot(md.date2num(DatesNB), S_NB_S2E, '-', label="S_NB_S2E")
lns3 = ax1.plot(md.date2num(DatesNB), S_NB_S1E, '-', label="S_NB_S1E")
lns4 = ax1.plot(md.date2num(DatesNB), S_NB_S1W, '-', label="S_NB_S1W")

lns = lns1+lns2+lns3+lns4


nticksX = 10
ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticksX))

nticksY = 10
ax1.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticksX))

ax1.set_ylabel('Microstrain (µε)')
#ax2.set_ylabel('Temperature (°C)')

labs = [l.get_label() for l in lns]

fontP = FontProperties()
fontP.set_size('small')

legend = ax1.legend(frameon=True)
for legend_handle in legend.legendHandles:
    legend_handle._legmarker.set_markersize(6)
    
leg = ax1.legend(lns, labs, title="Legend", bbox_to_anchor=(1.01, 1), loc='upper left', prop=fontP, fancybox=True, shadow=True)
lined = {}
for legline, origline in zip(leg.get_lines(), lns):
    legline.set_picker(True)
    lined[legline] = origline

def on_pick(event):
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()


ax1.grid(color='w', linestyle='solid')
ax1.set_facecolor('#E6E6E6')
ax1.set_axisbelow(True)


# specify the master            
canvas = FigureCanvasTkAgg(fig, master=canvas1)
fig.canvas.mpl_connect('pick_event', on_pick)
canvas.draw()

ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha='right')

canvas.get_tk_widget().pack(fill="both", expand=True)


# navigation toolbar
#toolbar = NavigationToolbar2Tk(canvas, canvas1)
#toolbar.pack(side="top")

# Export csv
#btn_exportInDepth = tk.Button(inner_frameInDepth, text="Export CSV", command=lambda: export(table))
#btn_exportInDepth.pack(fill="both", side="top")

#data = pd.DataFrame()
##print(dataFrames[table])


#SB Strain
rc('mathtext', default='regular')

fig = plt.figure(figsize=(5, 4))

ax1 = fig.add_subplot(111)


plt.subplots_adjust(left=0.112, top=0.9, bottom=0.198, right=0.84)

xfmt = md.DateFormatter('%Y-%m-%d')
ax1.xaxis.set_major_formatter(xfmt)

ax1.set_title('South Bound Strain')

lns1 = ax1.plot(md.date2num(DatesSB), S_SB_S2W, '-', label="S_SB_S2W")
lns2 = ax1.plot(md.date2num(DatesSB), S_SB_S2E, '-', label="S_SB_S2E")
lns3 = ax1.plot(md.date2num(DatesSB), S_SB_S1E, '-', label="S_SB_S1E")
lns4 = ax1.plot(md.date2num(DatesSB), S_SB_S1W, '-', label="S_SB_S1W")

lns = lns1+lns2+lns3+lns4


nticksX = 10
ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticksX))

nticksY = 10
ax1.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticksX))

ax1.set_ylabel('Microstrain (µε)')
#ax2.set_ylabel('Temperature (°C)')

labs = [l.get_label() for l in lns]

fontP = FontProperties()
fontP.set_size('small')

legend = ax1.legend(frameon=True)
for legend_handle in legend.legendHandles:
    legend_handle._legmarker.set_markersize(6)
    
leg = ax1.legend(lns, labs, title="Legend", bbox_to_anchor=(1.01, 1), loc='upper left', prop=fontP, fancybox=True, shadow=True)
lined = {}
for legline, origline in zip(leg.get_lines(), lns):
    legline.set_picker(True)
    lined[legline] = origline



ax1.grid(color='w', linestyle='solid')
ax1.set_facecolor('#E6E6E6')
ax1.set_axisbelow(True)


# specify the master            
canvas = FigureCanvasTkAgg(fig, master=canvas2)
fig.canvas.mpl_connect('pick_event', on_pick)
canvas.draw()

ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha='right')

canvas.get_tk_widget().pack(fill="both", expand=True)


# NB Health
fig = plt.figure(figsize=(5, 4))

ax = fig.add_subplot(111)

plt.subplots_adjust(left=0.1, bottom=0.195)

width_avg = 0.35
width_max = 0.1
ax.bar(wavelengthsNB_avg, powerLevelsNB, width_avg, align='center', color='r')
ax.bar(wavelengthsNB_max, powerLevelsNB, width_max, align='center', color='b')
ax.bar(wavelengthsNB_min, powerLevelsNB, width_max, align='center', color='b')
ax.set_xlabel('Wavelengths (nm)')
ax.set_ylabel('Power (db)')
ax.set_xticks(wavelengthsNB_avg)
ax.set_xticks(wavelengthsNB_max)
ax.set_xticks(wavelengthsNB_min)
ax.set_yticks(np.arange(0, 61, 10))
ax.set_title('NB Wavelengths and Power')

canvas = FigureCanvasTkAgg(fig, master=canvas3)
canvas.draw()

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')

canvas.get_tk_widget().pack(fill="both", expand=True)

# navigation toolbar
#toolbar = NavigationToolbar2Tk(canvas, canvas3)
#toolbar.pack(side="top")


# SB Health
# NB Health
fig = plt.figure(figsize=(5, 4))

ax = fig.add_subplot(111)

plt.subplots_adjust(left=0.1, bottom=0.195)

width_avg = 0.35
width_max = 0.1
ax.bar(wavelengthsSB_avg, powerLevelsSB, width_avg, align='center', color='r')
ax.bar(wavelengthsSB_max, powerLevelsSB, width_max, align='center', color='b')
ax.bar(wavelengthsSB_min, powerLevelsSB, width_max, align='center', color='b')
ax.set_xlabel('Wavelengths (nm)')
ax.set_ylabel('Power (db)')
ax.set_xticks(wavelengthsSB_avg)
ax.set_xticks(wavelengthsSB_max)
ax.set_xticks(wavelengthsSB_min)
ax.set_yticks(np.arange(0, 61, 10))
ax.set_title('SB Wavelengths and Power')

canvas = FigureCanvasTkAgg(fig, master=canvas4)
canvas.draw()

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')

canvas.get_tk_widget().pack(fill="both", expand=True)


# Place in Grid
frm_top.grid(row=0, columnspan=2, sticky="ew")
frm_right.grid(row=0, column = 2, rowspan=3, sticky="ns")
frm_left.grid(row=0, column=0, rowspan=3, sticky="ns")
frm_bottom.grid(row=2, column=0, columnspan=3, sticky="ew")
canvasFrame.grid(row=1, column=1, sticky="nsew")

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()