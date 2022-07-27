from re import sub


def count_substring(string, sub_string):
    count_i = 0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:len(sub_string)+i] == sub_string:
            count_i +=1
    return count_i


if __name__=="__main__":
    s = "MoMohammedMoMoMed"
    sub_string = 'MoM'
    print(count_substring(s, sub_string))
