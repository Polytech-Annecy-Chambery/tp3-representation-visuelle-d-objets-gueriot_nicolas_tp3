# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
         self.vertices = [
                [0,0,0], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                
                [0, self.parameters['thickness'], 0 ], 
                [0, self.parameters['thickness'], self.parameters['height']], 
                [self.parameters['width'],  self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'],  self.parameters['thickness'], 0]
                ]
         self.faces = [
                [0, 1, 5, 4],
                [0, 3, 7, 4],
                [1, 2, 6, 5],
                [3, 2, 6, 7]
                ]
            
    def drawEdges(self):
       
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # On trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé de ligne
        
        
        for y in self.faces:
            
            facteur = 0.5 #défini la couleur des arêtes
                       
            gl.glColor3fv([0.5 * facteur, 0.5 * facteur, 0.5 * facteur]) # Couleur
                
            for i in range(0,4):

                x = y[i]
                gl.glVertex3fv(self.vertices[x]) # Tracé des vertices
                
        
        gl.glEnd()
                  
    def draw(self):        
        
        gl.glPushMatrix() # Crée une matrice de projection temporaire
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # On trace les faces : GL_FILL
        gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2]) # Translate l'ouverture
        
        for f in self.faces:
            gl.glBegin(gl.GL_QUADS) # Trace un quadrilatère
            gl.glColor3fv(self.parameters['color']) # Couleur
            for e in f : 
                gl.glVertex3fv(self.vertices[e]) # Trace les vertices
            gl.glEnd()
        self.drawEdges()
        gl.glPopMatrix() # Termine la matrice de projection temporaire
        