#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ryckman Matthieu


# In[2]:


pi = 1
for i in range(1,100000):
    pi *= (4*i**2)/(4*i**2-1)
pi *= 2
pi


# In[3]:


nsd = 12345678912
nb_seconde = nsd
nb_minute = nsd//60
nb_heure = nb_minute//60
nb_jour = nb_heure//24
nb_mois = nb_jour//30
nb_annee = nb_jour//365

seconde = nsd%60
minute = nb_minute%60
heure = nb_heure%24
jour = nb_heure%30
annee = nb_jour%365


print("nombre de secondse totale ", nb_seconde, 
      "nombre de minutes totale ",nb_minute, 
      "nombre de heures totale ",nb_heure, 
      "nombre de jours total ",nb_jour, 
      "nombre de mois total ",nb_mois, 
      "nombre de année totale ",nb_annee )

print(seconde, minute, heure, jour, annee )


# In[4]:


l = [32,5,12,8,3,75,2,15]
pairs = []
impairs = []

for i in l:
    if(i%2 == 0):
        pairs.append(i)
    else: 
        impairs.append(i)
print(pairs)
print(impairs)


# In[5]:


L_mur = 1
l_mur = 3
L_salle = 6.5
l_salle = 5
S = ((L_salle) * (l_salle)) - (L_mur*l_mur) 
S_robot = 120
T_robot = 80
net = (T_robot * S)// 80

print("Le robot nettoiera la salle en ", net, "minutes")


# In[15]:


import turtle as tu


# In[16]:


import turtle as tu
zone_rouge = {"longeur":150, "largeur":500, "couleur":"red"}
zone_blue = {"longeur":500, "largeur":100, "couleur":"blue"}
zone_orange = {"longeur":200, "largeur":100, "couleur":"orange"}
zone_vert = {"longeur":500, "largeur":300, "couleur":"green"}
l = []
l.append(zone_rouge)
l.append(zone_blue)
l.append(zone_orange)
l.append(zone_vert)

tu.penup()
tu.left(90)
tu.fd(200)
tu.left(270)
tu.pendown()

for i in l:
    tu.color(i["couleur"])
    
    if(i["couleur"] == "orange"):
            tu.penup()
            tu.fd(100)
            tu.right(90)
            tu.fd(300)
            tu.left(90)
            tu.pendown()
    
    if(i["couleur"] == "green"):
            tu.penup()
            tu.fd(100)
            tu.left(90)
            tu.fd(300)
            tu.right(90)
            tu.pendown()
   
    tu.begin_fill()
    
    for _ in range(2):
           
        
        tu.forward(i["largeur"])
        if(i["couleur"] == "red"):
            tu.left(90)
        else:
            tu.right(90)
        tu.forward(i["longeur"])
        if(i["couleur"] == "red"):
            tu.left(90)
        else:
            tu.right(90)
    tu.end_fill()
tu.done()
    


# In[38]:


def max(a,b):
    return a if (a>b) else b


# In[39]:


def maxn3(n1,n2,n3):
    return max(max(n1,n2),n3)


# In[40]:


def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)


# In[41]:


def quicksort(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        for x in t[1:]:
            if x<pivot:
                t1.append(x)
            else:
                t2.append(x)
        return quicksort(t1)+[pivot]+quicksort(t2)


# In[ ]:





# In[ ]:




