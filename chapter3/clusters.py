#!/usr/bin/python
#coding:utf-8
from math import sqrt
from PIL import Image,ImageDraw
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class bicluster:
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance

def readfile(filename):
    lines = [line for line in file(filename)]
    #第一行是标题
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p=line.strip().split('\t')
        #没一行的第一列是行名
        #rowname = p[0]
        rownames.append(p[0])
        #剩余的部分是数据
        data.append([float(x) for x in p[1:]])
    return rownames,colnames,data

def pearson(v1,v2):
    #求和
    sum1 = sum(v1)
    sum2 = sum(v2)

    #求平方和
    sum1sq = sum([pow(v,2) for v in v1])
    sum2sq = sum([pow(v,2) for v in v2])

    #求乘积之和
    pSum = sum([v1[i]*v2[i] for i in range(len(v1))])

    #计算 r (pearson score)
    num = pSum - (sum1*sum2/len(v1))
    den = sqrt((sum1sq - pow(sum1,2)/len(v1))) * (sum2sq-pow(sum2,2)/len(v1))
    if den==0: return 0
    return 1.0-num/den



def hcluster(rows, distance=pearson):
    distances = {}
    currentclustid = -1

    clust =[bicluster(rows[i],id=i) for i in range(len(rows))]

    while len(clust)>1:
        lowestpair = (0,1)
        closest = distance(clust[0].vec, clust[1].vec)

        for i in range(len(clust)):
            for j in range(i+1,len(clust)):
                if(clust[i].id, clust[j].id) not in distances:
                    distances[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)

                d = distances[(clust[i].id, clust[j].id)]
                if d < closest:
                    closest = d
                    lowestpair=(i,j)

        mergevec = [(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0
                    for i in range(len(clust[0].vec))]

        newcluster = bicluster(mergevec,left=clust[lowestpair[0]],
                               right=clust[lowestpair[1]],
                               distance=closest,id=currentclustid)

        currentclustid -=1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)
    return clust[0]

def printclust(clust, labels=None, n=0):
    for i in range(n): print('   '),
    if clust.id<0:
        print('-')
    else:
        if labels==None: print( clust.id)
        else: print(labels[clust.id])

    if clust.left!=None: printclust(clust.left,labels=labels,n=n+1)
    if clust.right!=None: printclust(clust.right,labels=labels,n=n+1)

def getheight(clust):
    if clust.left==None and clust.right==None: return  1

    return getheight(clust.left)+getheight(clust.right)

def getdepth(clust):
    if clust.left==None and clust.right==None: return 0;

    return max(getdepth(clust.left), getdepth(clust.right)) + clust.distance

def drawnode(draw,clust,x,y,scaling,labels):
    if clust.id<0:
        h1=getheight(clust.left)*20
        h2=getheight(clust.right)*20
        top=y-(h1+h2)/2
        bottom=y+(h1+h2)/2

        l1=clust.distance*scaling
        draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0))

        draw.line((x,top+h1/2,x+l1,top+h1/2),fill=(255,0,0))

        draw.line((x,bottom-h2/2,x+l1,bottom-h2/2),fill=(255,0,0))

        drawnode(draw,clust.left,x+l1,top+h1/2,scaling,labels)
        drawnode(draw,clust.right,x+l1,bottom-h1/2,scaling,labels)
    else:
        draw.text((x+5,y-7),labels[clust.id],(0,0,0))


def drawdendrogram(clust,labels,jpeg='clusters.jpg'):
    h = getheight(clust)*25
    w = 1200
    depth = getdepth(clust)

    scaling = float(w-150)/depth

    img = Image.new('RGB',(w,h), (255,255,255))
    draw = ImageDraw.Draw(img)
    draw.line((0,h/2,10,h/2),fill=(255,0,0))
    drawnode(draw,clust,10,(h/2),scaling,labels)
    img.save(jpeg,'JPEG')

def rotatemaxtrix(data):
    newdata = []
    for i in range(len(data[0])):
        newrow=[data[j][i] for j in range(len(data))]
        newdata.append(newrow)
    return  newdata

if __name__ == '__main__':
    blognames,words,data = readfile("blogdata_cn.txt")
    # print(blognames)
    # print(words)
    # print(data)
    clust = hcluster(data)
    printclust(clust,labels=blognames)
    drawdendrogram(clust,blognames,jpeg='blogclust_cn.jpg')
    #rdata = rotatemaxtrix(data)
    #wordclust = hcluster(rdata)
    #drawdendrogram(wordclust, labels=words,jpeg='wordclust_cn.jpg')