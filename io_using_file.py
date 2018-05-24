poem = '''\
Programing is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open a file to edit('w'riting)
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close file
f.close()

# if did not special make a key to file
# will open the default reading module('r'read)
f = open('poem.txt')
while True:
    line = f.readline()
    # EOF
    if len(line) == 0:
        break
    # every ('line')'s end
    # when there is a \t
    # Because read from a file
    print(line, end='')

# close the file
f.close()
