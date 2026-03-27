# Write a program that opens an existing text file, reads its contents, and creates a new file with a different name, writing the copied content to the new file.

file = open("mbox.txt", "r")
content = file.read()#reads the entire content of the file and stores it in the variable 'content'.
file.close()

new_file = open("mbox_copy.txt", "w")
new_file.write(content) #writes the content of the variable 'content' to the new file.
new_file.close()

print("File copied successfully!")
