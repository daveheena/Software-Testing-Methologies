# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 19:23:54 2017

@author: Heena
"""

def parser(s):
    if not type(s) is str:
        return None
    elif len(s) < 1:
        return None
    else:
        power = 0
        decimal = False
        n = 0
        power2 = 0
        negative_number = False
        try:
            if float(s) < 0:
                negative_number = True
                s = s[1:]
                
            if float(s) < 1:
                for c in s:
                    if c == '.' and decimal == False:
                        decimal = True
                    elif decimal == True and '0' <= c <= '9':
                        if(n == 0):
                            power = power - 1
                        
                        if n == 0:
                            n = int(c) / 1.0
                            if n!= 0:
                                power2 = power2 - 1
                        else:
                            n = n + int(c) * pow(10,power2)
                            power2 = power2 - 1
                            
                    else:
                        continue
                
            else:
                for c in s:
                    if c == '.' and decimal == False:
                        decimal = True
                    elif n == 0:
                        n = int(c) / 1.0
                    elif '0' <= c <= '9' and decimal == False:
                        power = power + 1
                        n = n + int(c) * pow(10,-power)
                    else:
                        if power2 == 0:
                            power2 = power + 1
                        else:
                            power2 = power2 + 1
                        n = n + int(c) * pow(10,-power2)
            
            if negative_number:
                return "-" + str(n) + " * 10^" + str(power)    
            else:
                return "" + str(n) + " * 10^" + str(power)
            
            
        except ValueError:
            return None