# Q.1- create a string and save it in a another variable as reverse of original string.

str_0 = "i am trying to learn python myself"
#        0123456789
# ['i',' ','a','m',' ','t','r','y','i','n','g',' ','t','o',' ','l','e','a','r','n',' ','p','y','t','h','o','n',' ','m','y','s','e','l','f']
#   0   1   2   3   4   5   6   7   8   9  10  11  12  13     
#       s   b       b       b       b      b     b                    
# print(str_0[0:22:-1])
# print(str_0[::-2])
# print(str_0[5])
# print(len(str_0))

# print(str_0[:1])
# print(str_0[:-1])
# print(str_0[:0:-1])

# print(str(str_0[len(str_0)-1])+str(str_0[len(str_0)-2])+str(str_0[len(str_0)-3]))

print(str_0[1:10:2])

center_of_str_0 = int(len(str_0)/2)

first_half_of_str_0 = str_0[0:center_of_str_0]

second_half_of_str_0 = str_0[center_of_str_0:int(len(str_0))]

print("first half of str_0 :- ", first_half_of_str_0)
print("second half of str_0 :- ", second_half_of_str_0)