def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayuscula
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

def run():
    nombre = "felix"
    print(mensaje(nombre))
    name_upper = mayuscula(mensaje)
    print(name_upper(nombre))

if __name__ == "__main__":
    run()