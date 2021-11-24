# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

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
        # A compléter en remplaçant pass par votre code
        pass      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
       
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS)# Tracé de ligne
        
        
        for y in self.faces:
            
            facteur = 0.5
                       
            gl.glColor3fv([0.5 * facteur, 0.5 * facteur, 0.5 * facteur])
                
            for i in range(0,4):

                x = y[i]
                gl.glVertex3fv(self.vertices[x])
                
        
        gl.glEnd()           
                    
    # Draws the faces
    def draw(self):

        if self.parameters['edges'] == True :
            self.drawEdges()

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS)# Tracé d’un quadrilatère
        
        for y in self.faces:
            
            
            gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
            
            for i in range(0,4):
                x = y[i]
                gl.glVertex3fv(self.vertices[x])
        
        
        gl.glEnd()
        

  