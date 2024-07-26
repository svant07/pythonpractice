def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    #print(a, b)
    #print()

values_list = [5, 'Hello', [6, 7, 8]]
values_dict = {'a':16, 'b':True, 'c':'cat'}
values_list_2 = [54.32, 'Строка' ]
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
