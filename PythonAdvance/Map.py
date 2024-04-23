numbers = [1, 2, 3, 4, 5]

# Using map to square each number
squared_numbers = map(lambda x: x**2, numbers)
print(squared_numbers)

nums = (1,2,3,4,5,6)
result = map(lambda x: x+x+x, nums)
print(list(result))

test  = list(map(lambda x: x*x, nums))

test_string_list = ["test123","Test234","test456", "and"]
filtered_ob = list(filter(lambda x :  "test" in x, test_string_list))
print(filtered_ob)


# String formatting

price = 53
text = f"The price is {price} dollars"

text2 = "test is {} "
print(text2.format(price))