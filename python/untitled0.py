# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:20:16 2019

@author: praveen
"""

x=int(input("please enter any value"))
if x<=0:
    print("this is a negative number")
elif x == 1:
    print("single")
else:
    print("positive and greater than 1")


courses=['html','c','java','css']
for i in courses:
    print(i, len(i))


digit=['125000']
for i in digit:
    print(i, len(i))
 
for i in range(10):
    if (i==4 or i ==8):
        continue
    print(i)
    ####here 4 and 8 are not printed because in if satement as we passed when 4 and 8 iterations comes we use continue statement
            ## means when ever the iteartion flows and comes to 4 it says continue to next loop 
            #dont execute the current loop 


for x in "python":
    if x == "o":
        break
    print(x)  ###Here we have defined a sting to pass that is "python"
                ##  and in if statemnt we have given "o" value when iteration come at "o" we said that "break" 
                # means to stop the compilation at that point so we get ouput as "pyth"
                


x=int(input("give some value"))
while x<10:
    x=x+1
    print(x)
    

for i in range(10,20):
    if (i%2 == 0):
        continue
    print(i, 'is a odd number')



for i in range(100,104):##[values are 100,101,103,102]
    print("assinged value of i is", i)  #[100 is taken and printed]
    for num in range(100,i): #[as we have given num in range 100,i   here i is 100. 100,100 ]
        print(i,num)  #[loop 2 comes here i is 101 num is 100 because i is the value which the current loop value is running]
        if num == 102:
            pass
range(100,104)


        ###### here we have given range(100,104) for i means betweem 100 to  103 are the i values 
        ## itreation starts from here loop 1 starts range value 100 is taken and prints the print statement with 100 as
        ## value  and continues 