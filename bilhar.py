#cria material físico
#density: kg/m³ - densidade do material
#young: Pa - módulo de Young, resistência do material, relaciona pressão com defomação
#poisson: adimensional - Coeficiente de Poisson, relaciona deformação em dois eixos
#frictionAngle: radianos - Ângulo de fricção interno
mat_madeira1=CohFrictMat(density=550,young=1.1e11,poisson=0.25,frictionAngle=0.4712,label="mat1")



#cria esfera isolada
esfera1=sphere(center=(0,-1.95,0.45),color=(1,1,1),radius=0.05,material=mat_madeira1,fixed=False,wire=True)

#cria esferas em triangulo
esfera2=sphere(center=(0,0.03,0.05),color=(1,0,1),radius=0.05,material=mat_madeira1,fixed=False,wire=True)
esfera3=sphere(center=(-0.05,0.13,0.05),color=(0,1,1),radius=0.05,material=mat_madeira1,fixed=False,wire=True)
esfera4=sphere(center=(0.05,0.13,0.05),color=(0,1,0),radius=0.05,material=mat_madeira1,fixed=False,wire=True)
esfera5=sphere(center=(0,0.23,0.05),color=(1,1,0),radius=0.05,material=mat_madeira1,fixed=False,wire=True)
esfera6=sphere(center=(-0.10,0.23,0.05),color=(0,0,1),radius=0.05,material=mat_madeira1,fixed=False,wire=True)
esfera7=sphere(center=(0.10,0.23,0.05),color=(1,0,0),radius=0.05,material=mat_madeira1,fixed=False,wire=True)

O.bodies.append(esfera1)
O.bodies.append(esfera2)
O.bodies.append(esfera3)
O.bodies.append(esfera4)
O.bodies.append(esfera5)
O.bodies.append(esfera6)
O.bodies.append(esfera7)

#define quatro pontos formando um quadrado no plano z=0
p1=[-1,1,0]
p2=[-1,-2,0]
p3=[1,-2,0]
p4=[1,1,0]

p1b=[-1,1,0.4]
p2b=[-1,-2,0.4]
p3b=[1,-2,0.4]
p4b=[1,1,0.4]

p5=[1,-0.7,0]
p6=[-1,-0.7,0]


#Cria faces do chao
fchao=[]
f=facet([p1,p2,p4],wire=False,material=mat_madeira1,color=(0,1,0), fixed=True)
fchao.append(f)
f=facet([p2,p3,p4],wire=False,material=mat_madeira1,color=(0,1,0), fixed=True)
fchao.append(f)

f=facet([p1,p4,p4b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p1,p4b,p1b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)

f=facet([p2,p1,p2b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p2b,p1,p1b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)

f=facet([p2,p3,p2b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p2b,p3,p3b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)

f=facet([p3,p4,p3b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)
f=facet([p3b,p4,p4b],wire=True,material=mat_madeira1,color=(1,0,0), fixed=True)
fchao.append(f)


#Cria rampa
f3=facet([p2b,p3b,p5],wire=False,material=mat_madeira1,color=(0,0,1))
f4=facet([p5,p6,p2b],wire=False,material=mat_madeira1,color=(1,0,1))

#Adiciona as faces na simulação
O.bodies.append(fchao)

O.bodies.append([f3,f4])

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
	#integracao das forcas
	#damping eh o fator de amortecimento
	NewtonIntegrator(gravity=(0,0,-9.81),damping=0.1),
	PyRunner(command='minhafuncao(arq)',virtPeriod=0.1)
]
#calcula o tamanho do passo de tempo
O.dt=(0.5*PWaveTimeStep())
# salva o estado da simulacao para reiniciar de necessario
O.saveTmp()


arq = open("dados.csv", "w")

def minhafuncao(arq):
    e1=O.bodies[0]
    e2=O.bodies[1]
    v1=abs(e1.state.vel[2])
    v2=abs(e2.state.vel[2])
    arq.write(str(O.time)+", "+str(v1)+", "+str(v2)+"\n")
