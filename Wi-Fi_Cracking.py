import os
import random
import string
import subprocess

def find_john():
    """Find John the Ripper executable in system PATH or common directories."""
    possible_paths = [
        "/usr/bin/john", "/usr/local/bin/john", "C:\\john\\run\\john.exe",
        "C:\\Program Files\\JohnTheRipper\\run\\john.exe"
    ]
    
    for path in os.environ["PATH"].split(os.pathsep):
        possible_paths.append(os.path.join(path, "john"))
    
    for path in possible_paths:
        if os.path.exists(path) and os.access(path, os.X_OK):
            return path
    
    return None

def check_dependencies():
    """Check if John the Ripper is installed."""
    john_path = find_john()
    if not john_path:
        print("Error: John the Ripper is not installed or not in the system PATH. Please install it before proceeding.")
        exit(1)
    return john_path

def generate_passwords(length, charset, count=1000):
    """Generate a list of random passwords based on user constraints."""
    return [''.join(random.choices(charset, k=length)) for _ in range(count)]

def run_john_the_ripper(john_path, cap_file, wordlist):
    """Run John the Ripper against the .cap file using a given wordlist."""
    try:
        subprocess.run([john_path, "--wordlist=" + wordlist, "--format=wpapsk", cap_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: John the Ripper encountered an issue: {e}")
    except FileNotFoundError:
        print("Error: John the Ripper executable not found. Make sure it is installed and accessible.")

def main():
    john_path = check_dependencies()
    
    while True:
        try:
            length = int(input("Enter password length (6-15): "))
            if 6 <= length <= 15:
                break
            else:
                print("Please enter a valid length between 6-15.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    charset = input("Enter character set (default: letters, digits, punctuation): ")
    if not charset:
        charset = string.ascii_letters + string.digits + string.punctuation
    
    cap_file = input("Enter the full path to the .cap file: ")
    
    if not os.path.exists(cap_file):
        print(f"Error: The specified file path '{cap_file}' does not exist. Please check the path and try again.")
        return
    
    if not cap_file.endswith(".cap"):
        print(f"Error: The specified file '{cap_file}' is not a .cap file. Please provide a valid .cap file.")
        return
    
    print(f"Using .cap file: {cap_file}")
    
    # Generate passwords dynamically
    generated_passwords = generate_passwords(length, charset)
    
    # Save passwords in memory (not disk)
    print("Running John the Ripper with generated passwords...")
    try:
        process = subprocess.Popen([john_path, "--stdin", "--format=wpapsk", cap_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for password in generated_passwords:
            process.stdin.write((password + "\n").encode())
        process.stdin.close()
        process.wait()
    except FileNotFoundError:
        print("Error: John the Ripper executable not found. Make sure it is installed and accessible.")
        return
    except subprocess.CalledProcessError as e:
        print(f"Error: John the Ripper encountered an issue: {e}")
        return
    
    # Running John the Ripper with RockYou.txt (if available)
    rockyou_path = "/usr/share/wordlists/rockyou.txt"
    if os.path.exists(rockyou_path):
        print("Running John the Ripper with RockYou.txt...")
        run_john_the_ripper(john_path, cap_file, rockyou_path)
    else:
        print("RockYou.txt not found! Skipping...")
    
    print("Cracking attempt finished. Check John the Ripper output.")

if __name__ == "__main__":
    main()