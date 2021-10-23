#cria esfera
esfera1=sphere(center=(-0.5,0,2),color=(1,1,1),radius=0.1)
esfera2=sphere(center=(0.5,0,2),color=(1,1,1),radius=0.1)
O.bodies.append([esfera1,esfera2])

#cria material físico
#density: kg/m³ - densidade do material
#young: Pa - módulo de Young, resistência do material, relaciona pressão com defomação
#poisson: adimensional - Coeficiente de Poisson, relaciona deformação em dois eixos
#frictionAngle: radianos - Ângulo de fricção interno
mat_1=CohFrictMat(density=1243,young=2.6e7,poisson=0.25,frictionAngle=0.4712,label="mat1")
mat_2=CohFrictMat(density=1243,young=2.6e5,poisson=0.25,frictionAngle=0.4712,label="mat2")

#define quatro pontos formando um quadrado no plano z=0
p1=[-1,1,0]
p2=[-1,-1,0]
p3=[1,-1,0]
p4=[1,1,0]

#Cria a primaira face triangular
f1=facet([p1,p2,p4],wire=False,material=mat_1,color=(1,0,0))
#Cria a segunda face triangular
f2=facet([p2,p3,p4],wire=False,material=mat_2,color=(0,1,0))

#Adiciona as faces na simulação
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
	#integracao das forcas
	#damping eh o fator de amortecimento	
	NewtonIntegrator(gravity=(0,0,-9.81),damping=0.1)	
]
#calcula o tamanho do passo de tempo
O.dt=.5e-3*PWaveTimeStep()
# salva o estado da simulacao para reiniciar de necessario
O.saveTmp()
