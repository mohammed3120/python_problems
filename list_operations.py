if __name__ == '__main__':
    N = int(input('Insert the number of instractions that you want to run:'))
    l = []
    for ins in range(N):
        string = str(input())
        inst = string.split(' ')
        if inst[0] == 'insert':
            i = int(inst[1])
            e = int(inst[2])
            l.insert(i, e)
        elif inst[0] == 'print':
            print(l)
        elif inst[0] == 'remove':
            e = int(inst[1])
            l.remove(e)
        elif inst[0] == 'append':
            e = int(inst[1])
            l.append(e)
        elif inst[0] == 'sort':
            l.sort()
        elif inst[0] == 'pop':
            l.pop()
        elif inst[0] == 'reverse':
            l.reverse()
        else:
            print('wrong')
            continue
         