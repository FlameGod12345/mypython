def bebra():
    a = input()
    b = []
    for i in a:
        if i.isdigit():
            print(i)
            b.append(i)
    print(b)
bebra()
