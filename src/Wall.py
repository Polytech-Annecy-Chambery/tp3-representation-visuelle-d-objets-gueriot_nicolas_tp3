# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section
from copy import deepcopy

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]
            
        # Objects list
        self.objects = []

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color'],
                                      'position': self.parameters['position']})
        self.objects.append(self.parentSection) 
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self                 

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
    
    # Adds an object    
    def add(self, x):    
        section = self.findSection(x) # Cherche la section
        
        # Calcule de la position relative entre l'ouverture et la section
        position_Relative = [
            x.parameters["position"][0] - (section[1].getParameter("position")[0]),
            x.parameters["position"][1] - (section[1].getParameter("position")[1]),
            x.parameters["position"][2] - (section[1].getParameter("position")[2]),
        ]
        
        
        self.objects.append(x)  # Ajoute l'ouverture
        
        newopening= deepcopy(x) # Copie profonde afin de ne pas modifier x
        
        # On change la position de la nouvelle ouverture en fonction de la position relative
        newopening.setParameter("position", position_Relative) 
        
        #On crée une nouvelle liste de sections contenant les sections nouvellement crées
        new_Sections = section[1].createNewSections(newopening)
        
        self.objects.pop(section[0]) # On supprime la section original
        
        # On ajoute toutes les nouvelles sections
        for i in new_Sections:      
            self.objects.append(i)
        return self    
                    
    # Draws the faces
    def draw(self):
        
        gl.glPushMatrix() # Crée une matrice de projection temporaire
        gl.glRotatef(self.parameters['orientation'], 0, 0, 1)   # Oriente le mur
        self.parentSection.drawEdges() # Trace les arêtes
        for x in self.objects:
            x.draw()    # Appele la méthode draw de section
        gl.glPopMatrix() # Termine la matrice de projection temporaire
  