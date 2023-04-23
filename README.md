# DBCli_GEN
Generador de contenido para tabla "clientes" de base de datos. Todos los resultados se almacenan en el archivo "export.sql", ubicado en el directorio del script.
## Requisitos

- Python 3
- argparse ```pip install argparse ```
- requests ```pip install requests ```
- random

## Argumentos
| Argumento | Descripción |
| ------ | ------ |
| -t --tabla | Nombre de la tabla en la que se realizará el INSERT. Default: "CLIENTES" |
| -n --nombre | Nombre del campo en el que se insertaran los nombres. Default: "NOMBRE" |
| -a --apellidos | Nombre del campo en el que se insertaran los apellidos. Default: "APELLIDOS" |
| -c --cantidad | Cantidad de INSERTS a generar. Default: 10 |
| -d --dni | Indicar si desea incluir números de DNI en la sentencia. (y/n). Default: y |
| -k --key | API Key de "Randommer". Debes obtener una [aquí.](https://randommer.io/) |

## Uso

### Generar 100 registros, incluyendo DNI.
```sh
cd DBCli_GEN-main
python .\DBCli_GEN.py -k API_KEY -c 100
```
Genera como resultado 100 INSERTS en el siguiente formato: INSERT INTO CLIENTES(NOMBRE,APELLIDOS,DNI) VALUES(<-DATOS GENERADOS->)
### Generar 200 registros, avanzado. Excluyendo DNI.
```sh
cd DBCli_GEN-main
python .\DBCli_GEN.py -k API_KEY -c 200 -t humanos -n primer_nombre -a apellido -d n
```
Genera como resultado 200 INSERTS en el siguiente formato: INSERT INTO humanos(primer_nombre, apellido) VALUES (<-DATOS GENERADOS->)
