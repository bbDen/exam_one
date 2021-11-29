
a=['hello',5,'john']
def new_list(a):
    b=['Element','start','finish']
    a.insert(0,b[0])
    a.insert(1,b[1])
    a.insert(len(a),b[-1])
    print(a)
new_list(a)


l = ['x', 5, 'John', 'honey']
lenght = len(l)
def new_dict(lenght):
    a = {}
    for i in range(lenght):
        a[l[i]] = i + 1
    print(a)


new_dict(lenght)
def new_list(a, b):
    l = []
    c = []
    for i in a:
        if i % 2 == 0:
            l.append(i)
    for j in b:
        k = pow(j, 2)
        c.append(k)
    return c, l


a_1 = [1, 2, 3, 4, 5]
b_1 = [1, 2, 3, 4, 5]
a, b = new_list(a_1, b_1)
print(a)
print(b)




