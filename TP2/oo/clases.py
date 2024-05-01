from funciones import *
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt


class fuzzy_logic():
    def __init__(self, fmax,pmax,vmax,tipo,defuzzification='centroid'):
        self.fmax = fmax
        self.pmax = pmax
        self.vmax = vmax
        self.tipo = tipo
        self.dom_pos = np.linspace(-self.pmax, self.pmax, self.pmax*20)
        self.dom_vel = np.linspace(-self.vmax, self.vmax, self.vmax*20)
        self.dom_f = np.linspace(-self.fmax, self.fmax, 500)
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
        self.pos_z = vec_medio(-0.25*self.pmax, 0.25*self.pmax, self.dom_pos)
        self.pos_np = vec_medio(-0.5*self.pmax, 0, self.dom_pos)
        self.pos_ng = vec_extremo(-0.5*self.pmax, -0.25*self.pmax, self.dom_pos,'izq')
        self.pos_pp = vec_medio(0, 0.5*self.pmax, self.dom_pos)
        self.pos_pg = vec_extremo(0.25*self.pmax, 0.5*self.pmax, self.dom_pos,'der')
    

        self.vel_z = vec_medio(-0.25*self.vmax, 0.25*self.vmax, self.dom_vel)
        self.vel_np = vec_medio(-0.5*self.vmax, 0, self.dom_vel)
        self.vel_ng = vec_extremo(-0.5*self.vmax, -0.25*self.vmax, self.dom_vel,'izq')
        self.vel_pp = vec_medio(0, 0.5*self.vmax, self.dom_vel)
        self.vel_pg = vec_extremo(0.25*self.vmax, 0.5*self.vmax, self.dom_vel,'der')

        self.fuerza_z = vec_medio(-0.25*self.fmax, 0.25*self.fmax, self.dom_f)
        self.fuerza_np = vec_medio(-0.5*self.fmax, 0, self.dom_f)
        self.fuerza_ng = vec_extremo(-0.5*self.fmax, -0.25*self.fmax, self.dom_f,'izq')
        self.fuerza_pp = vec_medio(0, 0.5*self.fmax, self.dom_f)
        self.fuerza_pg = vec_extremo(0.25*self.fmax, 0.5*self.fmax, self.dom_f,'der')


    def fuzzy(self, pos, vel):
        #fuzzificacion de las variables de entrada

        pz = np.interp(pos, self.dom_pos, self.pos_z)
        pnp = np.interp(pos, self.dom_pos, self.pos_np)
        png = np.interp(pos, self.dom_pos, self.pos_ng)
        ppp = np.interp(pos, self.dom_pos, self.pos_pp)
        ppg = np.interp(pos, self.dom_pos, self.pos_pg)
        # plt.plot(self.dom_pos,self.pos_z)
        # plt.plot(self.dom_pos,self.pos_np)
        # plt.plot(self.dom_pos,self.pos_ng)
        # plt.plot(self.dom_pos,self.pos_pp)
        # plt.plot(self.dom_pos,self.pos_pg)
        # plt.plot(pz,0,'ro')
        # plt.plot(pnp,0,'ro')
        # plt.plot(png,0,'ro')
        # plt.plot(ppp,0,'ro')
        # plt.plot(ppg,0,'ro')
        # plt.show()




        vz = np.interp(vel, self.dom_vel, self.vel_z)
        vnp = np.interp(vel, self.dom_vel, self.vel_np)
        vng = np.interp(vel, self.dom_vel, self.vel_ng)
        vpp = np.interp(vel, self.dom_vel, self.vel_pp)
        vpg = np.interp(vel, self.dom_vel, self.vel_pg)




        # #reglas de inferencia + conjuntos difusos de salida
        # FZ=[min(pert_pos_z, pert_vel_z),min(pert_pos_ng, pert_vel_ng),min(pert_pos_pg,pert_vel_pg)]
        # #FPP=[min(pert_pos_z, pert_pos_np), min(pert_pos_np, pert_vel_pg)]
        # FPP=[min(pert_pos_z, pert_pos_np)]

        # FPG=[min(pert_pos_ng, pert_vel_np),min(pert_pos_ng, pert_vel_z),min(pert_pos_np, pert_vel_ng),min(pert_pos_np,pert_vel_np),min(pert_pos_np, pert_vel_z),min(pert_pos_np, pert_vel_pp),min(pert_pos_z,pert_vel_ng),min(pert_pos_pg, pert_vel_ng),min(pert_pos_pg,pert_vel_np), min(pert_pos_pp, pert_vel_ng)]
        # #FNP=[min(pert_pos_pp, pert_vel_ng),min(pert_pos_z, pert_vel_pp)]
        # FNP=[min(pert_pos_z, pert_vel_pp)]
        # FNG=[min(pert_pos_ng, pert_vel_pp),min(pert_pos_ng, pert_vel_pg),min(pert_pos_z, pert_vel_pg),min(pert_pos_pp, pert_vel_np),min(pert_pos_pp,pert_vel_z),min(pert_pos_pp, pert_vel_pp),min(pert_pos_pp, pert_vel_pg),min(pert_pos_pg,pert_vel_z),min(pert_pos_pg, pert_vel_pp),min(pert_pos_np, pert_vel_pg)]

        cuadro = [
            [min(png,vng),min(pnp,vng),min(pz,vng),min(ppp,vng),min(ppg,vng)],
            [min(png,vnp),min(pnp,vnp),min(pz,vnp),min(ppp,vnp),min(ppg,vnp)],
            [min(png,vz) ,min(pnp,vz) ,min(pz,vz) ,min(ppp,vz) ,min(ppg,vz) ],
            [min(png,vpp),min(pnp,vpp),min(pz,vpp),min(ppp,vpp),min(ppg,vpp)],
            [min(png,vpg),min(pnp,vpg),min(pz,vpg),min(ppp,vpg),min(ppg,vpg)]
        ]

        if self.tipo == 'pendulo':
            rules = [
                ["Z", "PG","PG","PG","PG"],
                ["PG","PG","PP","NG","PG"],
                ["NG","PG","Z" ,"NG","PG"],
                ["NG","PG","NP","NG","NG"],
                ["NG","NG","NG","NG","Z" ]
            ]
        elif self.tipo == 'carrito':
            rules = [
                ["PG","PP","PP","PP","Z"],
                ["PG","PP","PP","Z","NP"],
                ["PG","PP","Z" ,"NP","NG"],
                ["PP","Z","NP","NP","NG"],
                ["Z","NP","NP","NP","NG"]
            ]
        PP=[];PG=[];Z=[];NP=[];NG=[]

        for i in range(5):
            for j in range(5):
                if rules[i][j] == "Z":
                    Z.append(cuadro[i][j])
                elif rules[i][j] == "PP":
                    PP.append(cuadro[i][j])
                elif rules[i][j] == "PG":
                    PG.append(cuadro[i][j])
                elif rules[i][j] == "NP":
                    NP.append(cuadro[i][j])
                elif rules[i][j] == "NG":
                    NG.append(cuadro[i][j])
                    

        #defuzzificacion
        fuerza_z_c = cut(max(Z),self.fuerza_z)
        fuerza_pp_c = cut(max(PP),self.fuerza_pp)
        fuerza_pg_c = cut(max(PG),self.fuerza_pg)
        fuerza_np_c = cut(max(NP),self.fuerza_np)
        fuerza_ng_c = cut(max(NG),self.fuerza_ng)

        fuerza=union([fuerza_z_c,fuerza_pp_c,fuerza_pg_c,fuerza_np_c,fuerza_ng_c])
        

        self.fuerza = defuzz(self.dom_f,fuerza, self.defuzzification)
        # print("\n\nFuerza: ",self.fuerza)

        return fuerza


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
    
    def simular(self,obj,obj2):
        theta = (self.theta * np.pi) / 180
        v_carro = 0
        p_carro = 0
        m_t = self.masa_carro + self.masa_pendulo

        for t in self.x:
            force1 = obj.fuzzy(theta*180/np.pi, self.vel)
            # plt.plot(obj.dom_f,force1)
            # plt.show()
            force2 = obj2.fuzzy(p_carro, v_carro)
            # plt.plot(obj2.dom_f,force2)
            # plt.show()
            force3=union([force1,force2])
            # plt.plot(obj.dom_f,force)
            # plt.show()
            force=defuzz(obj.dom_f,force3,'centroid')
            #force = (force1 + force2) / 2
            a_carro = -force / m_t
            v_carro = v_carro + a_carro * self.delta_t
            p_carro = p_carro + v_carro * self.delta_t + a_carro * np.power(self.delta_t, 2) / 2
            self.velocidad_carro.append(v_carro)
            self.posicion_carro.append(p_carro)
            self.f.append(force)
            self.acel = self.calcula_aceleracion(theta, self.vel,force)
            # print("Tiempo: ",t)
            # print("Posición carro: ",p_carro)
            # print("Fuerza: ",force)
            # print("Velocidad carro: ",v_carro)
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
        fig, ax = plt.subplots(2, 1, sharex=True)
        ax[0].plot(self.x, self.y)
        ax[0].set(ylabel='theta', title='Delta t = ' + str(self.delta_t) + " s")
        ax[0].grid()

        ax[1].plot(self.x, self.posicion_carro)
        ax[1].set(xlabel='time (s)', ylabel='posicion carro')
        ax[1].grid()

        plt.show()