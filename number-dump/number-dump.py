import pyperclip
from collections import Counter

print("****************************************************************")
print("                 Screw with Count to a Mil")
print("****************************************************************\n\n")

start_string = input("Start Number: ")

char_count = 0
write_list = []
write_string_full = ''
  
print('-----------------------------------------------------------')


count = int(start_string)
while char_count < 1650:
    write_string = str(count) + '\n'
    char_count += len(write_string)
    #write_list.append(write_string)
    write_string_full += write_string
    count += 1

print(char_count)

#file1 = open("count.txt","w")
#file1.writelines(write_list)
#file1.close()

pyperclip.copy(str(write_string_full))
