from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that. hit CTRL-c (^C).")
print("If you do want that. hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask ou for three lines.")

line = input("line 1: ")
line = input("line 2: ")
line = input("line 3: ")

print("I'm going to write these to the file.")

target.write("line1")
target.write("\n")
target.write("line2")
target.write("\n")
target.write("line3")
target.write("\n")

print("And finally, we close it.")
target.close()

