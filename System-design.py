with open("notes.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("I am preparing for placements.")

# Step 2: Read the file
with open("notes.txt", "r") as file:
    content = file.readlines()

print(content)