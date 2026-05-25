# Practice Varaibles


# Crear un "Menú del Día de un Restaurante Gourmet" usando variables y la función print para mostrar los platos en la consola.

nombre_entrante = "Caldo de pollo"
precio_entrante = "5"
nombre_principal = "Arroz de marisco"
precio_principal = "10"
nombre_postre = "Flan"
precio_postre = "3"

print("Menú del Día - Restaurante Gourmet")
print("-- Entrante --")
print(nombre_entrante)
print("Precio:")
print(precio_entrante)
print("-- Plato Principal --")
print(nombre_principal)
print("Precio:")
print(precio_principal)
print("-- Postre -")
print(nombre_postre)
print("Precio:")
print(precio_postre)

# Indexation

my_name = "Sergio"

print(my_name[0]) #Print S
print(my_name[3]) #Print g
print(my_name[-1]) #Print o
print(my_name[-2]) #Print i

# Slicing (Takes pieces of Strings)

name = "Fernando Julian"

print(name[0:3]) #Fer
print(name[0:-3]) #Fernando Jul
print(name[2:9]) #rnando
print (name[9:]) #Julian (No number indicates util the end of the string)


#Stride (Similar to Slicing but define a pattern to skip some letters)

str = "Barcelona"

print(str[0::2]) #Breoa (The number 2 indeicates that the secuence takes a letter for each 2 positions)
print(str[0::3]) #Bco (The number 2 indeicates that the secuence takes a letter for each 2 positions)

# Multiples lines (Two possible ways)

str2 = "Sergio\n bs"
print(str2)

str2 = """Sergio
bs"""
print(str2)

parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."
parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."
parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."


part1 = parrafo1[1::18]
part2 = parrafo2[138:147]

first = parrafo3[125]
sec = parrafo3[94]
third = parrafo3[35]
four = parrafo3[107]
five = parrafo3[20]
six = parrafo3[1]

part3 = first + sec + third + four + five + six

text = "Mensajes Secretos Decodificados:\nMensaje secreto 1:\n" + part1 + "\n" + "Mensaje secreto 2:\n" + part2 + "\n" + "Mensaje secreto 3:\n" + part3

print(text)

########################

nombre_astronauta = "Sergio"
edad_astronauta = 36
destino = "Saturno"
combustible = 150
velocidad = 3000

print("Diario de un Astronauta\n")
print(f"Hola, soy {nombre_astronauta}, tengo {edad_astronauta} años y mi próximo destino es {destino}.")
print(f"Estoy navegando a {velocidad} km/s con {combustible}% de combustible restante hacia {destino}.")
print("Fecha: 2024-01-10")
print("Hoy experimentamos con el cultivo de plantas en microgravedad.")
print("Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!\n")
print("Fecha: 2024-01-11")
print("Realizamos una caminata espacial para reparar un panel solar.")
print("Mensaje personal: Flotar en el espacio nunca deja de asombrarme.\n")

# Len (function to count chars) 

titulo1 = "Cien años de soledad"
titulo2 = "El señor de los anillos"
titulo3 = "Don Quijote de la Mancha"

len1 = len(titulo1)
len2 = len(titulo2)
len3 = len(titulo3)

print(f"La longitud del título del libro 1 es: {len1}")
print(f"La longitud del título del libro 2 es: {len2}")
print(f"La longitud del título del libro 3 es: {len3}")

