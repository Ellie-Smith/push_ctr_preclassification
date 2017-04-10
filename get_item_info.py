#coding=utf-8
import json
import urllib2

def getNLP_info(item):
    # 获取文章id
    item_id = item

    essayUrl = 'http://napi.ucweb.com/3/classes/recoitem/objects/%s?_app_id=2c1629d6b19741f88a86cc23de5203eb&_fetch=1'%(str(item_id))

    try:
        essay = urllib2.urlopen(essayUrl).read()
        essay_content = json.loads(essay)
    except:
        print essayUrl
        raise Exception("Url not found")

    keyword_feature = essay_content['data']['nlp_info']['keyword']['feature']
    title = essay_content['data']['raw_item']['title']


    #获取关键词
    keywords = [keyword['literal'] for keyword in keyword_feature]

    return ','.join(keywords),title

def getDataList(path):
    f = open(path, 'r')
    criticalItems = []
    line = f.readline()
    while line:  # 读取数据构建标准
        items = line.split()
        criticalItems.append(items)
        line = f.readline()
    f.close()
    # print 'item_list.txt:  ', criticalItems
    return criticalItems

if __name__ == '__main__':
    list = getDataList('item_list.txt')
    for i in list:
        keywords,title = getNLP_info(int(i[0]))
        print title
