import os

def list_txt_files():
    current_dir = os.getcwd()
    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt') and os.path.isfile(f)]

    if txt_files:
        print("Text files in the current directory:")
        for file in txt_files:
            print(file)
    else:
        print("No .txt files found in the current directory.")

if __name__ == "__main__":
    list_txt_files()
