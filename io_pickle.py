import pickle

# We will store the object's file name
shoplistfile = 'shoplist.data'
# The list need to be buy
shoplist = ['apple', 'mango', 'carrot']

# Ready to write into file
f = open(shoplistfile, 'wb')
# Transfer object to file
pickle._dump(shoplist, f)
f.close()

# clear the shoplist variant
del shoplist

# Reopen the store file
f = open(shoplistfile, 'rb')
# Load object from file
storedlist = pickle.load(f)
print(storedlist)
