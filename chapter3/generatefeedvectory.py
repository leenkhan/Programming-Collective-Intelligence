#!/usr/bin/python
#coding:utf-8

import feedparser
import re
import jieba
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def getwordcounts(url):
    #解析订阅
    d=feedparser.parse(url)
    wc={}

    #循环遍历所有的文章条目
    for e in d.entries:
        if 'sumary' in e:
            summary = e.summary
        else:
            summary = e.description

        words = getwords(e.title + ' ' +summary)

        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    return d.feed.title,wc

def getwords(html):

    txt = re.compile(r'<[^>]+').sub('',html)

    #words = re.compile(r'[^A-Z^a-z]+').split(txt)

    words = jieba.cut(txt ,cut_all=False, HMM=True)

    return [word.lower() for word in words if word!='']


apcount = {}
wordcount={}
feedlist=[line for line in file('feedlist_cn.txt')]
for feedurl in feedlist:
    title,wc = getwordcounts(feedurl)
    wordcount[title]=wc
    for word,count in wc.items():
        apcount.setdefault(word,0)
        if count>1:
            apcount[word] +=1
print(wordcount)
print(apcount)


wordlist =[]
for w,bc in apcount.items():
    frac = float(bc)/len(feedlist)
    if frac>0.1 and frac<0.5:
        wordlist.append(w)

print(wordlist)

out = file('blogdata_cn.txt','w')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcount.items():
    out.write(blog)
    for word in wordlist:
        if word in wc: out.write('\t%d' % wc[word])
        else: out.write('\t0')
    out.write('\n')
