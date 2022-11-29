class ans:
    def sub_sets(original, final):
        return original.rec([], sorted(final))
    
    def rec(original, current, final):
        if final:
            return original.rec(current, final[1:]) + original.rec(current + [final[0]], final[1:])
        return [current]


l=set()
n=int(input("Enter number of numbers in list: "))
for i in range(n) : 
    cur=int(input("Enter number : "))
    l.add(cur)

print(ans().sub_sets(l))