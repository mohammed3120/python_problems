def wrap(string, max_width):
    result = ''
    for i in range(0, len(string),max_width):
        result += string[i:i+max_width]+'\n'
    print(result)
import textwrap
def text_wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width= max_width)
  
    word_list = wrapper.wrap(text = string)
    for line in word_list:
        print(line)




if __name__=="__main__":
    wrap('ABCDEFGHIJKLMNOPRS', 4)
    text_wrap('ABCDEFGHIJKLMNOPRS', 4)
