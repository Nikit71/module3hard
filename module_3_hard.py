#       Дополнительное практическое задание по модулю: "Подробнее о функциях."
#       Задание "Раз, два, три, четыре, пять .... Это не всё?"

def calculate_structure_sum(*args):
    res=0
    for i in range(len(args)):
        k=args[i]
        typ_k = type(k)
        if typ_k  == set:
            k = list(k)
            typ_k = type(k)
        if typ_k  == int:
            res = res + k
        elif typ_k == str:
            res = res + len(k)
        elif typ_k == set:
            res = res + calculate_structure_sum(list(k))
        elif typ_k == dict:
            res = res + calculate_structure_sum(list(k.items()))
        elif typ_k == tuple or typ_k == list:
            for j in range(len(k)):
                res = res + calculate_structure_sum(k[j])
    return res
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]) ]
result = calculate_structure_sum(*data_structure)
print(result)
