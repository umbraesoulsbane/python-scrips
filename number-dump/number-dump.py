import pyperclip

print("\n\n")
print("****************************************************************")
print("                 Screw with Count to a Mil")
print("****************************************************************\n\n")


start_string = ""
count = 0

while str(start_string) != "q":

	print("Starting With: " + str(count) + "\n")

	start_string = input("Start Number: ") or count
	char_count = 0
	write_string_full = ""

	if str(start_string) == "q":
		break

	count = int(start_string)
	while char_count < 1650:
		write_string = str(count) + "\n"
		char_count += len(write_string)
		write_string_full += write_string
		count += 1

	pyperclip.copy(str(write_string_full))

	print("\n\n================== Contents added to clipboard =================\n\n")

	print("Character Count: " + str(char_count) + "\n\n\n\n")

	print("Last Number: " + str(write_string))

print("\n------------------------- D O N E ------------------------------\n\n\n\n\n\n")


