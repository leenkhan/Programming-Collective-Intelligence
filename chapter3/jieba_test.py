#!/usr/bin/python
#coding:utf-8
import jieba
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("我爱吃黄焖鸡米饭",cut_all=True, HMM=False)
print("全模式:"+ "/ ".join(seg_list))

seg_list = jieba.cut("我爱吃黄焖鸡米饭",cut_all=False, HMM=True)
print("默认模式:"+ "/ ".join(seg_list))

seg_list = jieba.cut("我爱吃黄焖鸡米饭",HMM=False)
print("默认模式:"+ "/ ".join(seg_list))