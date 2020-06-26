#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:08:33 2020

@author: rishabhagarwal
"""


from opencage.geocoder import OpenCageGeocode
key = 'fed8a93c5b1a4352b1ca47d70a478188'
import math
class Distance2():
    def __init__(self):
        geocoder = OpenCageGeocode(key)
        self.q = input('City and Country you want to travel to [London, England]: ')
        result2 = geocoder.geocode(self.q)
        self.lat2 = result2[0]['geometry']['lat']
        self.long2 = result2[0]['geometry']['lng']
        self.g = input('City and Country you are currently in: ')
        result = geocoder.geocode(self.g)
        self.lat = result[0]['geometry']['lat']
        self.long = result[0]['geometry']['lng']
        self.earthrad = 3958.8
        self.currentcity = self.g
        self.othercity = self.q
    def distancefinder(self):
        self.latdiff = (self.lat2-self.lat)*(3.1415/180)
        self.longdiff = (self.long2-self.long)*(3.1415/180)
        self.latrad = self.lat*3.1415/180
        self.latrad2 = self.lat2*3.1415/180
        self.a = (math.sin(self.latdiff)*math.sin(self.latdiff))+((math.cos(self.latrad))*(math.cos(self.latrad2))*(math.sin(self.longdiff)))
        self.c = 2*math.atan2(math.sqrt(self.a),math.sqrt(1-self.a))
        self.distance = self.earthrad*self.c
        print(f'Distance is {self.distance}')
        
        
        
        
        
