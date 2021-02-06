class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $". format(
            self.nombre, self.cargo, self.salario
        )


listaEmpleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Maria", "Presidenta", 85000),
    Empleado("Enzo", "Gerente", 25000),
    Empleado("Dayi", "Contadora", 35000),
    Empleado("Agus", "Ingeniero", 65000),
    Empleado("Lucia", "Secretaria", 45000),
]

salarios_altos = filter(
    lambda empleado: empleado.salario > 50000, listaEmpleados
)
for empleado_salario in salarios_altos:
    print(empleado_salario)
