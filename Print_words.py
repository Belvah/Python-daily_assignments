#Write a program that takes a sentence and then prints the number of words in that sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print(sentence)
print("The number of words in the sentence is:", len(words))