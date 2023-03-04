# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
list=[]
value=input("Enter Elements in List and Enter exit to end loop\n: ")
while(True):
    list.append(int(value))
    value=input(": ")
    if (value == "exit"):
        break
ask=int(input("Enter specific number to check its occurnce in list: "))
print(ask," occurs ",list.count(ask), "times in a list")
