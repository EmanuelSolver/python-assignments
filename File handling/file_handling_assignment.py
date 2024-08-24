
def create_and_write_file():
    try:
        # Create and open a new text file in write mode
        with open("./my_file11.txt", "w") as file:
            # Write three lines of text to the file
            data = ["Hello, there!\n", "I love Python programming\n", "Number example: 12345\n"]
            
            for item in data:
                file.write(item)

        print("File created and written successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#File reading and displaying
def read_and_display_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read the contents of the file
            content = file.read()
            # Display the contents on the console
            print("\nContents of the file:")
            print(content)
    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# file appending
def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text
            file.write("My 1st name is ken\n")
            file.write("My phone number is +254712308234\n")
            file.write("My home address is: 678 4th street\n")
        print("Data appended successfully.")
        
    except FileNotFoundError:
        print("File not found: Unable to append to the file.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
