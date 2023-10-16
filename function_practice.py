def hello():
    print("Hello user!")

def pack(var1,var2,var3):
    list_values = [var1,var2,var3]
    return list_values

def eat_lunch(input):
    if len(input) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(input)):
            if i == 0:
                print(f"first I eat my {input[0]}")
            else:
                print(f"Next I eat {input[i]}")

hello()
print(pack("dog", "cat", "duck"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwhich"])
eat_lunch(["hot dog", "burger", "fries", "shake"])