#Count
def freq_word():
    str1 = "Hello Ranjan, how are you I love your Coding style. Hello Monisha, how are you I love your Cooking style."

    list_words = str1.replace(".", "").replace(",","").split()
    dic = {}

    for i in list_words:
        if i not in dic.keys():

            dic[i] = 0
        dic[i] = dic[i]+1
    print(dic)

freq_word()