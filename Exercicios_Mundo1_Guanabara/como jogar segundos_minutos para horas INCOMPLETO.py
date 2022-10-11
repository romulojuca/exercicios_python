r = 5
pi = 3.141592653589793
rf = ((4/3)*(pi)*(r**3))
print (rf)

c = 24.95
cd = 24.95*0.4
cdt = (c - cd)*60
print ('{:.3f}'.format(cdt),'R$ custarao as capas')

ct = ((59*0.75)+(3))
print ('{:.3f}'.format(ct),'R$ de transporte')

t = ct+cdt
print ('{:.3f}'.format(t),'R$ Para comprar e transportar ate o local')


#Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 
# 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
kma = (8*60+15)
print (kma)
kmb = (7*60+12)*3
print (kmb)
kmc = (8*60+15)
print (kmc)
kmt = kma+kmc+kmb
print (kmt,'Segundos')
print (kmt/60,'minutos')
print  #falta somar os minutos com a hora (6:52)