import argparse
import requests
import random

def generarDni(cant):
    dnis = []
    for i in range(cant):
        e = "0"
        for x in range(7):
            x = random.randint(1,9)
            e+=str(x)
        dnis.append(e)
    return dnis

def obtenerDatos(key, cant):
    cabecera = {"X-Api-Key":key,"accept":"*/*"}
    r = requests.get("https://randommer.io/api/Name?nameType=fullname&quantity="+str(cant),headers=cabecera)
    data = r.json()

    listaNombres = []
    for i in range(cant):
        listaNombres.append(data[i].split())
    return listaNombres

def exportarResultado(lista,conDNI,nombreN,nombreA,nombreT):
    archivo = open("export.sql","w")
    listaSize = len(lista)
    if listaSize > 0 and (conDNI=="y" or conDNI =="Y"):
        listaDnis = generarDni(listaSize)
        for i in range(len(lista)):
            archivo.write("INSERT INTO "+nombreT+"("+nombreN+", "+nombreA+", DNI) VALUES ("+"'"+(lista[i])[0]+"'"+","+"'"+(lista[i])[1] +"'"+", '"+listaDnis[i]+"')"+"\n")
        archivo.close()  
    elif listaSize > 0 and (conDNI != "y" or conDNI != "Y"):
        for i in range(len(lista)):
            archivo.write("INSERT INTO "+nombreT+"("+nombreN+", "+nombreA+") VALUES ("+"'"+(lista[i])[0]+"'"+","+"'"+(lista[i])[1] +"')"+"\n")
        archivo.close()  
    else:
        archivo.write("[ERROR] : Algo ha fallado!")
        archivo.close()

parser = argparse.ArgumentParser()

parser.add_argument("-t","--tabla",type=str,help="Nombre de la tabla.", default="CLIENTES")
parser.add_argument("-n","--nombre",type=str,help="Asigne nombre al campo 'nombres'",default="NOMBRE")
parser.add_argument("-a","--apellidos",type=str,help="Asigne nombre al campo 'apellido/s'",default="APELLIDOS")
parser.add_argument("-c","--cantidad",type=int,help="Cantidad de registros a generar.",default=10)
parser.add_argument("-d","--dni", type=str,choices=["y","n"],default="y",required=False,help="Seleccione si desea incluir campo dni y su contenido.")
parser.add_argument("-k","--key",type=str,required=True,help="Ingrese API KEY de Randommer.io")

args = parser.parse_args()

if (args.cantidad <= 0):
    print("[ADVERTENCIA] : Debe ingresar un número igual o mayor a 0 al parametro de cantidad.")
else:
    listado = obtenerDatos(str(args.key),args.cantidad)
    exportarResultado(listado,args.dni,args.nombre,args.apellidos,args.tabla)
    print("[TERMINADO] : Número de registros generados: "+str(len(listado)))