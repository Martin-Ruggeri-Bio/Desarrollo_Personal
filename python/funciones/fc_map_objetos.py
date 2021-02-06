class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $". format(
            self.nombre, self.cargo, self.salario
        )


def calculo_comision(empleado):
    if empleado.salario <= 50000:
        empleado.salario = empleado.salario*1.03
    return empleado


listaEmpleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Maria", "Presidenta", 85000),
    Empleado("Enzo", "Gerente", 25000),
    Empleado("Dayi", "Contadora", 35000),
    Empleado("Agus", "Ingeniero", 65000),
    Empleado("Lucia", "Secretaria", 45000)
]

listaEmpleadosComision = map(calculo_comision, listaEmpleados)
for empleado in listaEmpleadosComision:
    print(empleado)
