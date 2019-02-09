'''
Created on Dec 12, 2018

@author: coditum
'''


def ftoc(ftemp):
    coutput=(ftemp-32)/1.8
    return coutput

def celciustof(celciusinput):
    farenheitoutput=(1.8*celciusinput)+32
    return farenheitoutput



def userinput():
    corf=int(input('1 for ftoc, 2 for ctof'))
    tempinput=int(input('Input temp to convert'))
    return corf, tempinput
    
corf, tempinput = userinput()
if corf==1:
    x=ftoc(tempinput)
if corf==2:
    x=celciustof(tempinput)


print(x)