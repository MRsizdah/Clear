import os 
import glob
from colorama import Fore , init
from pyfiglet import Figlet

#banner
banner = Figlet()
os.system("cls")
#banner print
print(Fore.RED + banner.renderText('CLEAR') )
print(Fore.RED + ">MR XIII--------------------v.1<")



#Question
print(Fore.RED + 'Which format do you decide to delete? ')
print(Fore.WHITE + '[1] .mp3' )
print(Fore.WHITE + '[2] .psd' )
print(Fore.WHITE + '[3] .txt' )
print(Fore.WHITE + "[4] other format's " )
print(Fore.RED + "<------------------------------>")
#User selection
print(Fore.WHITE  )
suffixNum = int(input("Enter the format Number ==> "))



#user selected 1
if suffixNum == 1:
    #Clears mp3 files
    listt = glob.glob("*.mp3")
    init()
    if listt:
        for file in listt:
            os.remove( file  )
            print(Fore.GREEN + "[+]  " + Fore.GREEN + file  )
    else:
        print(Fore.RED + "The file does not exist in such a format")
#user selected 2
elif suffixNum == 2:
    #Clears psd files
    listt = glob.glob("*.psd")
    init()
    if listt:
        for file in listt:
            os.remove( file  )
            print(Fore.GREEN + "[+]  " + Fore.GREEN + file  )
    else:
        print(Fore.RED + "The file does not exist in such a format")
#user selected 3
elif suffixNum == 3:
    #Clears txt files
    listt = glob.glob("*.txt")
    init()
    if listt:
        for file in listt:
            os.remove( file  )
            print(Fore.GREEN + "[+]  " + Fore.GREEN + file  )
    else:
        print(Fore.RED + "The file does not exist in such a format")
#user selected 4
elif suffixNum == 4:
    #Clears psd other files
    print(Fore.RED + "<------------------------------>"
    print(Fore.WHITE  )
    suffix = input("Enter you Suffix for example 'mp3' ==> ")
    
    listt = glob.glob("*."+suffix)
    init()
    if listt:
        for file in listt:
            os.remove( file  )
            print(Fore.GREEN + "[+]  " + Fore.GREEN + file  )
    else:
        print(Fore.RED + 'The file does not exist in such a format')
