v = ["", "", "",]
varprompt = ["Initial Principal Balance", "Rate (in decimal)", "Number of Years Elapsed",]
for i in range(len(v)):
    temp = "0"
    i = int(i)
    while not temp.isalnum() or temp.upper() != temp.lower() or int(temp) <= 0:
        temp = input(f"{varprompt[i]} : ")
    v[i] = float(temp)
total = v[0] * pow(1 + v[1], v[2])
print(total)
