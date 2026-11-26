#//shutdownTool.py//#

import subprocess
import os

def pause():
    input("\n[INFO] Press Enter to return to the main menu...")
    
def set_shutdown_time():
    while True:

        user_input = input("[INPUT]Enter time in minutes (or 'q' to cancel): ").strip()
        
        if user_input.lower() == 'q':
            print("[INFO] Operation canceled.")
            return 
            
        try:
            minutes = int(user_input)
            if minutes <= 0:
                print("[WARN] Please enter a positive number.")
                continue
                
            seconds = minutes * 60
            subprocess.run(["shutdown", "/s", "/t", str(seconds)])
            print(f"[INFO] Shutdown scheduled in {minutes} minutes.")
            break  
            
        except ValueError:
            print("[WARN] Invalid input. Please enter a valid number.")
    
def cancel_shutdown():
    result = subprocess.run(["shutdown", "/a"], capture_output=True, text=True)
    if result.returncode == 0:
        print("[INFO]Shutdown canceled.")
    else:
        print("[WARN]Failed to cancel shutdown. There might not be a scheduled shutdown.")
        
def main_menu():
    print("=" * 40)
    print("[MENU] Tool for shutdown your computer")
    print("-" * 40)
    print("1. Set the time for shutdown")
    print("2. Cancel the shutdown")
    print("3. Exit")
    print("=" * 40)

while True:
    os.system("cls")

    main_menu()
    
    choice = input("[INPUT]Enter your choice (1/2/3): ").strip()

    if choice == "1":
        set_shutdown_time()
        pause()
    elif choice == "2":
        cancel_shutdown()
        pause()
    elif choice == "3":
        print("[INFO]Exiting the program.")
        break
    else:
        print("[WARN]Invalid choice.")
        pause()








