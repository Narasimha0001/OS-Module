import os

def check_folder(folder_name):
    path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Directory '{folder_name}' created at: {path}")
    else:
        print(f"Directory '{folder_name}' already exists at: {path}")

    txt_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.txt') and os.path.isfile(f)]

    if txt_files:
        print("Text files in Direcotry:")
        for file in txt_files:
            os.rename(os.path.join(os.getcwd(),file), os.path.join(path,file))
            print(file)
    else:
        print("No .txt files found in the current directory.")

if __name__ == "__main__":
    folder_name = input("Enter the name of the folder to create: ")
    check_folder(folder_name)        
