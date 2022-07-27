def draw_rangoli(size, alfa):
    string = alfa[:size]
    si = size -1
    for i in range(2*size-1):
        j = abs(si-i)
        s2 =  string[j:]
        s1 = s2[::-1]
        s3 =  s1[:-1] +s2
        print('-'.join(s3.center(2*size-1,'-')))

if __name__ == "__main__":
    alfa='أبتثجحخدذرزسشصضطظعغفقكلمنهوي'
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    size = int(input('Enter raduis of rangoli:'))
    if size>=1 and size<=len(alfa):
        draw_rangoli(size, alfa)