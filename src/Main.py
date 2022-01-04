# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening


def Q1a():
    return Configuration()
    
def Q1b_f():
    return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}). \
        setParameter('xAxisColor', [1, 1, 0]). \
        setParameter('yAxisColor', [0,1,1])
        
def Q2b():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
            ) 

def Q2c():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True})
            )

def Q3a():
    return Configuration().add(Wall({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True}))

def Q4a():
    # Ecriture en utilisant des variables : A compléter
    wall1 = Wall({'position': [0, 0, 0]   , 'width':7, 'height':2.6,'orientation': 0, 'edges': True})
    wall2 = Wall({'position': [0, 4.8, 0]   , 'width':7, 'height':2.6,'orientation': 0, 'edges': True})
    wall3 = Wall({'position': [0, 0, 0]   , 'width':5, 'height':2.6,'orientation': 90, 'edges': True})
    wall4 = Wall({'position': [0.2, -7, 0]   , 'width':4.6, 'height':2.6,'orientation': 90,'edges': True})
    house = House({'position': [-3, 1, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    return Configuration().add(house)

    
def Q5a():  
    # Ecriture avec mélange de variable et de chaînage    
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
    return Configuration().add(opening1).add(opening2)
    
def Q5b():  
    # Ecriture avec mélange de variable et de chaînage   
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    print(section.canCreateOpening(opening1))
    print(section.canCreateOpening(opening2))    
    print(section.canCreateOpening(opening3))
    return Configuration()    
    
def Q5c1():      
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    sections = section.createNewSections(opening1)
    configuration = Configuration()
    for x in sections:
        configuration.add(x)    
    return configuration     
    
def Q5c2():      
    section = Section({'width':7, 'height':2.6})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    sections = section.createNewSections(opening2)
    configuration = Configuration()
    for section in sections:
        configuration.add(section)    
    return configuration    

def Q5d():      
    
    wall1 = Wall({"position":[0,0,0], 'width':7, 'height':2.6})
    
    doorFrame1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    windowFrame1 = Opening({'position': [4, 0, 1.25], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    wall1.add(doorFrame1)
    wall1.add(windowFrame1)

    configuration = Configuration()
    configuration.add(wall1)

    return configuration
    
def Q6():  
    
    wall1 = Wall({'position': [0, 0, 0] , 'width':7, 'height':2.6,'orientation': 0})
    
    door1 = Door({'position': [2, 0.1, 0],'color': [0.6, 0.6, 0]})
    window1 = Window({'position': [4, 0.1, 1.25],'color': [0.8, 1, 1]})
    
    doorFrame1 = Opening({'position': [0, -0.1, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.4, 0.4, 0.4]})
    windowFrame1 = Opening({'position': [0, -0.1, 0], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.4, 0.4, 0.4]})
    door1.add(doorFrame1)
    window1.add(windowFrame1)
    
    wall1.add(door1)
    wall1.add(window1)
    
    wall2 = Wall({'position': [0, 4.8, 0]   , 'width':7, 'height':2.6,'orientation': 0, 'edges': True})
    wall3 = Wall({'position': [0.2, -0.2, 0]   , 'width':4.6, 'height':2.6,'orientation': 90, 'edges': True})
    wall4 = Wall({'position': [0.2, -7, 0]   , 'width':4.6, 'height':2.6,'orientation': 90,'edges': True})
    house = House({'position': [0, 0, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    
    return Configuration().add(house)

def Q7():  
    
    wall1 = Wall({'position': [0, 0, 0] , 'width':7, 'height':2.6,'orientation': 0})
    
    door1 = Door({'position': [2, 0.1, 0],'color': [0.6, 0.6, 0]})
    window1 = Window({'position': [4, 0.1, 1.25],'color': [0.8, 1, 1]})
    
    doorFrame1 = Opening({'position': [0, -0.1, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.4, 0.4, 0.4]})
    windowFrame1 = Opening({'position': [0, -0.1, 0], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.4, 0.4, 0.4]})
    door1.add(doorFrame1)
    window1.add(windowFrame1)
    
    wall1.add(door1)
    wall1.add(window1)
    
    wall2 = Wall({'position': [0, 4.8, 0]   , 'width':7, 'height':2.6,'orientation': 0, 'edges': True})
    wall3 = Wall({'position': [0.2, -0.2, 0]   , 'width':4.6, 'height':2.6,'orientation': 90, 'edges': True})
    wall4 = Wall({'position': [0.2, -7, 0]   , 'width':4.6, 'height':2.6,'orientation': 90,'edges': True})
    house = House({'position': [0, 0, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    house2= House({'position': [-7, 0, 0], 'orientation':0})
    house2.add(wall1).add(wall3).add(wall4).add(wall2)
    
    return Configuration().add(house).add(house2)
 
def main():
    # Enlever un des commentaires pour la question traitée
    
    #configuration = Q1a()
    #configuration = Q1b_f()
    #configuration = Q2b()
    #configuration = Q2c()
    #configuration = Q3a()
    #configuration = Q4a()
    #configuration = Q5a()
    #configuration = Q5b()
    #configuration = Q5c1()
    #configuration = Q5c2() 
    #configuration = Q5d()
    #configuration = Q6()
    #configuration = Q7()
    
    configuration.display()     
         
# Calls the main function
if __name__ == "__main__":
    main()    