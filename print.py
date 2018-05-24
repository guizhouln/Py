age = 20
name = 'swaroop'

print('{} was {} year old when wrote this book!'.format(name, age))
print('why is	{} playing with that python?'.format(name))

# 对于浮点数 ‘0.333’保留小数点（.)后三位
print("{0:.3f}".format(1.0 / 3))
#
# set the format length to 11
print("{0:_^11}".format('Hello!'))

# Base output
print('{name} wrote {book}'.format(name='Swaroop', book='A byte of Python'))

print('a', end=" ")
print('b', end=' ')
print('c')

# 转义序列 use \
print('What\'s your name!')
# test
print("'This is the first line\nThis is the second line'")
#
print('\"This is the first sentence.\tThis is the second sentence.\"')
#
print(r"Newlines are indicated by \n")
