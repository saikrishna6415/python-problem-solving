s = "abcdefghhgfedecba"
s1 = set(s)
dic = { }
for i,k in dic.items():
    dic[s[i]]=s.count(s[i])

print(dic)