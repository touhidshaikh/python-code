#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author : Touhid M Shaikh
# Website : www.touhidshaikh.com
# Description : This is my first python module. This module helps you to color your stings in your program. Hassell free approach to color you stings without remembering any color code . just type font style, Foreground color and Background color name only. 
# Date : March 24, 2017
# Version : 1.0

def reset():
    r = "\033[0m"
    return r

def colorbyint(style,foreground,background):

    r = "\033["+str(style)+";"+str(foreground)+";"+str(background)+"m"
    return r

def colorbyname(style,foreground,background):
    style = style.lower()
    foreground = foreground.lower()
    background = background.lower()

    s = {"normal":0,"bold":1,"faint":2,"italic":3,"underline":4,"blink":5}
    fg = {"black":30,"red":31,"green":32,"yellow":33,"blue":34,"purple":35,"cyan":36,"white":37}
    bg = {"black": 40, "red": 41, "green": 42, "yellow": 44, "blue": 44, "purple": 45, "cyan": 46, "white": 47}

    style = str(s.get(style,"0"))
    foreground = str(fg.get(foreground,"37"))
    background = str(bg.get(background,"40"))

    r = "\033[" +style+ ";" +foreground+ ";" +background+ "m"

    return r



def colorstring(style,foreground,background,string):
    style = style.lower()
    foreground = foreground.lower()
    background = background.lower()
    string = str(string)


    s = {"normal":0,"bold":1,"faint":2,"italic":3,"underline":4,"blink":5}
    fg = {"black":30,"red":31,"green":32,"yellow":33,"blue":34,"purple":35,"cyan":36,"white":37}
    bg = {"black": 40, "red": 41, "green": 42, "yellow": 44, "blue": 44, "purple": 45, "cyan": 46, "white": 47}


    style = str(s.get(style,"0"))
    foreground = str(fg.get(foreground,"37"))
    background = str(bg.get(background,"40"))

    r = "\033[" +style+ ";" +foreground+ ";" +background+ "m"+string+"\033[0m"

    return r


