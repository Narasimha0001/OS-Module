import os

def create_test_folder():
    path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Directory '{folder_name}' created at: {path}")
    else:
        print(f"Directory '{folder_name}' already exists at: {path}")

if __name__ == "__main__":
    folder_name = input("Enter the name of the folder to create: ")
    if not folder_name:
        folder_name = "test_folder"
    create_test_folder()
