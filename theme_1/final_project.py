
# Header
def header() :
    """Header app
    """
    title = r"""
                       
 /$$__  $$                                        | $$__  $$| $$                  | $$                        
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$| $$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$$$$$$/| $$__  $$| $$  | $$|_  $$_/   /$$__  $$| $$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$____/ | $$  \ $$| $$  | $$  | $$    | $$  \ $$| $$  \ $$
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      | $$      | $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$  | $$
 \______/  \_______/|__/ |__/ |__/ \_______/      |__/      |__/  |__/ \____  $$   \___/   \______/ |__/  |__/
                                                                       /$$  | $$                              
                                                                      |  $$$$$$/                              
                                                                       \______/                               
    """
    print(title)
    
def getTag(name) :
    return name [:4]
  
def revertTag(name) :
    return name[::-1]

def intercalate(name, lastname) :
    first_name = name[0]
    first_lastname = lastname[0]
    return f"{first_name}{first_lastname}{name[1:]}{lastname[1:]}"

def eliteTag(name) :
    return f"{name[:2]}{name[-2:]}"

def favNumber(name, number) : 
    return f"{name[:5]}{number}"

def displayInfo(name) :
    print("Nombre completo: ", name)
    print("Longitud del nombre: ",{len(name)})
    print("Primera letra: ", {name[0]})
    print("Última letra: ", {name[-1]})
    
def displayTags(name, lastName, number) :
    print("\n TUS OPCIONES DE TAGS PARA GAMING")
    print("\nTag Basico: ", getTag(name))
    print("\nTag Invertido: ", revertTag(name))
    print("\nTag Intercalado: ", intercalate(name, lastName))
    print("\nTag Elite: ", eliteTag(name))
    print("\nTag Fav number: ", favNumber(name, number))
    

# Running app
header()
name = input("\n Introdice nombre: ")
lastname = input("\n Introduce apellido: ")
number = input("\n Introdice tu numero favorito: \n")

displayInfo(name)
displayTags(name, lastname,number)

print("\nElige tu favorito y a jugar!!!")

    
    
                                                                       
                                                                       
    
    