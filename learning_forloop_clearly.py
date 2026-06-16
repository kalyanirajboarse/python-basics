# for loop learning

number_list = [1, 2, "hh", "678", 980, "fyi", [3,66,876]]

# for i in number_list:
#     print(i)


# print(number_list[1])
# print(number_list[2])
# print(number_list[3])
# print(number_list[4])
# print(number_list[5])

for num in number_list:
    if type(num)==int:
        continue

    
    print(num[-1])

