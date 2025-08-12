


def again():
    a=int(input("Do you want to see more books? (1 for yes, 0 for no): "))
    if(a==1):
        bookinfo()
    else:
        print("bye,bye")

def bookinfo():
    a=int(input("enter choice form 1,2,3"))
    if(a==1):
        print("book name 1")
        print("author name 1")
        print("price 1")
    elif(a==2):
        print("book name 2")
        print("author name 2")
        print("price 2")
    elif(a==3):
        print("book name 3")
        print("author name 3")
        print("price 3")
    again()



bookinfo()
