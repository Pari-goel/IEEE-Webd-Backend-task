dictionary = dict()
n = int(input("How many elements do you want? "))
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    dictionary[k]=[v]

def keys_ascending():
    for a in sorted(dictionary):
        print((a, dictionary[a]), end=" ")

def values_ascending():
    dict1={}
    for a in sorted(dictionary.values()):
        for i in dictionary.keys():
            if dictionary[i] == a:
                dict1[i]=dictionary[i]
    print(dict1)

print("dictionary sorted by keeping keys in ascending order")
keys_ascending()
print("dictionary sorted by keeping values in ascending order")
values_ascending()
