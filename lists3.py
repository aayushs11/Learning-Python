dev = []

dev.append('Aayush')
dev.append('Mitra')
dev.append('Agni')
dev.append('Indra')
dev.append('Ajaekpada')
dev.append('Varuna')
dev.append('Ahirbudnya')

a = [dev for dev in dev if dev.startswith('A')]
print('Gods',a)

b = [dev for dev in dev if not dev.startswith('A')]
print('Gods',b)