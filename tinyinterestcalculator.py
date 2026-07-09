v=["", "", ""]
p=["Initial Principal Balance", "Rate (In Decimal)", "Number of Years Elapsed"]
for i in range(len(v)):
    t=""
    i=int(i)
    while not t.replace(".","",1).isdigit() or float(t) <= 0:
        t=input(f"{p[i]} : ")
    v[i]=float(t)
f = v[0]*pow(1+v[1],v[2])
print(f)
