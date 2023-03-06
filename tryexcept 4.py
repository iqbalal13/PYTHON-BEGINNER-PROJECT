try:
    file_name = input("Enter the name of the file you want to open: ")
    with open(file_name, 'r') as file:
        contents = file.read()
        print("The contents of the file are:", contents)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except:
    print("An error occurred while trying to open the file.")