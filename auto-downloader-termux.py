import os
import time

def clear_screen():
    os.system('clear')  # EkranÄ± temizle

def install_packages():
    os.system('apt update && apt upgrade -y')
    os.system('pkg update && pkg upgrade -y')
    os.system('pkg install python2 -y')
    os.system('pkg install git -y')

def clone_wifite_repository():
    if os.system('git clone https://github.com/derv82/wifite.git') != 0:
        clear_screen()
        print("Error: 'wifite' directory creation failed. \n")
        print("Maybe Wifite Already Exists\n")
        print("")
        print("")
        return False
    return True

def main():
    clear_screen()
    print("Helloo!")
    time.sleep(1.8)
    clear_screen()
    print("")
    print("Wifite made By   derv82 ")
    
    
    
    time.sleep(2)
    for i in range(1, 4):
        loading_text = "Installer Made By.   Sertxs" + "." * i
        print(loading_text, end='', flush=True)
        time.sleep(1)
        clear_screen()
        time.sleep(0)
        
        print("")
        print("WARNÄ°NG THÄ°S Ä°S MADE FOR Ä°NSTALL WÄ°FÄ°TE")
        print("ALSO FOR LAZY NERDS!")
        print("")
    
    choice = input("Do you Wanna Continue Fella? (y/n): ")

    if choice == 'y':
        for _ in range(3):
            print("Loading...", end='', flush=True)
            time.sleep(1)
            clear_screen()
            time.sleep(0)

        install_packages()

        if clone_wifite_repository():
            os.system('cd wifite')
            time.sleep(0.2)
            os.system('chmod +x wifite.py')
            time.sleep(0.4)
            os.system('cd ..')
            time.sleep(0.1)
            clear_screen()
            time.sleep(1.6)
            os.system('ls')

            print("\n\nWifite is Successfully Downloaded\n\n")
            print("")
            print("; )")

    else:
        os.system('clear')
        print("Closing the App...\n")
        print(":*(")
        time.sleep(4.2)
        clear_screen()

if __name__ == "__main__":
    main()