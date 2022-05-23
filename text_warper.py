from re import sub
def wrap(string, max_width):
    result = ''
    for i in range(0, len(string),max_width):
        result += string[i:i+max_width]+'\n'
    print(result)




if __name__=="__main__":
    wrap('ABCDEFGHIJKLMNOPRS', 4)
