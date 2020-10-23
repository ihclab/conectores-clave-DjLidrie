users = [{"id": 0, "name": "Hero"},      
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "CLive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
        ]

friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),(4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#creamos una lista vacia, para agregar un nuevo campo a la lista existente users
for user in users:
    user["amigos"] = []

#recorremos las tuplas de la lista friendships, tanto en sentido de izquierda a derecha, 
#Como de derecha a izquierda, y agregamos los datos a la lista "amigos" que acabamos de crear
for x, y in friendships:
    users[x]["amigos"].append(users[y] ["name"])
    users[y]["amigos"].append(users[x] ["name"])

#Imprimimos el recorrido que hicimos pero agregando los amigos["name"] correspondintes de la tupla 
# "friendships"
print(users)


#Promedio de amigos, la lista "user" contiene la lista de amigos, utilizaremos la función "len"
#para devolver el número
def num_amigos(user):
    return len(user["amigos"])
conexiones = sum(num_amigos(user) for user in users)
print("--------PARÁMETROS------------")
print(conexiones)

#Ahora dividimos para obtener el promedio
num_usuarios = len(users)
print(num_usuarios)
promedio = conexiones / num_usuarios
# 24 (total de conexiones de amistades) / 10 (total de la lista de la lista principal, numero de usuarios)
print("--------PROMEDIO------------")
print(promedio)

#cantidad de amigos de cada usuario
cant_amigos_name = [(user["name"], num_amigos(user)) for user in users]
print("--------AMIGOS------------")
print(cant_amigos_name)


