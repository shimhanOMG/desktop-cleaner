import os 
import shutil


desktop = "C:\\Users\\Arujith\\Desktop\\"
pcdir = "C:\\Users\\Arujith\\Desktop\\images\\"
pdfdir = "C:\\Users\\Arujith\\Desktop\\PDF\\"
auddir = "C:\\Users\\Arujith\\Desktop\\audio\\"
regdir = "C:\\Users\\Arujith\\Desktop\\files\\"


for fname in os.listdir(desktop):
    
    if fname.endswith(".pdf"):
        shutil.move(desktop+fname, pdfdir+fname)
        print(fname + " moved")
    elif fname.endswith(".jpg") or fname.endswith(".png"):
        shutil.move(desktop+fname, pcdir+fname)
        print(fname + " moved")
    elif fname.endswith(".mp3"):
        shutil.move(desktop+fname, auddir+fname)
        print(fname + " moved")
    
    if fname =="files":
        print("file cannot be moved")
    else:
        shutil.move(desktop+fname,regdir+fname)
        print(fname + " moved")
    

print("desktop cleanup complete")
