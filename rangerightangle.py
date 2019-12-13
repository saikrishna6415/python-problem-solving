start = int(input("starting range : "))

end = int(input("ending range : "))
for i in range(start,end+1):
    print(str(i)*(i-start+1))
for i in range(start,end)[::-1]:
    print(str(i)*(i-start+1))