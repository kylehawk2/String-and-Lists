words = "It's thanksgiving day. It's my birthday,too!"
print words.replace("day", "month")
x = [2, 54, -2, 7, 12, 98]
print min(x), max(x)
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[::len(x)-1]
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
print x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
print "first_list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list