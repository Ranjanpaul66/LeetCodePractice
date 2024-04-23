def common_letters():
    s1 ="Ranjan Paul"
    s2 = "Monisha Paul"

    s1 = set(s1.replace(" ", ""))
    print(s1)
    s2 = set(s2.replace(" ", ""))
    print(s2)

    print(len(s1 & s2))


common_letters()