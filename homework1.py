def print_paramets(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = (47, 'Sergei', 'Yaroslevl')
values_list2 = (2024, "Года")
values_dick = {'a':28_01_1977, 'b':"student", 'c':"Urban"}
print_paramets(1, b = 25, c = [1,2,3])
print_paramets(*values_list)
print_paramets(**values_dick)
print_paramets(*values_list2, 42)