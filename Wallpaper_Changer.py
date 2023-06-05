import ctypes
import os
import random
import shutil
import sys
import subprocess
my_list=[]
Directory="" #Resimleri barındıran Klasörün Yolu
Dosya_Listesi=os.listdir(Directory)

for file in Dosya_Listesi:
    my_list.append(file) #Klasorün içindeki resim dosyalarını listemize ekledik.

Resim=random.choice(my_list) #Listemizden rastgele bir dosya seçtik ve bunu Resim' atadık. Böylelikle random resim seçilmiş oldu.
Resim_yolu=Directory +("\\")+(Resim) #Resmin tam dosya yolunu aldık.
ctypes.windll.user32.SystemParametersInfoW(20,0,Resim_yolu,3) #Duvar kağıdı değiştirme komutumuz.
#Başlangıca Yerleşme:

Dosya=os.environ["appdata"] +"\\Wallpaper_Changer.exe"

if not os.path.exists(Dosya): #Önceden dosya olup olmadığını kontrol ediyoruz, başlangıçta varsa tekrar başlangıca almamıza gerek yok.
    try:
        shutil.copy(sys.executable,Dosya)
        regedit_komutu="reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Wallpaper_Changer /t REG_SZ /d "+Dosya
        print(regedit_komutu)
        subprocess.call(regedit_komutu,shell=True)
    except Exception as a:
        print(a)
