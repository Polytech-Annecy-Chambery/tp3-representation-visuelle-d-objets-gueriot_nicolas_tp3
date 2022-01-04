# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Opening import Opening

class Section:
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
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    def generate(self):
        # Définie tous les points à partir des paramètres
        self.vertices = [
                # Point A
                self.parameters['position'], 
                # Point E
                [self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2] + self.parameters['height']],
                # Point F
                [self.parameters['position'][0] + self.parameters['width'], self.parameters['position'][1], self.parameters['position'][2] + self.parameters['height']],
                # Point B
                [self.parameters['position'][0] + self.parameters['width'], self.parameters['position'][1], self.parameters['position'][2]],
                # Point D
                [self.parameters['position'][0], self.parameters['position'][1] + self.parameters['thickness'], self.parameters['position'][2]],
                # Point H
                [self.parameters['position'][0], self.parameters['position'][1] + self.parameters['thickness'], self.parameters['position'][2] + self.parameters['height']],
                # Point G
                [self.parameters['position'][0] + self.parameters['width'], self.parameters['position'][1]+self.parameters['thickness'], self.parameters['position'][2] + self.parameters['height']],
                # Point C
                [self.parameters['position'][0] + self.parameters['width'], self.parameters['position'][1]+self.parameters['thickness'],self.parameters['position'][2] ]
                ]
        
        # Définie toutes les faces
        self.faces = [
                [0,3,2,1], # Face AEFB
                [0,4,5,1], # Face ADHE
                [4,7,6,5], # Face DCGH
                [3,7,6,2], # Face BCGF
                [0,3,7,4], # Face ABCD
                [1,2,6,5]  # Face EFGH            
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        
        # compare la largeur total de l'ouverture à la largeur total de la section
        if x.getParameter("position")[0] + x.getParameter("width") > self.parameters["position"][0] + self.parameters["width"]:
            return False
        
        # compare la hauteur total de l'ouverture à la largeur hauteur de la section
        elif x.getParameter("position")[2] + x.getParameter("height") > self.parameters["position"][2] + self.parameters["height"]:
            return False
        
        # compare la position en x de l'ouverture à la position en x de la section
        elif x.getParameter("position")[0]< self.parameters["position"][0] :
            return False
        
        # compare la position en z de l'ouverture à la position en z de la section
        elif x.getParameter("position")[2] < self.parameters["position"][2]:
            return False
        
        # sinon on retourne True
        else:
            return True
        
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        
        sections= [] # Creation d'une liste de section
        
        # Creation de la section 1 en indiquant les paramètres
        section1 = Section(
            {
                "position":     self.parameters["position"], 
                "width":        x.getParameter("position")[0], 
                "height":       self.parameters["height"],
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
        
        # Vérifie si la taille n'est pas nulle
        if section1.parameters["width"] > 0 :
            sections.append(section1)
        
        # Creation de la section 2 en indiquant les paramètres
        section2 = Section(
            {
                "position":     [self.parameters['position'][0] + x.getParameter("position")[0],self.parameters['position'][1],self.parameters['position'][1] + x.getParameter("position")[2]+x.getParameter("height")], 
                "width":        x.getParameter("width"), 
                "height":       self.parameters["height"]-x.getParameter("height")-x.getParameter("position")[2],
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
        
        # Vérifie si la taille n'est pas nulle
        if section2.parameters["height"] > 0 :
            sections.append(section2)

        # Creation de la section 3 en indiquant les paramètres
        section3 = Section(
            {
                "position":     [self.parameters['position'][0] + x.getParameter("position")[0],self.parameters['position'][1],self.parameters['position'][1]], 
                "width":        x.getParameter("width"), 
                "height":       x.getParameter("position")[2],
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
        
        # Vérifie si la taille n'est pas nulle
        if section3.parameters["height"] > 0 :
            sections.append(section3)
        
        
        # Creation de la section 4 en indiquant les paramètres
        section4 = Section(
            {
                "position":     [self.parameters['position'][0] + x.getParameter("position")[0]+x.getParameter("width"),self.parameters['position'][1],self.parameters['position'][1]], 
                "width":        self.parameters["width"]-x.getParameter("width")-x.getParameter("position")[0], 
                "height":       self.parameters["height"],
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
        
        # Vérifie si la taille n'est pas nulle
        if section4.parameters["width"] > 0 :
            sections.append(section4)
        
        return sections
    
    
    # Draws the edges
    def drawEdges(self):
       
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on Trace des arêtes : GL_LINE
        gl.glBegin(gl.GL_QUADS)# Tracé d'un quadrilatère
        
        
        for y in self.faces:
            
            facteur = 0.5 #défini la couleur des arêtes
                       
            gl.glColor3fv([0.5 * facteur, 0.5 * facteur, 0.5 * facteur]) # Couleur
                
            for i in range(0,4):

                x = y[i]
                gl.glVertex3fv(self.vertices[x])    #Tracé des vertices
        
                
        
        gl.glEnd()           
                    
    # Draws the faces
    def draw(self):

        if self.parameters['edges'] == True :
            self.drawEdges()    # Tracé des bordures

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS)# Tracé d’un quadrilatère
        
        for y in self.faces:
            
            gl.glColor3fv(self.getParameter("color")) # Couleur
            
            for i in range(0,4):
                x = y[i]
                gl.glVertex3fv(self.vertices[x]) #Tracé des vertices
        
        
        gl.glEnd()
        

  