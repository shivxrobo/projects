def change_list_to_matrix(*list_):
    fox = [list_]
    mat = []
    mat.append(list_)
    return mat

list_1 = ['Shivam',23,"@#44"]
list_2 = ["Rajive",4565,44]
X = change_list_to_matrix(list_1,list_2)
print(X)
for row in X:
    print(type(row))

    