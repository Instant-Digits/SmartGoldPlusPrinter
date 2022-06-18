import os
import platform
from glob import glob
import shutil
cwdForward = os.getcwd()
cwd = cwdForward.replace('\\','/')

if (platform.system()=='Windows'):
    import win32api
    import win32print
    from termcolor import colored
    GHOSTSCRIPT_PATH = cwdForward+r"\GHOSTSCRIPT\bin\gswin32.exe"
    GSPRINT_PATH = cwdForward+r"\GSPRINT\gsprint.exe"
    printer_num =-1
    all_printers = ['None - Dont do anything Just run the server','Generate PDF Only' ]+[ printer[2] for printer in win32print.EnumPrinters(2)]
   
    while (printer_num<0):
        try :
            printer_num =int(input("\nChoose a printer for all purpose except LABEL:\n\n"+"\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n\n"+ colored('Select the option number and Press Enter : ', 'yellow')))
        except:
            print('Input Error')

    
    
    



def printPDF(fileName):   
    if (platform.system()=='Windows'):
        global cwd, printer_num, all_printers, GHOSTSCRIPT_PATH, GSPRINT_PATH
        if (printer_num==0):
            return
        elif(printer_num==1):
            desktopOut = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+ '\GoldPlusOutputs'
            
            if not os.path.isdir(desktopOut):
                os.system('mkdir '+desktopOut)
            os.system(r'copy '+fileName+ r' '+desktopOut)
            print(colored('Pls find the '+fileName+' in the folder : Desktop/GoldPlusOutputs\n', 'green'))
            return
        # win32print.SetDefaultPrinter(all_printers[printer_num])
        
        if 'invoice' in fileName:
            win32api.ShellExecute(0, "print", cwd+'/'+fileName, '/d:"%s"' % all_printers[printer_num],  ".",  0)

        else :
            win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -dPDFFitPage -color -printer "'+all_printers[printer_num]+'" '+fileName+'"', '.', 0)

        # os.system('start cmd /c "timeout 1 & taskkill /f /im Acrobat.exe"')
        # os.system("Acrobat.exe /t "+fileName+" "+ all_printers[printer_num])
        
        print(colored(fileName+' is set to be printed\n', 'green'))
        

    else :
        os.system('lp ./'+fileName)


# printPDF('destination.pdf')





