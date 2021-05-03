import pyperclip

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
    write_string_full += write_string
    count += 1

print(char_count)

pyperclip.copy(str(write_string_full))

