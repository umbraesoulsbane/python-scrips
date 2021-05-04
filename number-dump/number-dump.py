import pyperclip

print("\n\n")
print("****************************************************************")
print("                 Screw with Count to a Mil")
print("****************************************************************\n\n")

start_string = input("Start Number: ")

char_count = 0
write_string_full = ''
  
print('\n------------------------- D O N E ------------------------------\n')


count = int(start_string)
while char_count < 1650:
    write_string = str(count) + '\n'
    char_count += len(write_string)
    write_string_full += write_string
    count += 1

print("Character Count: " + str(char_count))
print("Last Number: " + str(write_string))

pyperclip.copy(str(write_string_full))

print("================== Contents added to clipboard =================\n\n")