mat_madeira1=CohFrictMat(density=550,young=1.1e11,poisson=0.25,frictionAngle=0.4712,label="mat1")

#O.materials.append(FrictMat(young=1.7e8,poisson=0.20588,frictionAngle=radians(17),density=2650))
s1=O.bodies.append( utils.sphere([0,-0.7,0.05],.05,color=[1,1,0],fixed=False,wire=True,material=mat_madeira1))
s1=O.bodies.append( utils.sphere([0,0.03,0.05],.05,color=[1,0,1],fixed=False,wire=True,material=mat_madeira1))
s1=O.bodies.append( utils.sphere([-0.05,0.13,0.05],.05,color=[0,1,1],fixed=False,wire=True,material=mat_madeira1))
s1=O.bodies.append( utils.sphere([0.05,0.13,0.05],.05,color=[0,1,0],fixed=False,wire=True,material=mat_madeira1))

#define quatro pontos formando um quadrado no plano z=0
p1=[-1,1,0]
p2=[-1,-1,0]
p3=[1,-1,0]
p4=[1,1,0]

p1b=[-1,1,0.4]
p2b=[-1,-1,0.4]
p3b=[1,-1,0.4]
p4b=[1,1,0.4]



## time step
O.dt=1e-4

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
