import os

for i in range(3):
    file = open('./archivo-de-prueba-'+str(i) +
                'archivo-de-prueba.txt', 'w')
    file.write('texto de ejemplo'+str(i))
    file.close()
file = open('./archivo-de-prueba-'+str(10) +
            'archivo-de-prueba.txt', 'w')
file.write('texto de ejemplo'+str(10))
file.close()
file = open('./archivo-de-prueba-'+str(100) +
            'archivo-de-prueba.txt', 'w')
file.write('texto de ejemplo'+str(100))
file.close()
file = open('./archivo-de-prueba-'+str(1000) +
            'archivo-de-prueba.txt', 'w')
file.write('texto de ejemplo'+str(1000))
file.close()
file = open('./archivo-de-prueba-'+str(123456) +
            'archivo-de-prueba.txt', 'w')
file.write('texto de ejemplo'+str(123456))
file.close()
