#cria esfera
from yade import qt
mat_madeira=CohFrictMat(density=740, #kg/m3
						young= 12.5e6, #Pa 
						poisson=0.25, #adm
						frictionAngle=(34.0/180.0)*3.14, #rad
						label="madeira")

mat_borracha=CohFrictMat(density=1, #kg/m3
						young=0.001e9, #Pa
						poisson=0.5, #adm
						frictionAngle=3.14/4.0, #rad
						label="borracha")
esfera1=sphere(center=(-0.2,0,2),radius=0.1,color=(1,0,0),material=mat_madeira)
esfera2=sphere(center=(0.2,0,2),radius=0.1,color=(0,1,0),material=mat_borracha)
O.bodies.append(esfera1)
O.bodies.append(esfera2)

p1=[-1,1,0]
p2=[-1,-1,0]
p3=[1,-1,0]
p4=[1,1,0]
f1=facet([p1,p2,p4],material=mat_madeira)
f2=facet([p2,p3,p4],material=mat_madeira)
O.bodies.append(f1)
O.bodies.append(f2)

#O.engines contem as os modtores da simulacao
O.engines=[
	#reinicia as forcas
	ForceResetter(),
	#motor que analisa os contatos
	InsertionSortCollider([Bo1_Sphere_Aabb(),Bo1_Facet_Aabb()]),
	# iteracao ptinciais	
	InteractionLoop(
		#modelo de colisao esfera-esfera
		[Ig2_Sphere_Sphere_ScGeom(), Ig2_Facet_Sphere_ScGeom()],
		#material fisico
		[Ip2_FrictMat_FrictMat_FrictPhys()], 
		#modelo de contato inear
		[Law2_ScGeom_FrictPhys_CundallStrack()] 
	),
    #motor de arrasto aerodinamico
	DragEngine(ids=[0,1], Cd=0.47, Rho=10.225),
	#integracao das forcas
	#damping eh o fator de amortecimento	
	NewtonIntegrator(gravity=(0,0,-9.81),damping=0.1),
	PyRunner(command='minhafuncao(arq)',virtPeriod=0.02)
	#qt.SnapshotEngine(fileBase='imgs/img-',virtPeriod=1.0/60.0,label='snap'),
	#VTKRecorder(fileName='vtk/vtk-',recorders=['all'],virtPeriod=1.0/60.0),
]
#calcula o tamanho do passo de tempo
O.dt=.5*PWaveTimeStep()*0.01
# salva o estado da simulacao para reiniciar de necessario
O.saveTmp()

arq = open("dados.csv", "w")



def minhafuncao(arq):
    if O.time<=2.0:
        e1=O.bodies[0]
        e2=O.bodies[1]
        v1=abs(e1.state.vel[2])
        v2=abs(e2.state.vel[2])
        arq.write(str(O.time)+", "+str(v1)+", "+str(v2)+"\n")
    else:
        arq.close()
        O.pause()






