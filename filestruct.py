# File Read & Write Challenge with Error Handling

def main():
    # Ask user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Open the file in read mode
        with open("filehand.xls", "r") as file:
            content = file.read()
            print("Original Content:")
            print(content)

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new file and write the modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write("JOHN, ESTER, PETER")

        print(f"✅ Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to access this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
