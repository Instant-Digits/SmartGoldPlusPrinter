import time 
import os
import win32api
import win32print
from termcolor import colored

GHOSTSCRIPT_PATH = r"C:\Users\Next\Desktop\Instant Digits\gold\SmartPosPrinters\GHOSTSCRIPT\bin\gswin32.exe"
GSPRINT_PATH = r"C:\Users\Next\Desktop\Instant Digits\gold\SmartPosPrinters\GSPRINT\gsprint.exe"

# YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "destination.pdf"', '.', 0)
