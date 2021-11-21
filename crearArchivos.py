import os

for i in range(10):
    file = open('./archivo-de-prueba-'+str(i) +
                'archivo-de-prueba.txt', 'w')
    file.write('texto de ejemplo'+str(i))
    file.close()
