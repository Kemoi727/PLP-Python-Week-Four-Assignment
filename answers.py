#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Step 1: Read from the original file
with open("original.txt", "r") as file:
    content = file.read()

# Step 2: Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open("modified.txt", "w") as new_file:
    new_file.write(modified_content)

print("✅ File has been read, modified, and written to 'modified.txt'.")




#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
# Error Handling Lab 🧪

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n📄 File Content:\n")
        print(content)
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You do not have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
