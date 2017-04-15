#coding=utf-8

import re
'''
@author:Ellie Smith
@Create Date:April 15
@Description: Soundex Algo

'''
#----  P140 38  ----

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


#----  P140 39  ----

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
    string = raw_input('请输入一个英文名:')
    if re.findall('[^A-Za-z]',string):
        print '非法字符输入:',re.findall('[^A-Za-z]',string)
        continue
    string = string.lower()
    if len(string)>1:
        # 如果两个或多个相同号码的字母在原始名称中相邻,只保留一个字母
        step1 = [string[i] for i in range(1,len(string)) \
                 if (string[i] not in dict or string[i-1] not in dict or dict[string[i]] != dict[string[i-1]])]
        #将辅音转换成对应的数字
        step1 = map(filter_char, step1)
        # 两个以“h”或“w”分隔的相同数字的字母被编码为单个数字，
        step2 = step1[:2]
        if len(step1)>2:
            for i in range(2,len(step1)):
                if (step1[i-1] =='h' or step1[i-1] == 'w') and step1[i] == step1[i-2]:
                        continue
                else:
                    step2.append(step1[i])
        else:
            step2 = step1
        result = re.sub('[aeiouyhw]','',string[0].upper()+''.join(step2))[:4]
        if len(result) < 4:
            result+='0'*(4-len(result))
        print result
    else:
        print string

