# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 02:20:46 2019

@author: wangjingyi
"""


class TableInfo(object):
    def __init__(self):
        self.bland_user = 0
        self.bcur_user = 0
        self.bland_score = 0
        self.bcur_score = 0
        self.bTurnCardCount = 0
        self.bCardCount = [0,0,0]
        self.bOutCardUser = 0
        self.bTurnCardData = []
        
    def parse(self,param):
        land_user = param['land_user']
        cur_user = param['cur_user']
        land_score = param['land_score']
        cur_score = param['cur_score']
        self.bland_user = land_user
        self.bcur_user = cur_user
        self.bland_score = land_score
        self.bcur_score = cur_score
        return
    
    def clear(self):
        self.bland_user = 0
        self.bcur_user = 0
        self.bland_score = 0
        self.bcur_score = 0
        self.bTurnCardCount = 0
        self.bCardCount = [0,0,0]
        self.bOutCardUser = 0
        self.bTurnCardData = []
    
    def getland_user(self):
        return self.bland_user
    
    def getone_farmer_user(self):
        one_farmer_pos = self.bland_user - 1
        if one_farmer_pos < 0:
            one_farmer_pos = 2
        return one_farmer_pos
    
    def gettwo_farmer_user(self):
        two_farmer_pos = self.bland_user + 1
        if two_farmer_pos > 2:
            two_farmer_pos = 0
        return two_farmer_pos
    
    def setlanduser(self,land_user):
        self.bland_user = land_user
    
    def setlandscore(self,land_score):
        self.bland_score = land_score
    
    def setcuruser(self,cur_user):
        self.bcur_user = cur_user
    
    def setoutcard(self,out_card_user,card_count,out_card_data):
        self.bCardCount[out_card_user] += card_count
        self.bOutCardUser = out_card_user
        self.bTurnCardCount = card_count
        self.bTurnCardData = out_card_data.copy()
    
    def getturncardcount(self):
        return self.bTurnCardCount;
    
    def getland_score(self):
        return self.bland_score
    
    def is_new_turn(self):
        if self.bTurnCardCount == 0:
            return True
        else:
            return False
    
    def newturn(self):
        self.bTurnCardCount = 0
        self.bTurnCardData.clear()
    
    def getturncarddata(self):
        return self.bTurnCardData
        
        
        