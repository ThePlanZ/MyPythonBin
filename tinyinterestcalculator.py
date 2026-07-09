v=["", "", ""]
p=["Initial Principal Balance", "Rate (In Decimal)", "Number of Years Elapsed"]
for i in range(len(v)):
    t=""
    i=int(i)
    while not t.isdigit() or int(t) < 0:
        t=input(f"{p[i]} : ")
    v[i]=float(t)
t = v[0]*pow(1+v[1],v[2])
print(t)
