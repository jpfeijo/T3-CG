
from Ponto import Ponto
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

class Bezier:
    def __init__NEW(self, p0:Ponto, p1:Ponto, p2:Ponto):
        print ("Construtora da Bezier")
        self.ComprimentoTotalDaCurva = 0.0
        self.Coords = []
        self.Coords += [p0]
        self.Coords += [p1]
        self.Coords += [p2]
        #P = self.Coords[0]
        #P.imprime()

    def __init__(self, *args:Ponto):
        #print ("Construtora da Bezier")
        self.ComprimentoTotalDaCurva = 0.0
        self.Coords = []
        #print (args)
        for i in args:
            self.Coords.append(i)
        #P = self.Coords[2]
        #P.imprime()

    def Calcula(self, t):
        UmMenosT = 1-t
        P = Ponto()
        P = self.Coords[0] * UmMenosT * UmMenosT + self.Coords[1] * 2 * UmMenosT * t + self.Coords[2] * t*t
        return P

    def Traca(self):     
        t=0.0
        DeltaT = 1.0/50
        P = Ponto
        glBegin(GL_LINE_STRIP)
        
        while(t<1.0):
            P = self.Calcula(t)
            glVertex2f(P.x, P.y)
            t += DeltaT
        P = self.Calcula(1.0) #faz o acabamento da curva
        glVertex2f(P.x, P.y)
        
        glEnd()

    def calculaComprimento(self):
        deltaT = 1/50
        t = deltaT
        p1 = self.Calcula(0)
        comprimentoTotal = 0
        while t < 1:
            p2 = self.Calcula(t)
            comprimentoTotal += math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
            p1 = p2
            t += deltaT
        
        p2 = self.Calcula(1)
        comprimentoTotal += math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        print(comprimentoTotal)
        return 1.2
    

           
            