#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 12:05:53 2018

@author: koushikahamed
"""

class infixTopostfix:
    def __init__(self):
        self.input="9-5+2."
        self.Inputlength=len(self.input)
        self.position=0
        self.lookahead=self.input[self.position]
        
    def expr(self):
        self.term()
        self.rest()
        
    def term(self):
        if self.lookahead.isdigit():
            print(self.lookahead)
            self.position+=1
            self.lookahead=self.input[self.position]
        
    def match(self,operator):
        if self.lookahead==operator:
            self.position+=1
            self.lookahead=self.input[self.position]
            
    def rest(self):
        if self.lookahead=='+':
            self.match("+")
            self.term()
            print ("+")
            self.rest()
        elif self.lookahead=="-":
            self.match('-')
            self.term()
            print('-')
            self.rest()
            
if __name__=="__main__":
    ip=infixTopostfix()
    ip.expr()
