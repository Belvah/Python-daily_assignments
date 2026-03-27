# Write a program that opens a text file and iterates through each line using a for loop, printing each line separately.

file = open("mbox.txt", "r") #opens the file "mbox.txt" in read mode and assigns the file object to the variable 'file'.

for line in file: #iterates through each line in the file object 'file' and assigns the current line to the variable 'line' in each iteration.
    print(line.strip()) #prints the current line after removing any leading and trailing whitespace characters.

file.close()
