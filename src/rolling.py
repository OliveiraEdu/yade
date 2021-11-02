h=0.2
y_ext = 2
x_ext = 2

O.materials.append(FrictMat(young=1.7e8,poisson=0.20588,frictionAngle=radians(17),density=2650))
s1=O.bodies.append( utils.sphere([0,-0.7,0.1],.05,color=[0,1,0],fixed=False,wire=True))
s1=O.bodies.append( utils.sphere([0,0.03,0.1],.05,color=[0,1,1],fixed=False,wire=True))


#define quatro pontos formando um quadrado no plano z=0
p1=[-1,1,0]
p2=[-1,-1,0]
p3=[1,-1,0]
p4=[1,1,0]

p1b=[-1,1,0.4]
p2b=[-1,-1,0.4]
p3b=[1,-1,0.4]
p4b=[1,1,0.4]

#Cria faces do chao
fchao=[]
f=facet([p1,p2,p4],wire=False,color=(0,1,0), fixed=True)
fchao.append(f)
f=facet([p2,p3,p4],wire=False,color=(0,1,0), fixed=True)
fchao.append(f)

f=facet([p1,p4,p4b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p1,p4b,p1b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)

f=facet([p2,p1,p2b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p2b,p1,p1b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)

f=facet([p2,p3,p2b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p2b,p3,p3b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)

f=facet([p3,p4,p3b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p3b,p4,p4b],wire=True,color=(1,0,0), fixed=True)
fchao.append(f)


#Adiciona as faces na simulação
O.bodies.append(fchao)

## time step
O.dt=(0.5*PWaveTimeStep())

O.engines=[
        ForceResetter(),
        InsertionSortCollider([Bo1_Sphere_Aabb(),Bo1_Facet_Aabb()]),
        InteractionLoop(
        [Ig2_Facet_Sphere_ScGeom(),Ig2_Sphere_Sphere_ScGeom()],
        [
        Ip2_FrictMat_FrictMat_MindlinPhys(en=0.1, krot=0.24, eta=1)
        ],
        [Law2_ScGeom_MindlinPhys_Mindlin(includeMoment=True),
        ]),
        NewtonIntegrator(damping=0,gravity=(0,0,-9.81)),
]
