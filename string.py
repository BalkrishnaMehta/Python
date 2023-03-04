s = 'hello' #can be declared in " " ''' ''' immutable
s1 = 'world'
print(s+s1) 
print(len(s)) # print 5
x= list(enumerate(s)) # it will make[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
y= tuple(enumerate(s)) # it will make ((0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'))
print(s.upper()) # it will capitalize whole str and return but s will not change
print(s.lower()) #  it will lowercase whole str and return but s will not change
str = "hello world"
print(str.split()) # it will return ['hello', 'world'] a list with separeted word after space
s.replace("world","INDIA")  # it will return 'hello INDIA' but s will not change


s = 'spam'
t = list(s)
print(t)

s = 'pining-for-the-fjords'
t = s.split("-")
print(t)

t = ['p', 'y', 't', 'on']
delimiter = ' '
s = delimiter.join(t)
print(s)