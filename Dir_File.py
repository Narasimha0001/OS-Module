import os

def check_path(path='.'):
    if os.path.isfile(path):
        return "It's a file."
    elif os.path.isdir(path):
        return "It's a directory."
    else:
        return "The path does not exist or is neither a file nor a directory."

if __name__ == "__main__":
    path = input("Enter the path: ")
    result = check_path("./Dir_File.py" if not path else path)
    print(result)
