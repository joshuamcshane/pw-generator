#from pathlib import Path

#p = Path('/usr/share/dict/words')

#print(p)

#import random module
import random

#open words file
words = open('/usr/share/dict/web2', mode='r')

# #read words file into list
file_contents = words.read().splitlines()

#get length of words file, minus 1 for zero index
length = len(file_contents) - 1

number_of_words = input("How many words do you want in your random string?\n")

number_of_words_int = int(number_of_words)

output = ""

i = 0

#append random words to output string, with a single random digit between each word.
while i < number_of_words_int:
     output += file_contents[random.randint(0,length)] + str(random.randint(0,9))
     i += 1

print(output)

words.close()