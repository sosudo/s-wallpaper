import os
import ctypes
import random
dir = os.listdir('images')
file = random.choice(dir)
filepath = os.getcwd()+'\\images\\' + file
ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)