with open("notes.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("I am preparing for placements.")

# Step 2: Read the file
with open("notes.txt", "r") as file:
    content = file.readlines()

print(content)

# tell() and seek()
with open("notes.txt","r") as file:
    file.read(3)
    print(file.tell())
    file.seek(0)