from ast import literal_eval
t=literal_eval(input("enter the list of tuples"))
def ToStrng(x) :
    l=[]
    for i in x :
        l.append("=".join(i))
    s=";".join(l)
    return s

a=ToStrng(t)
print(a)
