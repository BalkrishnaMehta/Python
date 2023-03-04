# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
def add(mat1,mat2,m1,n1):
    print("Addition is: ")
    for i  in range(m1):
        print("| ",end="")
        for j in range(n1):
            print(str(mat1[i][j]+mat2[i][j])+" ",end="")
        print("|")
def sub(mat1,mat2,m1,n1):
    print("Subtraction is: ")
    for i  in range(m1):
        print("| ",end="")
        for j in range(n1):
            print(str(mat1[i][j]-mat2[i][j])+" ",end="")
        print("|")
def mul(mat1,mat2,m1,n2,m2):
    list1=[]
    for i in range(m1):
        list2=[]
        for j in range(n2):
            a=0
            for k in range(m2):
                a+=mat1[i][k]*mat2[k][j]
            list2.append(a)
        list1.append(list2)
    print("Multiplication: ")
    for k in range (m1):
        print("| ",end="")
        for l in list1[k]:
            print(str(l)+" ",end="")
        print("|")
def trans(mat3,m3,n3):
    print("Transpose A: ")
    for k in range(n3):
        print("| ",end="")
        for l in range(m3):
           print(str(mat3[l][k])+" ",end="")
        print("|")
def main():
    opr=input("Enter add or sub or mul or trans: ")
    if(opr=="add" or opr=="sub" or opr=="mul"):
        mat1=[]
        m1=int(input("Enter number of rows of matrix A: "))
        n1=int(input("Enter number of column of matrix A: "))
        for i in range(m1):
            list1=[]
            for j in range(n1):
                value=int(input("Enter value for position "+str(i)+str(j)+": "))
                list1.append(value)
            mat1.append(list1)
        print("Matrix A: ")
        for k in range (m1):
            print("| ",end="")
            for l in mat1[k]:
                print(str(l)+" ",end="")
            print("|")

        mat2=[]
        m2=int(input("Enter number of rows of matrix B: "))
        n2=int(input("Enter number of column of matrix B: "))
        for i in range(m2):
            list2=[]
            for j in range(n2):
                value=int(input("Enter value for position "+str(i)+str(j)+": "))
                list2.append(value)
            mat2.append(list2)
        print("Matrix B: ")
        for k in range (m2):
            print("| ",end="")
            for l in mat2[k]:
                print(str(l)+" ",end="")
            print("|")
    else:
        mat3=[]
        m3=int(input("Enter number of rows of matrix A: "))
        n3=int(input("Enter number of column of matrix A: "))
        for i in range(m3):
            list3=[]
            for j in range(n3):
                value=int(input("Enter value for position "+str(i)+str(j)+": "))
                list3.append(value)
            mat3.append(list3)
        print("Matrix A: ")
        for k in range (m3):
            print("| ",end="")
            for l in mat3[k]:
                print(str(l)+" ",end="")
            print("|")

    if(opr=="add"):
        if(m1==m2 and n1==n2):
            add(mat1,mat2,m1,n1)
        else:
            main()
    if(opr=="sub"):
        if(m1==m2 and n1==n2):
            sub(mat1,mat2,m1,n1)
        else:
            main()
    if(opr=="mul"):
        if(n1==m2):
            mul(mat1,mat2,m1,n2,m2)
        else:
            main()
    if(opr=="trans"):
        trans(mat3,m3,n3)
main()
