from funciones import *
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

class fuzzy_logic():
    def __init__(self, rF,defuzzification='centroid'):
        self.rF = rF
        self.dom_pos = np.linspace(-180, 180, 3600)
        self.dom_vel = np.linspace(-20,20,400)
        self.dom_f = np.linspace(-self.rF, self.rF, 400)
        self.pos_z = None
        self.pos_np = None
        self.pos_ng = None
        self.pos_pp = None
        self.pos_pg = None
        self.vel_z = None
        self.vel_np = None
        self.vel_ng = None
        self.vel_pp = None
        self.vel_pg = None
        self.fuerza_z = None
        self.fuerza_np = None
        self.fuerza_ng = None
        self.fuerza_pp = None
        self.fuerza_pg = None
        self.fuerza = None
        self.defuzzification = defuzzification


    def func_pertenencia(self):
        self.pos_z = vec_medio(-67.5, 67.5, self.dom_pos)
        self.pos_np = vec_medio(-135, 0, self.dom_pos)
        self.pos_ng = vec_extremo(-135, -67.5, self.dom_pos,'izq')
        self.pos_pp = vec_medio(0, 135, self.dom_pos)
        self.pos_pg = vec_extremo(67.5, 135, self.dom_pos,'der')
    

        self.vel_z = vec_medio(-7.5, 7.5, self.dom_vel)
        self.vel_np = vec_medio(-15, 0, self.dom_vel)
        self.vel_ng = vec_extremo(-15, -7.5, self.dom_vel,'izq')
        self.vel_pp = vec_medio(0, 15, self.dom_vel)
        self.vel_pg = vec_extremo(7.5, 15, self.dom_vel,'der')

        self.fuerza_z = vec_medio(-0.375*self.rF, 0.375*self.rF, self.dom_f)
        self.fuerza_np = vec_medio(-0.75*self.rF, 0, self.dom_f)
        self.fuerza_ng = vec_extremo(-0.75*self.rF, -0.375*self.rF, self.dom_f,'izq')
        self.fuerza_pp = vec_medio(0, 0.75*self.rF, self.dom_f)
        self.fuerza_pg = vec_extremo(0.375*self.rF, 0.75*self.rF, self.dom_f,'der')


    def fuzzy(self, pos, vel):
        #fuzzificacion de las variables de entrada
        pert_pos_z = np.interp(pos, self.dom_pos, self.pos_z)
        pert_pos_np = np.interp(pos, self.dom_pos, self.pos_np)
        pert_pos_ng = np.interp(pos, self.dom_pos, self.pos_ng)
        pert_pos_pp = np.interp(pos, self.dom_pos, self.pos_pp)
        pert_pos_pg = np.interp(pos, self.dom_pos, self.pos_pg)

        pert_vel_z = np.interp(vel, self.dom_vel, self.vel_z)
        pert_vel_np = np.interp(vel, self.dom_vel, self.vel_np)
        pert_vel_ng = np.interp(vel, self.dom_vel, self.vel_ng)
        pert_vel_pp = np.interp(vel, self.dom_vel, self.vel_pp)
        pert_vel_pg = np.interp(vel, self.dom_vel, self.vel_pg)

        #reglas de inferencia + conjuntos difusos de salida
        FZ=[min(pert_pos_z, pert_vel_z),min(pert_pos_ng, pert_vel_ng),min(pert_pos_pg,pert_vel_pg)]
        #FPP=[min(pert_pos_z, pert_pos_np), min(pert_pos_np, pert_vel_pg)]
        FPP=[min(pert_pos_z, pert_pos_np)]

        FPG=[min(pert_pos_ng, pert_vel_np),min(pert_pos_ng, pert_vel_z),min(pert_pos_np, pert_vel_ng),min(pert_pos_np,pert_vel_np),min(pert_pos_np, pert_vel_z),min(pert_pos_np, pert_vel_pp),min(pert_pos_z,pert_vel_ng),min(pert_pos_pg, pert_vel_ng),min(pert_pos_pg,pert_vel_np), min(pert_pos_pp, pert_vel_ng)]
        #FNP=[min(pert_pos_pp, pert_vel_ng),min(pert_pos_z, pert_vel_pp)]
        FNP=[min(pert_pos_z, pert_vel_pp)]
        FNG=[min(pert_pos_ng, pert_vel_pp),min(pert_pos_ng, pert_vel_pg),min(pert_pos_z, pert_vel_pg),min(pert_pos_pp, pert_vel_np),min(pert_pos_pp,pert_vel_z),min(pert_pos_pp, pert_vel_pp),min(pert_pos_pp, pert_vel_pg),min(pert_pos_pg,pert_vel_z),min(pert_pos_pg, pert_vel_pp),min(pert_pos_np, pert_vel_pg)]

        #defuzzificacion
        fuerza_z_c = cut(FZ[0],self.fuerza_z)
        fuerza_pp_c = cut(max(FPP),self.fuerza_pp)
        fuerza_pg_c = cut(max(FPG),self.fuerza_pg)
        fuerza_np_c = cut(max(FNP),self.fuerza_np)
        fuerza_ng_c = cut(max(FNG),self.fuerza_ng)

        fuerza=union([fuerza_z_c,fuerza_pp_c,fuerza_pg_c,fuerza_np_c,fuerza_ng_c])

        self.fuerza = defuzz(self.dom_f,fuerza, self.defuzzification)
        # print("\n\nFuerza: ",self.fuerza)

        return self.fuerza


class pendulo():
    def __init__(self, t_max, delta_t, theta,vel ,acel,masa_carro,masa_pendulo,longitud_pendulo):
        self.t_max = t_max
        self.delta_t = delta_t
        self.theta = theta
        self.vel = vel
        self.acel = acel
        self.x = np.arange(0, self.t_max, self.delta_t)
        self.y = []
        self.f = []
        self.masa_carro = masa_carro
        self.masa_pendulo = masa_pendulo
        self.longitud_pendulo = longitud_pendulo
        self.posicion_carro = []
        self.velocidad_carro = []


    def calcula_aceleracion(self,theta, v,f): 
        # f=anashe(theta*180/np.pi,v*180/np.pi)
        fuerza=-f
        numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-fuerza - self.masa_pendulo * self.longitud_pendulo * np.power(v, 2) * np.sin(theta)) / (self.masa_carro + self.masa_pendulo))
        denominador = self.longitud_pendulo * (4/3 - (self.masa_pendulo * np.power(np.cos(theta), 2) / (self.masa_carro + self.masa_pendulo)))
        return numerador / denominador
    
    def simular(self,obj):
        theta = (self.theta * np.pi) / 180
        v_carro = 0
        p_carro = 0
        m_carro = self.masa_carro

        for t in self.x:
            force = obj.fuzzy(theta*180/np.pi, self.vel)
            a_carro = force / m_carro
            v_carro = v_carro + a_carro * self.delta_t
            p_carro = p_carro + v_carro * self.delta_t + a_carro * np.power(self.delta_t, 2) / 2
            self.velocidad_carro.append(v_carro)
            self.posicion_carro.append(p_carro)
            self.f.append(force)
            self.acel = self.calcula_aceleracion(theta, self.vel,force)
            # print("Tiempo: ",t)
            #print("angulo: ",theta*180/np.pi)
            #print("velocidad: ",self.vel)
            if abs(self.vel)>20:
                print("engine caput")
                pass
            # time.sleep(0.1)
            self.vel = self.vel + self.acel * self.delta_t
            theta = theta + self.vel * self.delta_t + self.acel * np.power(self.delta_t, 2) / 2
            if theta > np.pi:
                theta = theta - 2 * np.pi
            elif theta < -np.pi:
                theta = theta + 2 * np.pi
            self.y.append(theta*180/np.pi)

    def graficar(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)

        ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(self.delta_t) + " s")
        ax.grid()
        
        plt.show()
        