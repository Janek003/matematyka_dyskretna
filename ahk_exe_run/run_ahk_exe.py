import subprocess
import os

def main():#errro with getting a path after moving it into a folder
    current_path = os.getcwd()
    script_file_name = "ahk_exe_run\\zbiory_hotkey.exe"

    dynamic_script_path = os.path.join(current_path, script_file_name)
    print(dynamic_script_path)
    #starts overwriting 
    hotkey_script = subprocess.Popen([dynamic_script_path])
    
    a = ""
    
    while a.lower() != "stop":
        a = input("if you want to exit the program, type 'stop': ")
    
    #at the end it stops it
    hotkey_script.terminate()

if __name__ == "__main__":
    main()