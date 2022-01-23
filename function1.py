a = input('[a]: ')
b = input('[b]: ')
if len(a) and len(b) == 1:
    print('[a]: ', a, '=',ord(a))
    print('[b]: ', b, '=',ord(b))
    print(('[a] + [b]: '), ord(a), '+', ord(b), '=', ord(a) + ord(b))
