#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Matthieu Ryckman M2 Data Science


# In[28]:


#Import nécéssaire
from math import *
import numpy as np


# In[8]:


#EXO1
print("Entrez la valeur du rayon  : ")
r = int(input())
print("Entrez la valeur de la hauteur : ")
h = int(input())
v = (pi*(r*r)*h)/3
print("Le volume du cone est de ", v, "m³")


# In[25]:


#EXO2
while True:
    print("Entrez un entier strictement positif  : ")
    n = int(input())
    if n > 0:
        break
l = [] 

for i in range(2,n):
    if (n%i) == 0:
        l.append(i)

if l != []:
    print("Diviseurs propres sans répétition de ",n," : ",l,"soit",len(l),"diviseurs propres")
else: 
    print("Diviseurs propres sans répétition de ",n," : aucun ! Il est premier" )


# In[51]:


#EXO3

while True:
    print("Entrez un entier strictement sup à 50  : ")
    c = int(input())
    if c > 50:
        break


prox_e = 0;

for n in range(c):
    prox_e+= (1/factorial(n))


e = 2.71828182846

tab = []
tab.append(e)
tab.append(prox_e)
print(tab)


# In[67]:


#EXO4
def valide(adn):
   if adn == "":
       return False
   for i in adn:
       if i != "a" and i !="t" and i!="g" and i!="c":
           return False
   
   return True


def saisie():
   while True:
       adn = input()
       if valide(adn):
           break
   return adn


def proportion(adn, seq):
   deb = 0
   fin = len(seq)
   cpt = 0
   
   while (fin < len(adn)):
       if (adn[deb:fin] == seq):
           cpt+=1
       deb += 1
       fin += 1
       
   per = cpt/len(adn)
   return per*100

chaine = saisie()
print("chaine: ")
print("séquence: : ")
seq = input()
per = proportion(chaine, seq) 

print("Il y a ", per, " % de ", seq, "dans votre chaine.")
   
      
  


# In[71]:


#Exo5
def minMaxMoy(l):
    l2 = []
    l2.append(min(l))
    l2.append(max(l))
    l2.append(sum(l) / len(l))
    return l2


minMaxMoy([10,18,14,20,12,16])   


# In[86]:


#EXO6 
def Ave_cesar(num):
        v = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        s = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // v[i]):
                roman_num += s[i]
                num -= v[i]
            i += 1
        return roman_num
u = int(input())
Ave_cesar(u)


# In[89]:


#EXO7

def maFonction(x):
    return 2*(x*x*x)+x-5

def tabuler(f,bi,bs,p):
    if bi > bs:
        return -1000000000
    for i in range(bi,bs,p):
        print(f(i))

tabuler(maFonction,1,90,12)


# In[98]:


#EXO8
X = {'a','b','c','d'}
Y = {'s','b','d'}
'c' in X
'a' in Y
X.difference(Y)
Y.difference(X)
X.union(Y)
X.intersection(Y)


# In[100]:


#EXO9 En cours
dico = {"Au": 
       {"TE/TF":(2970,1063),"NM atomique":(79,196.967)}},
        ""


# In[ ]:


#EXO10

