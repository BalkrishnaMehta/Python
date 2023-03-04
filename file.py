'''file_obj = open("myfile.txt","w")   # total 7 functions in file # 2 ways to open or close file
file_obj.write("Hello Dhruv\n")
file_obj.write("How are you\n")
file_obj.write("What are you doing\n")
file_obj.close()

file = open("myfile.txt","r")
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)                    #f.seek changes the cursor location
print(file.readlines())         #readlines gives list
print(file.tell())             # f.tells gives the cursor location
file.close()'''


'''file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()'''


with open("myfile.txt","w") as f:          # no need to close file here as after the block it will automatically close it
    f.write("Hello dhruv\n")
    f.write("Good Morning\n")

with open("myfile.txt","r") as g:
    print(g.read())
    g.seek(0)
    print(g.readlines()) 