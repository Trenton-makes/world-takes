'''
Created on Nov 13, 2018

@author: wickm
'''
def main():
    numbers=open('numbers_list.txt', 'r')
    goose=numbers.readline()
    maverick = 0
    while goose != '':
        
        goose=numbers.readline()
        jester=int(goose)
        maverick=maverick+jester
        print(maverick)

    numbers.close()

  
main()