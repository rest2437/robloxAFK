import customtkinter as ctk
from PIL import Image
import os
import autoit
import time
import pywinauto
import threading
import pyautogui
import subprocess
import random


# real time data (no storage)
startAFK = bool
stopAFK = bool
start = bool
stop = bool
hcOnOrOff = int
robloxApp = pywinauto.Application(backend='uia')


############################## AFK MOUSE POINTS ##############################
#Game 1
mouse_entry_1_x = 0 
mouse_entry_1_y = 0 
#Game 2
mouse_entry_2_x = 0 
mouse_entry_2_y = 0 
#Game 3
mouse_entry_3_x = 0 
mouse_entry_3_y = 0 
#Game 4
mouse_entry_4_x = 0 
mouse_entry_4_y = 0 
#stopButton
stopButton_x = 0
stopButton_y = 0
############################## Global variables ##############################
keyPress = int
# Macro
macroState = int    
#Game1
game1State = int
#Game2
game2State = int
#Game3
game3State = int
#Game4
game4State = int
#Ultimate 1
ultimate1State = int
#Ultimate 2
ultimate2State = int
#Ultimate 3
ultimate3State = int
#Ultimate 4
ultimate4State = int


############################## testing start ##############################
############################## testing start ##############################
############################## testing start ##############################

# TOGGLE_KEY = KeyCode(char='1')
# clicking = False

# mouse = Controller()

# def clicker():
#     while True:
#         if clicking and macroState == 1:
#             mouse.click(Button.left,1)
#         time.sleep(0.001)

# def toggle_event(key):
#     if key == TOGGLE_KEY and macroState == 1:
#         global clicking
#         clicking = not clicking

# listener= Listener(on_press=toggle_event)

############################## testing end ##############################
############################## testing end ##############################
############################## testing end ##############################
############################## testing end ##############################





### Project Title Frame DONE###
class ProjectTitleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # title label
        self.label2 = ctk.CTkLabel(
            self, text="OLDD Clan [BETA]", font=ctk.CTkFont(size=25, weight='bold'))
        self.label2.pack(padx=10, pady=(20, 1))
        # version
        self.label3 = ctk.CTkLabel(
            self, text="By RobDaDev", text_color="#545f63", font=ctk.CTkFont(size=15, weight='bold'))
        self.label3.pack(pady=(1, 20))

### Colsole Frame DONE ###
class ConsoleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global console_updates
        self.label2 = ctk.CTkLabel(
            self, text='Console Updates', font=ctk.CTkFont(size=20, weight='bold'))
        self.label2.pack(padx=10, pady=(20, 1))

        self.label3 = ctk.CTkLabel(
            self, text='No Updates', font=ctk.CTkFont(size=12, weight='bold'))
        self.label3.pack(pady=(1, 20))
        self.x = "zero"

### Main Frame - IN PROGRESS ###
class MainFrame(ctk.CTkFrame):
    # TODO
    # buttons for start/stop anti afk
    # console scrollable window
    # start/save for mouse configs
    # toggles for how many games or just leave blank for no use

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
######################### PARENT FRAMES #########################
        self.parent_frame = ctk.CTkScrollableFrame(self,fg_color = "#333333")
        self.parent_frame.pack(ipadx = 50, ipady = 10, pady = 10, padx=10)

######################### stop button #########################
        self.sb_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
        self.sb_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.sb_frame.grid_columnconfigure(0, minsize=100)
        self.sb_frame.grid_columnconfigure(1, minsize=100)
        self.sb_frame.grid_columnconfigure(2, minsize=100)
        
        self.sb_label = ctk.CTkLabel(
            self.sb_frame, text='Hover mouse over stop button', font=ctk.CTkFont(size=12,weight='bold'))
        self.sb_label.grid(column=0, row=3, padx=30, columnspan=3,
                         pady=(0, 0))

        self.sb_label = ctk.CTkLabel(
            self.sb_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
        self.sb_label.grid(column=0, row=4, padx=5,
                         pady=(0, 10))
        
        self.start_mouse_location_sb = ctk.CTkButton(
            self.sb_frame, width=75, height=20, text='Start', command=self.startMouseLocationsb)
        self.start_mouse_location_sb.grid(
            column=1, row=4, padx=5, pady=(0, 10))
        
        self.start_mouse_location_sb = ctk.CTkButton(
            self.sb_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntrysb_x(), self.mouseEntrysb_y()])
        self.start_mouse_location_sb.grid(
            column=2, row=4, padx=5, pady=(0, 10))
        
######################### ENTRY 1 #########################
        self.entry_1_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
        self.entry_1_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.entry_1_frame.grid_columnconfigure(0, minsize=100)
        self.entry_1_frame.grid_columnconfigure(1, minsize=100)
        self.entry_1_frame.grid_columnconfigure(2, minsize=100)

        self.game1_switch_var = ctk.IntVar(value=0)
        self.game1_switch = ctk.CTkSwitch(
            self.entry_1_frame, text='Game 1', command=self.game1SwitchValue, variable=self.game1_switch_var, onvalue=1, offvalue=0)
        self.game1_switch.grid(column=0, row=1, padx=30, columnspan=3,
                         pady=(10, 0))
        
        self.ultimate1_var = ctk.IntVar(value=0)
        self.ultimate1_switch = ctk.CTkSwitch(
            self.entry_1_frame, text='Ultimate', command=self.ultimate1SwitchValue, variable=self.ultimate1_var, onvalue=1, offvalue=0)
        self.ultimate1_switch.grid(columnspan=3, row=2, padx=5, pady=(0, 10))
        
        self.label1 = ctk.CTkLabel(
            self.entry_1_frame, text='Press start and point\nmouse at Game 1 ', font=ctk.CTkFont(size=12,weight='bold'))
        self.label1.grid(column=0, row=3, padx=30, columnspan=3,
                         pady=(0, 0))

        self.label1 = ctk.CTkLabel(
            self.entry_1_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
        self.label1.grid(column=0, row=4, padx=5,
                         pady=(0, 10))
        
        self.start_mouse_location_1 = ctk.CTkButton(
            self.entry_1_frame, width=75, height=20, text='Start', command=self.startMouseLocation1)
        self.start_mouse_location_1.grid(
            column=1, row=4, padx=5, pady=(0, 10))
        
        self.save_mouse_location_1 = ctk.CTkButton(
            self.entry_1_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry1_x(), self.mouseEntry1_y()])
        self.save_mouse_location_1.grid(
            column=2, row=4, padx=5, pady=(0, 10))
        
######################### ENTRY 2 #########################
        self.entry_2_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
        self.entry_2_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.entry_2_frame.grid_columnconfigure(0, minsize=100)
        self.entry_2_frame.grid_columnconfigure(1, minsize=100)
        self.entry_2_frame.grid_columnconfigure(2, minsize=100)

        self.game2_switch_var = ctk.IntVar(value=0)
        self.game2_switch = ctk.CTkSwitch(
            self.entry_2_frame, text='Game 2', command=self.game2SwitchValue, variable=self.game2_switch_var, onvalue=1, offvalue=0)
        self.game2_switch.grid(column=0, row=1, padx=30, columnspan=3,
                         pady=(10, 0))
        
        self.ultimate2_var = ctk.IntVar(value=0)
        self.ultimate2_switch = ctk.CTkSwitch(
            self.entry_2_frame, text='Ultimate', command=self.ultimate2SwitchValue, variable=self.ultimate2_var, onvalue=1, offvalue=0)
        self.ultimate2_switch.grid(columnspan=3, row=2, padx=5, pady=(0, 10))
        
        self.label2 = ctk.CTkLabel(
            self.entry_2_frame, text='Press start and point\nmouse at Game 2 ', font=ctk.CTkFont(size=12,weight='bold'))
        self.label2.grid(column=0, row=3, padx=30, columnspan=3,
                         pady=(0, 0))

        self.label2 = ctk.CTkLabel(
            self.entry_2_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
        self.label2.grid(column=0, row=4, padx=5,
                         pady=(0, 10))
        
        self.start_mouse_location_2 = ctk.CTkButton(
            self.entry_2_frame, width=75, height=20, text='Start', command=self.startMouseLocation2)
        self.start_mouse_location_2.grid(
            column=1, row=4, padx=5, pady=(0, 10))
        
        self.save_mouse_location_2 = ctk.CTkButton(
            self.entry_2_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry2_x(), self.mouseEntry2_y()])
        self.save_mouse_location_2.grid(
            column=2, row=4, padx=5, pady=(0, 10))
        
        
        

        
# ######################### ENTRY 2 #########################
#         self.entry_2_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
#         self.entry_2_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
#         self.entry_2_frame.grid_columnconfigure(0, minsize=100)
#         self.entry_2_frame.grid_columnconfigure(1, minsize=100)
#         self.entry_2_frame.grid_columnconfigure(2, minsize=100)
#         self.label2 = ctk.CTkLabel(
#             self.entry_2_frame, text='Game 2', font=ctk.CTkFont(size=12,weight='bold'))
#         self.label2.grid(column=0, row=1, padx=30, columnspan=3,
#                          pady=(0, 0))
#         self.label2 = ctk.CTkLabel(
#             self.entry_2_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
#         self.label2.grid(column=0, row=2, padx=5,
#                          pady=(0, 10))
#         self.start_mouse_location_2 = ctk.CTkButton(
#             self.entry_2_frame, width=75, height=20, text='Start', command=self.startMouseLocation2)
#         self.start_mouse_location_2.grid(
#             column=1, row=2, padx=5, pady=(0, 10))
#         self.save_mouse_location_2 = ctk.CTkButton(
#             self.entry_2_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry2_x(), self.mouseEntry2_y()])
#         self.save_mouse_location_2.grid(
#             column=2, row=2, padx=5, pady=(0, 10))

# ######################### ENTRY 3 #########################
        self.entry_3_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
        self.entry_3_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.entry_3_frame.grid_columnconfigure(0, minsize=100)
        self.entry_3_frame.grid_columnconfigure(1, minsize=100)
        self.entry_3_frame.grid_columnconfigure(2, minsize=100)

        self.game3_switch_var = ctk.IntVar(value=0)
        self.game3_switch = ctk.CTkSwitch(
            self.entry_3_frame, text='Game 3', command=self.game3SwitchValue, variable=self.game3_switch_var, onvalue=1, offvalue=0)
        self.game3_switch.grid(column=0, row=1, padx=30, columnspan=3,
                         pady=(10, 0))
        
        self.ultimate3_var = ctk.IntVar(value=0)
        self.ultimate3_switch = ctk.CTkSwitch(
            self.entry_3_frame, text='Ultimate', command=self.ultimate3SwitchValue, variable=self.ultimate3_var, onvalue=1, offvalue=0)
        self.ultimate3_switch.grid(columnspan=3, row=2, padx=5, pady=(0, 10))
        
        self.label3 = ctk.CTkLabel(
            self.entry_3_frame, text='Press start and point\nmouse at Game 3 ', font=ctk.CTkFont(size=12,weight='bold'))
        self.label3.grid(column=0, row=3, padx=30, columnspan=3,
                         pady=(0, 0))

        self.label3 = ctk.CTkLabel(
            self.entry_3_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
        self.label3.grid(column=0, row=4, padx=5,
                         pady=(0, 10))
        
        self.start_mouse_location_3 = ctk.CTkButton(
            self.entry_3_frame, width=75, height=20, text='Start', command=self.startMouseLocation3)
        self.start_mouse_location_3.grid(
            column=1, row=4, padx=5, pady=(0, 10))
        
        self.save_mouse_location_3 = ctk.CTkButton(
            self.entry_3_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry3_x(), self.mouseEntry3_y()])
        self.save_mouse_location_3.grid(
            column=2, row=4, padx=5, pady=(0, 10))
        
#         self.entry_3_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
#         self.entry_3_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
#         self.entry_3_frame.grid_columnconfigure(0, minsize=100)
#         self.entry_3_frame.grid_columnconfigure(1, minsize=100)
#         self.entry_3_frame.grid_columnconfigure(2, minsize=100)
#         self.label3 = ctk.CTkLabel(
#             self.entry_3_frame, text='Game 3', font=ctk.CTkFont(size=12,weight='bold'))
#         self.label3.grid(column=0, row=1, padx=30, columnspan=3,
#                          pady=(0, 0))
#         self.label3 = ctk.CTkLabel(
#             self.entry_3_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
#         self.label3.grid(column=0, row=2, padx=5,
#                          pady=(0, 10))
#         self.start_mouse_location_3 = ctk.CTkButton(
#             self.entry_3_frame, width=75, height=20, text='Start', command=self.startMouseLocation3)
#         self.start_mouse_location_3.grid(
#             column=1, row=2, padx=5, pady=(0, 10))
#         self.save_mouse_location_3 = ctk.CTkButton(
#             self.entry_3_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry3_x(), self.mouseEntry3_y()])
#         self.save_mouse_location_3.grid(
#             column=2, row=2, padx=5, pady=(0, 10))

# ######################### ENTRY 4 #########################
        self.entry_4_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
        self.entry_4_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.entry_4_frame.grid_columnconfigure(0, minsize=100)
        self.entry_4_frame.grid_columnconfigure(1, minsize=100)
        self.entry_4_frame.grid_columnconfigure(2, minsize=100)

        self.game4_switch_var = ctk.IntVar(value=0)
        self.game4_switch = ctk.CTkSwitch(
            self.entry_4_frame, text='Game 4', command=self.game4SwitchValue, variable=self.game4_switch_var, onvalue=1, offvalue=0)
        self.game4_switch.grid(column=0, row=1, padx=30, columnspan=3,
                         pady=(10, 0))
        
        self.ultimate4_var = ctk.IntVar(value=0)
        self.ultimate4_switch = ctk.CTkSwitch(
            self.entry_4_frame, text='Ultimate', command=self.ultimate4SwitchValue, variable=self.ultimate4_var, onvalue=1, offvalue=0)
        self.ultimate4_switch.grid(columnspan=3, row=2, padx=5, pady=(0, 10))
        
        self.label4 = ctk.CTkLabel(
            self.entry_4_frame, text='Press start and point\nmouse at Game 4 ', font=ctk.CTkFont(size=12,weight='bold'))
        self.label4.grid(column=0, row=3, padx=30, columnspan=3,
                         pady=(0, 0))

        self.label4 = ctk.CTkLabel(
            self.entry_4_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
        self.label4.grid(column=0, row=4, padx=5,
                         pady=(0, 10))
        
        self.start_mouse_location_4 = ctk.CTkButton(
            self.entry_4_frame, width=75, height=20, text='Start', command=self.startMouseLocation4)
        self.start_mouse_location_4.grid(
            column=1, row=4, padx=5, pady=(0, 10))
        
        self.save_mouse_location_4 = ctk.CTkButton(
            self.entry_4_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry4_x(), self.mouseEntry4_y()])
        self.save_mouse_location_4.grid(
            column=2, row=4, padx=5, pady=(0, 10))

#         self.entry_4_frame = ctk.CTkFrame(self.parent_frame,fg_color = "#252525")
#         self.entry_4_frame.pack(ipadx = 5, ipady = 5, padx = 5, pady = 5)
#         self.entry_4_frame.grid_columnconfigure(0, minsize=100)
#         self.entry_4_frame.grid_columnconfigure(1, minsize=100)
#         self.entry_4_frame.grid_columnconfigure(2, minsize=100)
#         self.label4 = ctk.CTkLabel(
#             self.entry_4_frame, text='Game 4', font=ctk.CTkFont(size=12,weight='bold'))
#         self.label4.grid(column=0, row=1, padx=30, columnspan=3,
#                          pady=(0, 0))
#         self.label4 = ctk.CTkLabel(
#             self.entry_4_frame, text='No Value', font=ctk.CTkFont(size=12,weight='bold'))
#         self.label4.grid(column=0, row=2, padx=5,
#                          pady=(0, 10))
#         self.start_mouse_location_5 = ctk.CTkButton(
#             self.entry_4_frame, width=75, height=20, text='Start', command=self.startMouseLocation4)
#         self.start_mouse_location_5.grid(
#             column=1, row=2, padx=5, pady=(0, 10))
#         self.save_mouse_location_4 = ctk.CTkButton(
#             self.entry_4_frame, width=75, height=20, text='Save', command=lambda: [self.mouseEntry4_x(), self.mouseEntry4_y()])
#         self.save_mouse_location_4.grid(
#             column=2, row=2, padx=5, pady=(0, 10))

######################### Start Button #########################
        self.afk_button = ctk.CTkButton(
            self, text="Start Anti AFK", width=200, command=self.start_AFK, fg_color="#1F6AA5", hover_color='#144870')
        self.afk_button.pack(pady=(10, 0))

######################### Account Menu #########################
        self.consoleUpdates = ctk.CTkLabel(
            self, text="No Updates",font=ctk.CTkFont(size=12,weight='bold'))
        self.consoleUpdates.pack(pady=(10, 0))
                

######################### toggle #########################    
    
    def macroSwitchValue(self):
        global macroState
        macroState = self.macro_var.get()
        if self.macro_var.get() == 1:
            self.start_autoclick_inbg()
            print('Macro enabled')
        elif self.macro_var.get() == 0:
            print('Macro disabled')

    def game1SwitchValue(self):
        global game1State
        game1State = self.game1_switch_var.get()
        if self.game1_switch_var.get() == 1:
            print('Game 1 enabled')
        elif self.game1_switch_var.get() == 0:
            print('Game 1 disabled')

    def ultimate1SwitchValue(self):
        global ultimate1State
        ultimate1State = self.ultimate1_var.get()
        if self.ultimate1_var.get() == 1:
            print('ultimate enabled')
        elif self.ultimate1_var.get() == 0:
            print('ultimate disabled')

    def game2SwitchValue(self):
        global game2State
        game2State = self.game2_switch_var.get()
        if self.game2_switch_var.get() == 1:
            print('Game 2 enabled')
        elif self.game2_switch_var.get() == 0:
            print('Game 2 disabled')

    def ultimate2SwitchValue(self):
        global ultimate2State
        ultimate2State = self.ultimate2_var.get()
        if self.ultimate2_var.get() == 1:
            print('ultimate enabled')
        elif self.ultimate2_var.get() == 0:
            print('ultimate disabled')
    def game3SwitchValue(self):
        global game3State
        game3State = self.game3_switch_var.get()
        if self.game3_switch_var.get() == 1:
            print('Game 3 enabled')
        elif self.game3_switch_var.get() == 0:
            print('Game 3 disabled')

    def ultimate3SwitchValue(self):
        global ultimate3State
        ultimate3State = self.ultimate3_var.get()
        if self.ultimate3_var.get() == 1:
            print('ultimate enabled')
        elif self.ultimate3_var.get() == 0:
            print('ultimate disabled')

    def game4SwitchValue(self):
        global game4State
        game4State = self.game4_switch_var.get()
        if self.game4_switch_var.get() == 1:
            print('Game 4 enabled')
        elif self.game4_switch_var.get() == 0:
            print('Game 4 disabled')

    def ultimate4SwitchValue(self):
        global ultimate4State
        ultimate4State = self.ultimate4_var.get()
        if self.ultimate4_var.get() == 1:
            print('ultimate enabled')
        elif self.ultimate4_var.get() == 0:
            print('ultimate disabled')

######################### Ultimate #########################
  
    def ultimate1(self):
        global ultimate1State
        if ultimate1State == 1:
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            print('Ultimate pressed')
        else:
            print('Ultimate is disabled, function skipped')

    def ultimate2(self):
        global ultimate2State
        if ultimate2State == 1:
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            print('Ultimate pressed')
        else:
            print('Ultimate is disabled, function skipped')

    def ultimate3(self):
        global ultimate3State
        if ultimate3State == 1:
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            print('Ultimate pressed')
        else:
            print('Ultimate is disabled, function skipped')

    def ultimate4(self):
        global ultimate4State
        if ultimate4State == 1:
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            autoit.send("rrrrrrrrrrr")
            print('Ultimate pressed')
        else:
            print('Ultimate is disabled, function skipped')

######################### Backpack item click #########################    
    def backpack(self):
        autoit.mouse_click("left")
######################### macro #########################    
    # def start_stop_macro(self):
    #     global macroState
    #     global keyPress
    #     # global listener
    #     if macroState == 1:
    #         click_thread.start()
    #         print('macro started')
    #     elif keyboard.is_pressed('2'):
    #         keyPress = 2
    #         print('waiting')
    #         click_thread.stop()

    #     else:
    #         print('not enabled')
######################### Mouse Handles #########################
    #stop button
    def startMouseLocationsb(self):
        global stopButton_x
        global stopButton_y
        self.consoleUpdates.configure(text = 'Recording in 5 seconds')
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        stopButton_x = x
        stopButton_y = y
        self.sb_label.configure(text = ('Configured\npress save'))
        print('Mouse location sb', values)
        self.consoleUpdates.configure(text = 'Recorded.\nPress Start to redo\nor save to save')
    
    def mouseEntrysb_x(self):
        global stopButton_x
        print('Mouse location 1 saved')
        self.sb_label.configure(text = 'Ready', text_color ='#39FF14')
        self.consoleUpdates.configure(text = 'Ready to move on to games')
        return mouse_entry_1_x

    def mouseEntrysb_y(self):
        global stopButton_y
        return stopButton_y

    # input 1    
    def startMouseLocation1(self):
        global mouse_entry_1_x
        global mouse_entry_1_y
        self.consoleUpdates.configure(text = 'Recording in 5 seconds')
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        mouse_entry_1_x = x
        mouse_entry_1_y = y
        self.label1.configure(text = ('Configured\npress save'))
        print('Mouse location 1', values)
        self.consoleUpdates.configure(text = 'Recorded.\nPress Start to redo\nor save to save')
    
    def mouseEntry1_x(self):
        global mouse_entry_1_x
        print('Mouse location 1 saved')
        self.label1.configure(text = 'Ready', text_color ='#39FF14')
        self.consoleUpdates.configure(text = 'Ready for next game.\nOr if you are finished\n click start')
        return mouse_entry_1_x

    def mouseEntry1_y(self):
        global mouse_entry_1_y
        return mouse_entry_1_y

    # input 2    
    def startMouseLocation2(self):
        global mouse_entry_2_x
        global mouse_entry_2_y
        self.consoleUpdates.configure(text = 'Recording in 5 seconds')
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        mouse_entry_2_x = x
        mouse_entry_2_y = y
        self.label2.configure(text = ('Configured\npress save'))
        print('Mouse location 2', values)
        self.consoleUpdates.configure(text = 'Recorded.\nPress Start to redo\nor save to save')
    
    def mouseEntry2_x(self):
        global mouse_entry_2_x
        print('Mouse location 2 saved')
        self.label2.configure(text = 'Ready', text_color ='#39FF14')
        self.consoleUpdates.configure(text = 'Ready for next game.\nOr if you are finished\n click start')
        return mouse_entry_2_x

    def mouseEntry2_y(self):
        global mouse_entry_2_y
        return mouse_entry_2_y

    # input 3    
    def startMouseLocation3(self):
        global mouse_entry_3_x
        global mouse_entry_3_y
        self.consoleUpdates.configure(text = 'Recording in 5 seconds')
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        mouse_entry_3_x = x
        mouse_entry_3_y = y
        self.label3.configure(text = ('Configured\npress save'))
        print('Mouse location 3', values)
        self.consoleUpdates.configure(text = 'Recorded.\nPress Start to redo\nor save to save')
    
    def mouseEntry3_x(self):
        global mouse_entry_3_x
        print('Mouse location 3 saved')
        self.label3.configure(text = 'Ready', text_color ='#39FF14')
        self.consoleUpdates.configure(text = 'Ready for next game.\nOr if you are finished\n click start')
        return mouse_entry_3_x

    def mouseEntry3_y(self):
        global mouse_entry_3_y
        return mouse_entry_3_y

    # input 4    
    def startMouseLocation4(self):
        global mouse_entry_4_x
        global mouse_entry_4_y
        self.consoleUpdates.configure(text = 'Recording in 5 seconds')
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        mouse_entry_4_x = x
        mouse_entry_4_y = y
        self.label4.configure(text = ('Configured\npress save'))
        print('Mouse location 4', values)
        self.consoleUpdates.configure(text = 'Recorded.\nPress Start to redo\nor save to save')
    
    def mouseEntry4_x(self):
        global mouse_entry_4_x
        print('Mouse location 4 saved')
        self.label4.configure(text = 'Ready', text_color ='#39FF14')
        self.consoleUpdates.configure(text = 'Ready for next game.\nOr if you are finished\n click start')
        return mouse_entry_4_x

    def mouseEntry4_y(self):
        global mouse_entry_4_y
        return mouse_entry_4_y

######################### Account Menu #########################
    def randomTimedHop(self):
        self.afkInt = random.randint(3000,10000)
        self.secondsConversion = self.afkInt / 1000
    
    def stopButton(self):
        autoit.mouse_move(stopButton_x, stopButton_y)

    def game1(self):
        global game1State
        if game1State == 1:
            if mouse_entry_1_x == 0 or mouse_entry_1_y == 0:
                return print('Not used')
            else :
            # self.consoleUpdates.configure(text = 'Working on Game 1')
                autoit.mouse_click("left", mouse_entry_1_x, mouse_entry_1_y)
                time.sleep(5)
                autoit.mouse_click("left", mouse_entry_1_x, mouse_entry_1_y)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                self.ultimate1()
                time.sleep(2)
        else:
            print("game 1 is not enabled")


    def game2(self):
        global game2State
        if game2State == 1:
            if mouse_entry_2_x == 0 or mouse_entry_2_y == 0:
                return print('Not used')
            else :
            # self.consoleUpdates.configure(text = 'Working on Game 1')
                autoit.mouse_click("left", mouse_entry_2_x, mouse_entry_2_y)
                time.sleep(5)
                autoit.mouse_click("left", mouse_entry_2_x, mouse_entry_2_y)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                self.ultimate1()
                time.sleep(2)
        else:
            print("game 2 is not enabled")

    def game3(self):
        global game3State
        if game3State == 1:
            if mouse_entry_3_x == 0 or mouse_entry_3_y == 0:
                return print('Not used')
            else :
            # self.consoleUpdates.configure(text = 'Working on Game 1')
                autoit.mouse_click("left", mouse_entry_3_x, mouse_entry_3_y)
                time.sleep(5)
                autoit.mouse_click("left", mouse_entry_3_x, mouse_entry_3_y)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                self.ultimate1()
                time.sleep(2)
        else:
            print("game 3 is not enabled")

    def game4(self):
        global game4State
        if game4State == 1:
            if mouse_entry_4_x == 0 or mouse_entry_4_y == 0:
                return print('Not used')
            else :
            # self.consoleUpdates.configure(text = 'Working on Game 1')
                autoit.mouse_click("left", mouse_entry_4_x, mouse_entry_4_y)
                time.sleep(5)
                autoit.mouse_click("left", mouse_entry_4_x, mouse_entry_4_y)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                autoit.mouse_click("left")
                time.sleep(2)
                self.ultimate1()
                time.sleep(2)
        else:
            print("game 4 is not enabled")

    def aFK(self):
        if startAFK == True and stopAFK == False:
            self.consoleUpdates.configure(text = 'Running',text_color ='#39FF14')
            self.game1()
            self.game2()
            self.game3()
            self.game4()
            self.stopButton()
            app.after(20000,self.aFK)

        elif stopAFK == True and startAFK == False:
            print('Program stopped')
            self.consoleUpdates.configure(text = 'Program stopped')

    def start_AFK(self):
        global startAFK
        startAFK = True
        global stopAFK
        stopAFK = False
        self.start_afk_inbg()
        print('Anti AFK activated')
        self.consoleUpdates.configure(text = 'Anti AFK activated')
        self.afk_button.configure(text = "Stop Anti AFK", fg_color="Red",hover_color='darkred',command=self.stop_all)
        

    def stop_all(self):
        global startAFK
        startAFK = False
        global stopAFK
        stopAFK = True
        self.afk_button.configure(text = "Start Anti AFK", fg_color="#1F6AA5", hover_color='#144870',command=self.start_AFK)
        self.consoleUpdates.configure(text = 'Stopping Application...\nDo not close until\n"Program stopped" is displayed',text_color ='white')
        print('Stopping Application... Please keep roblox open and')
        print('wait until "Program stopped" is displayed to close window')

    def start_afk_inbg(self):
        threading.Thread(target=self.aFK).start()
    

### APP Frame DONE ###
class App(ctk.CTk):
    # TODO
    # Reflect window changes
    # make window larger to account for new functions

    def __init__(self):
        super().__init__()
        self.geometry("350x490")
        self.minsize(350, 490)
        self.maxsize(350, 490)
        self.resizable(False, False)
        # self.iconbitmap(icon)
        self.title("RobDaDev")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title_frame = ProjectTitleFrame(master=self)
        self.title_frame.grid(row=0, column=0, padx=10, pady=10,
                                        sticky="nsew", columnspan=1)
        self.button_housing = MainFrame(master=self)
        self.button_housing.grid(row=1, column=0, padx=10,pady=(0,10), ipady=10, ipadx=10, sticky='nsew')


app = App()
app.mainloop()
# listener.join()

