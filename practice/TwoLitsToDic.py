def listToDic():
    list = [1,2,3]
    list2 = ['One', 'two', 'Three', 'g']
    dic = dict(zip(list, list2))
    return dic

print(listToDic())