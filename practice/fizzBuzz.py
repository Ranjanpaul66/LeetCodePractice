def fizBuz(n):
    d = {3 : 'fizz',4 :'buzz' }
    for i in range(1, n+1):
        result = ""

        for k,v in d.items():
            if(i%k==0):
                result =v
        if not result:
            result=i
        print(result)

fizBuz(15)
