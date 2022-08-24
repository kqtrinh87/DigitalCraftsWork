# Creating a file via python
# 'w' creates a file if it doesn't already exist
file = open('newFile.txt', 'w')
print(type(file))

# To write to a file:
file.write("Good morning, it's Friday!")
file.close()

# To read a file:
file = open('newFile.txt', 'r')
print(file.read())

# Modifying a file:
# 'a' append the new data to the end of the file
file = open('newFile.txt','a')
file.write( '\nHope you guys have a great weekend')
file.close()


file = open('newFile.txt','r')
file.close
print(file.read())

# Overwriting a file
file = open('newFile.txt','w')
file.write( '\nWe will be learning about bootstrap today.')
file.close()

file = open('newFile.txt','r')
file.close
print(file.read())