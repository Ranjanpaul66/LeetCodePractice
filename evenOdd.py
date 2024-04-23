def evn_or_odd(n):
    if n / 2 != 0:
        print("Weird")
    elif n / 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n / 2 == 0 and n >= 6 and n <= 20:
        print("Wired")
    elif n / 2 == 0 and n > 20:
        print("Not Wired")


if __name__ == '__main__':
    n = int(input().strip())
    evn_or_odd(24)

