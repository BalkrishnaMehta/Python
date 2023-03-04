dict={"Name" : "Ayush" , "roll no" : 12, 3 : 4} # key/value pair mutable 
for a,b in dict.items():
    print(a,b)

print(dict.values())       # It will return all value from dictonary  (class = dict_values)
print(dict.items())        # It will return tupple of all key value pair   (class = dict_items)
print(dict.keys())         # it will return all key from key,value pair i.e return index of dictonary (class = dict_keys)
print(type(dict.values()))
print(type(dict.items()))
print(type(dict.keys()))  
print(dict.get("Name"))
dict.popitem()
print(dict)

a=dict.items()
b =list(a)
print(type(b[0]))

dict.clear()
