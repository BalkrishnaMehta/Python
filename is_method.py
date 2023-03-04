class base():
    pass
class derived(base):
    pass
class superderived():
    pass
obj1=base()
obj2=derived()
obj3=superderived()
print("Obj1 is the instance of base" if(isinstance(obj1,base)==True) else "Obj1 is not the instance of base")
print("Obj2 is the instance of base" if(isinstance(obj2,base)==True) else "Obj2 is not the instance of base")
print("derived is the sub class of base" if(issubclass(derived,base)==True) else "derived is not the sub class of base")
print("superderived is the sub class of base" if(issubclass(superderived,base)==True) else "superderived is not the sub class of base")
