# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:21:23 2016

@author: abc
"""

class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23),User(10),User(3)]

print users
print sorted(users, key=lambda u:u.user_id)
from operator import attrgetter 
##可多欄位
print sorted(users,key=attrgetter('user_id'))
print min(users,key=attrgetter('user_id'))
print max(users,key=attrgetter('user_id'))