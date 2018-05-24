#!/usr/bin/python
#coding:utf-8
from math import sqrt

critics ={'Lisa Rose':{'Lady in the Water':2.5, 'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman  Returns':3.5,
                       'You, Me and Dupress':2.5,'The night Listener':3.0},
          'Gene Seymour':{'Lady in the Water':3.0, 'Snakes on a Plane':3.5,'Just My Luck':1.5,'Superman  Returns':5.0,
                       'You, Me and Dupress':3.5,'The night Listener':3.0},
          'Michael Phillips':{'Lady in the Water':2.5, 'Snakes on a Plane':4.0,'Just My Luck':1.5,'Superman  Returns':3.5,
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