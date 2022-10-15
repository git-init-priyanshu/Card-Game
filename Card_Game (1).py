#############################################################################################

import random

import time

import os

#############################################################################################

os.system('cls')

print("Loading.",end="")#animation lol

for i in range(5):
     time.sleep(0.8)
     print(".",end="")

os.system('cls')

print()
print()
time.sleep(0.5)
print("              |CARDS|")
time.sleep(2)
print()

#############################################################################################

deck=[]
l=[]
temp=[]##line 245,246

for i in range(1,12):#for random no. of cards from 1 to 11
    for j in range(random.randint(1,5)):
        l.append(i)
        temp.append(i)

for i in range(6):
    l.append("A")
    l.append("J")
    
for i in range(len(l)):#shuffle 
    j=random.randint(0,len(l)-1)
    deck.append(l[j])
    l.pop(j)

aim =21

#############################################################################################

def show():
     print("Hoffmann's deck")
     for z in oc.c:
          for j in range(3):
               if j==1:
                    print(z,end=" ")
               else:
                    print("|",end=" ")                    
     print("     ",oc.sum_c,"/",aim)
     print()
     
     print("Your deck")
     for y in op.p:
          for j in range(3):
               if j==1:
                    print(y,end=" ")
               else:
                    print("|",end=" ")
     print("     ",op.sum_p,"/", aim)
     print()


def fun():     
    #if oc.inp_c=='no' and op.inp_p=='no':##win conditions
        for i in op.p:
            op.sum_p+=i
        for i in oc.c:
            oc.sum_c+=i

        if op.sum_p>oc.sum_c and op.sum_p<aim and oc.sum_c<aim:             
            time.sleep(0.8)
            print()
            print()
            print("Lucas: And the winner is...")
            time.sleep(2)
            print()
            print("...Clancy...")
            time.sleep(0.8)
            print(show())
            
        elif oc.sum_c>op.sum_p and op.sum_p<aim and oc.sum_c<aim:             
            time.sleep(0.8)
            print("Lucas: And the winner is...")
            time.sleep(2)
            print()
            print("...Hoffmann...")
            time.sleep(0.8)
            print(show())
            
        elif op.sum_p>oc.sum_c and op.sum_p>aim and oc.sum_c<aim:             
            time.sleep(0.8)
            print("Lucas: And the winner is...")
            time.sleep(2)
            print()
            print("...Hoffmann...")
            time.sleep(0.8)
            print(show())
            
        elif oc.sum_c>op.sum_p and op.sum_p<aim and oc.sum_c>aim:             
            time.sleep(0.8)
            print("Lucas: And the winner is...")
            time.sleep(2)
            print()
            print("...Clancy...")
            time.sleep(0.8)
            print(show())
            
        elif oc.sum_c>aim and op.sum_p>aim:             
            if (op.sum_p)-(oc.sum_c)<0:
                time.sleep(0.8)
                print("Lucas: And the winner is...")
                time.sleep(2)
                print()
                print("...Clancy...")
                time.sleep(0.8)
                print(show())
                
            elif (op.sum_p)-(oc.sum_c)>0:                 
                time.sleep(0.8)
                print("Lucas: And the winner is...")
                time.sleep(2)
                print()
                print("...Hoffmann...")
                time.sleep(0.8)
                print(show())
                
        elif oc.sum_c==op.sum_p:             
             time.sleep(0.8)
             print("Lucas: Well played, It's a draw")
             time.sleep(0.8)
             print()
             print(show())

#############################################################################################

class player:
    
    def __init__(self):

        self.p=[]
        self.trump_p=[]
        self.sum_p=0
        self.inp_p='y'

    def funtrump_p(self):

        if self.inp_p=='A':
            print("|A|")
            for i in self.trump_p:
                if i=='A':
                    time.sleep(0.8)
                    if len(self.p)>1:
                        self.p.pop(-1)
                        self.trump_p.pop(i)
                        print("Lucas:Clancy used his trump card")
                        
                        op.display_p()
                        print()
                        oc.display_c()
                    else:
                        print("Lucas:What do you want?")
                else:
                    time.sleep(0.8)
                    print("Lucas:You don't have one")
            
        elif self.inp_p=='J':
            print("|J|")
            for i in self.trump_p:
                if i=='J':
                    time.sleep(0.8)
                    if len(self.c)>1:
                        self.c.pop(-1)
                        self.trump_p.pop(i)
                        print("Lucas:Clancy used his trump card")
                        
                        op.display_p()
                        print()
                        oc.display_c()
                    else:
                        print("Lucas:What do you want?")
                else:
                    time.sleep(0.8)
                    print("Lucas:You don't have one")
    
    def getcard_p(self):

        #print()
        b=0
        while b<1:#invalid input glitch
            
            #print()
            self.inp_p=input('input: ')

            if self.inp_p=='help':
                print()
                print("   type 'inv' to see your trump cards")
                print("   to use trump card type 'A' or 'J' ")
                print("   want a card? type 'y' or 'n' ")
                print()

                time.sleep(5)###
                os.system('cls')
                display()

            elif self.inp_p=='A' or self.inp_p=='J':
                op.funtrump_p()
                oc.getcard_p()#another turn
            
            elif self.inp_p=='inv':    
                if len(self.trump_p)==0:
                    print("___")
                    print()

                    time.sleep(2)###
                    os.system('cls')
                    display()
                    
                elif len(self.trump_p)!=0:
                    for i in range(len(self.trump_p)):
                        for j in range(3):
                            if j==1:
                                 print(self.trump_p,end='')
                            else:
                                 print('|',end='')
                                 
                    time.sleep(2)###
                    os.system('cls')
                    display()
                                 
            elif  self.inp_p=='y':

                os.system('cls')
                display()

                #print()
                #print()
                print("Clancy: Hit me")
                time.sleep(1)
                self.p.append(deck[random.randint(0,len(deck)-1)])

                if self.p[-1]=='A' or self.p[-1]=='J':
                    print('Lucas:lucky you Clancy you got a trump card')
                    self.trump_p.append(self.p[-1])
                    self.p.pop(-1)

                time.sleep(2)###
                os.system('cls')
                display()#    

                b=2#to break the loop
                    
            elif self.inp_p=='n':

                os.system('cls')
                display()

                #print()
                #print()
                print("Clancy:I'am gonna stay")
                time.sleep(1)

                time.sleep(2)###
                os.system('cls')
                display()#
                
                b=2#to break the loop
                            
    def display_p(self):

        #print("Your cards:      ",end=" ")#display cards
        print("                           ",end="")
        for i in range(len(self.p)):
            for j in range(3):
                if j==1:
                    print(self.p[i],end='')
                else:
                    print('|',end='')

        for i in self.p:#display sum
            self.sum_p+=i
        print("     ",self.sum_p,"/",aim)
        self.sum_p=0        
    
class computer:

    def __init__(self):

        self.c=[]
        self.trump_c=[]
        self.sum_c=0
        self.inp_c='y'

    def funtrump_c(self):
        
        if self.inp_c=='A':
            print("|A|")## bug
            for i in self.trump_c:
                if i=='A':
                    time.sleep(0.8)
                    print()##
                    print(self.c)##
                    self.c.pop(-1)##bug
                    self.trump_c.pop(i)
                    print("Lucas:Hoffmann used his trump card")
                    
                    op.display_p()
                    print()
                    oc.display_c()                   
                else:
                    time.sleep(0.8)
                    print("Lucas:You don't have one")
            
        elif self.inp_c=='J':
            print("|J|")
            for i in self.trump_c:
                if i=='J':
                    time.sleep(0.8)
                    self.p.pop(-1)
                    self.trump_c.pop(i)
                    print("Lucas:Hoffmann used his trump card")
                    
                    op.display_p()
                    print()
                    oc.display_c()
                else:
                    time.sleep(0.8)
                    print("Lucas:You don't have one")

    def getcard_c(self):

        ch=int

        for i in range(len(self.c)):
            self.sum_c+=self.c[i]

        #print()
        for i in (self.trump_c):#risk taking factor
            if i=='A':
                ch=1
            else:
                ch=0

        if self.sum_c<=13:
            self.inp_c='y'
            
        elif self.sum_c<=15:
            if ch==1:
                self.inp_c='y'
            else:
                if random.randint(1,100)>=20:
                    self.inp_c='y'
                else:
                    self.inp_c='n'

        elif self.sum_c==16:
            if ch==1:
                self.inp_c='y'
            else:
                if random.randint(1,100)>=75:
                    self.inp_c='y'
                else:
                    self.inp_c='n' 

        elif self.sum_c==17:
            if ch==1:
                self.inp_c='y'
            else:
                if random.randint(1,100)>=90:
                    self.inp_c='y'
                else:
                    self.inp_c='n'

        elif self.sum_c>17:
            if ch==1:
                self.inp_c='y'
            else:
                self.inp_c='n'

        elif self.sum_c==21:
            self.inp_c='n'

        if self.sum_c>21:
            if ch==1:
                self.inp_c='A'
                oc.funtrump_c()
                oc.getcard_c()#another turn

        if self.inp_c=='y':
            print("Hoffmann: Hit me")
            time.sleep(1)
            self.c.append(deck[random.randint(0,len(deck)-1)])
            if self.c[-1]=='A' or self.c[-1]=='J':
                    print('Lucas:lucky you Hoffmann you got a trump card')
                    self.trump_c.append(self.c[-1])
                    self.c.pop(-1)
                    oc.getcard_c()

            time.sleep(2)###
            os.system('cls')
            display()#

        elif self.inp_c=='n':
                print("Hoffmann:I'am gonna stay")
                time.sleep(1)

        if self.inp_c=='n':
            for i in self.trump_c:
                if i=='J':                    
                    if random.randint(1,100)>=10:
                        self.inp_c='J'
                        oc.funtrump_c()
                        oc.getcard_c()#another turn
                        break

            time.sleep(2)###
            os.system('cls')
            display()#

        self.sum_c=0
                               
    def display_c(self):

        #print("Hoffmann's cards:",end=" ")
        print("                           ",end="")
        for i in range(len(self.c)):
            for j in range(3):
                if j==1:
                    if i!=0:
                        print(self.c[i],end='')
                    else:
                        print("?",end='')
                else:
                    print('|',end='')

        for i in range(len(self.c)):
            self.sum_c+=self.c[i]
            s=self.sum_c-self.c[0]
        print("    ? +",s,"/",aim)

        self.sum_c=0

#############################################################################################

def display():#UI

        print("*" * 80)
        print()
        oc.display_c()
        for i in range(8):
            print()
        op.display_p()
        print()
        print("*" * 80)

#time.sleep(2)

#############################################################################################

op=player()##object

oc=computer()##object

for i in range(2):##all get 2 cards(excluding trump)
    op.p.append(temp[random.randint(0,len(temp)-1)])
    oc.c.append(temp[random.randint(0,len(temp)-1)])

os.system('cls')#to clear the terminal

#display()

while True:##newly added loop

        display()
        
        if op.inp_p!='n':
            op.getcard_p()
            #print()
            #op.display_p()

        if oc.inp_c!='n':
            oc.getcard_c()
            #print()
            #oc.display_c()

        if op.inp_p=='n' and oc.inp_c=='n':
            print()
            time.sleep(1)
            fun()
            break
        
        os.system('cls')#to clear the terminal
