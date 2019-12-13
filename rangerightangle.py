start = int(input("starting range : "))

end = int(input("ending range : "))
for i in range(start,end+1):
    print(str(i)*(i-start+1))
for i in range(start,end)[::-1]:
    print(str(i)*(i-start+1))

# starting range : 5
# ending range : 9
# 5
# 66
# 777
# 8888
# 99999
# 8888
# 777
# 66
# 5
