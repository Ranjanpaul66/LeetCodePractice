try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content.join("Test"))
except FileNotFoundError:
    print("File not found!")
except OSError:
    print("An OS error occurred!")