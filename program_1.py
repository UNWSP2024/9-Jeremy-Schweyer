# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    names_text = open('names.txt', 'w')
    names_text.write("name1" + ' ')
    names_text.write("name2" + ' ')
    names_text.write("name3" + ' ')
    names_text.write("name4" + ' ')
    names_text.close()
    names_text = open('names.txt', 'r')
    names = names_text.readlines()
    names_text.close()
    print(names)
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
