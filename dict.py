# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)



# d = { }
# for i in range(1,16):
#     d.update({i : i**2})
# print(d)


# d1 = {1:"sai",2:"krishna"}
# d2 = {3:"kittu"}
# d = d1.copy()
# d.update(d2)
# print(d)


# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', value) 


# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))


# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))

# my_dict = {'x':500, 'y':5874, 'z': 560}

# mmax = max(my_dict.values())
# mmin = min(my_dict.values())

# print('Maximum Value: ',mmax)
# print('Minimum Value: ',mmin)


# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)

# unival = [ ]
# for i in L:
#     for dic in i.values():
#         unival.append(dic)
# print(set(unival))

# place = ["tlk","chpd","knr","hyd"]

# for i in place:
#     print(hash(i))



# s = "ifailuhkqq"
# s1 = { }
# for i in range(len(s)):
#     s1.update({s[i] : s.count(s[i])})
# print(s1)

# buckets = {}
#     for i in range(len(s)):
#         for j in range(1, len(s) - i + 1):
#             key = frozenset(Counter(s[i:i+j]).items())
#             buckets[key] = buckets.get(key, 0) + 1
#         count = 0
#     for key in buckets:
#         count += buckets[key] * (buckets[key]-1) // 2
#     return count  

arr = [10,-5,6]
left = [ ]
right = [ ]
count = 0
for i in range(len(arr)):
    left.append(arr[i+1:])
    right.append(arr[:i])
print(left,right)
for  i in range(len(arr)):
    if sum(left[i])>sum(right[i]):
        count+=1
print(count)
