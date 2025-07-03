#Vamos a trabajar con librerias
#importaremos la libreria os que nos permite trabajar con el sistema operativo mismo
import os

"""
cwd = os.getcwd()#cwd hace referencia a current working directory
    #y lo que hacemos es decirle que os (sistema operativo) llame al metodo que nos diga en que directorio estamos
print('Directorio de trabajo actual', cwd)
    #Directorio de trabajo actual E:\Cursos\Curso de Python
"""

#Ahora vamos a intentar listar los archvios que sean tipo .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]#estamos cargando en una variable una list compresion
    #donde definimos f y que para f en el sistemaoperativo me liste la informacion del directorio
    #os.listdir() lista toda la informacion del directorio
        #pero yo quiero saber solo los .txt
    #('.') hace que sea toda la informacion del directorio donde estoy
    #.endswith() hace que busque los archivos que tengan la terminacion que especifique en el parentesis
print('Archivos txt: ', txt_files)
    #  #Directorio de trabajo actual E:\Cursos\Curso de Python
#Archivos txt:  ['clase30_caperusita.txt']

#Ahora veremos como se renombra un archvio
os.rename('clase30_caperusita.txt', 'clase30_cuentoRenombradoEnLaClase34.txt')#ose.raname renombra el archivo y despues de la , pongo como se debe llamar
print('Archivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Archivos txt: ', txt_files)
#Resultado
"""  #Directorio de trabajo actual E:\Cursos\Curso de Python
Archivos txt:  ['clase30_caperusita.txt']
Archivo renombrado
Archivos txt:  ['clase30_cuentoRenombradoEnLaClase34.txt']
"""