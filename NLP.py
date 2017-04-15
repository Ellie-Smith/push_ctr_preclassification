#coding=utf-8

import re
import nltk

# f = open('text.txt','r')
# lines = f.readlines()
# s = ''.join(lines)
# print s
#
# reg = re.compile(' \w*-\n\w* ')
# print reg.findall(s)
#
# s = re.sub('-\n','-',s)
#
# print s

dict = {'b':'1', 'f':'1', 'p':'1', 'v':'1',
        'c':'2', 'g':'2', 'j':'2', 'k':'2', 'q':'2', 's':'2', 'x':'2', 'z':'2',
        'd':'3', 't':'3',
        'l':'4',
        'm':'5', 'n':'5',
        'r':'6'
        }
def filter_char(x):
    if x in dict:
        return dict[x]
    else:
        return x

while 1:
    string = raw_input('input a string:')
    string = string.lower()
    if len(string)>1:
        tail1 = []
        #如果两个或多个相同号码的字母在原始名称中相邻,只保留一个字母
        for i in range(1,len(string)):
            if string[i] in dict and string[i-1] in dict \
                and dict[string[i]] == dict[string[i-1]]:
                    continue
            else:
                tail1.append(string[i])
        #将辅音转换成对应的数字
        tail1 = map(filter_char, tail1)
        # 两个以“h”或“w”分隔的相同数字的字母被编码为单个数字，
        tail2 = tail1[:2]
        if len(tail1)>2:
            for i in range(2,len(tail1)):
                if (tail1[i-1] =='h' or tail1[i-1] == 'w') and tail1[i] == tail1[i-2]:
                        continue
                else:
                    tail2.append(tail1[i])
        else:
            tail2 = tail1[:]
        result = re.sub('[aeiouyhw]','',string[0].upper()+''.join(tail2))[:4]
        if len(result) < 4:
            result+='0'*(4-len(result))
        print result
    else:
        print string

