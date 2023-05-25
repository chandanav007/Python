#have a python dictionary that has a key /value pair that represents a word and it's defination 
#collect input from the user, input is a word
# check if the road is in the dictionary
# print the defination
from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
       break
    
    print(dictionary.meaning(word))

