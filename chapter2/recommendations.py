#!/usr/bin/python
#coding:utf-8
from math import sqrt

critics ={'Lisa Rose':{'Lady in the Water':2.5, 'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman  Returns':3.5,
                       'You, Me and Dupress':2.5,'The night Listener':3.0},
          'Gene Seymour':{'Lady in the Water':3.0, 'Snakes on a Plane':3.5,'Just My Luck':1.5,'Superman  Returns':5.0,
                       'You, Me and Dupress':3.5,'The night Listener':3.0},
          'Michael Phillips':{'Lady in the Water':2.5, 'Snakes on a Plane':3.0,'Superman  Returns':3.5,
                       'The night Listener':4.0},
          'Claudia Puig':{ 'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman  Returns':4.0,
                       'The night Listener':4.5,'You, Me and Dupress':2.5},
          'Mick LaSalle':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0,'Just My Luck':2.0,'Superman  Returns':3.0,
                       'You, Me and Dupress':2.0,'The night Listener':3.0},
          'Jack Matthews':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0,'Just My Luck':2.0,'Superman  Returns':5.0,
                       'You, Me and Dupress':3.5,'The night Listener':3.0},
          'Toby':{'Snakes on a Plane':4.5,'Just My Luck':2.0,'Superman  Returns':4.0,'You, Me and Dupress':1.0}
          }


#返回person1和person2的基于距离的相似度评价
def sim_distance(prefs, person1, person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    if len(si)==0: return 0

    sum_of_squares=sum(pow(prefs[person1][item] - prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2])

    return 1/(1+sqrt(sum_of_squares))




#返回p1和p2的皮尔逊相关系数
def sim_pearson(prefs, p1, p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    n=len(si)

    if n==0: return 1

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2sq=sum([pow(prefs[p2][it],2) for it in si])

    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    num=pSum - (sum1*sum2/n)
    den=sqrt((sum1sq-pow(sum1, 2)/n)*(sum2sq-pow(sum2, 2)/n))
    if den==0: return 0

    r=num/den

    return r

def topMatches(perfs, person, n=5, similarity=sim_pearson):
    scores=[(similarity(perfs, person, other),other) for other in perfs if other!=person]

    scores.sort()
    scores.reverse()
    return  scores[0:n]