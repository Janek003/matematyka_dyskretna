import subprocess

def main():
    # Start a subprocess
    process = subprocess.Popen(['your_command_here'])
    
    # Main function code
    print("Main function is running...")

    # Do something in the main function
    # After main function ends, terminate the subprocess
    process.terminate()  # This will kill the subprocess when the main function finishes

if __name__ == "__main__":
    main()
#reads a string and checks if its using correct characters
#deletes all white space
#before '=' string L, after string R
#some sort of statment analasys,where statements are extracted from inside brackets