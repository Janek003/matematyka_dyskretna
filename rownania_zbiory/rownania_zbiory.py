import subprocess
import os

def main():
    current_path = os.getcwd()
    script_file_name = "zbiory_hotkey.exe"

    dynamic_script_path = os.path.join(current_path, script_file_name)

    #starts overwriting 
    hotkey_script = subprocess.Popen([dynamic_script_path])
    
    a = ""
    
    while a.lower() != "stop":
        a = input("if you want to exit the program, type 'stop' ")
    
    #at the end it stops it
    hotkey_script.terminate()

if __name__ == "__main__":
    main()