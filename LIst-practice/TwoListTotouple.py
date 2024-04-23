def two_list_to_dic():
    a = [1,2,3]
    b = ['one', 'two', 'three']

    # converted to dic
    result = dict(zip(a,b))
    print(result)
two_list_to_dic()

def dic_to_tuple():
    x = {1: 'one', 2: 'two', 3: 'three'}
    print(tuple(x.items()))

dic_to_tuple()