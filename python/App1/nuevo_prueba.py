class Persona(object):
    def __init__(self, cedula, nombre, apellido, sexo):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.cedula), self.nombre,
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        return mensaje

    def getGenero(self, sexo):
        genero = ('Masculino', 'Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"


class Supervisor(Persona):
    def __init__(self, cedula, nombre, apellido, sexo, rol):
        Persona.__init__(self, cedula, nombre, apellido, sexo)
        self.rol = rol
        self.tareas = ['10', '11', '12', '13']

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido,
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ', '.join(self.tareas)


class Destreza(object):
    def __init__(self, area, herramienta, experiencia):
        """Constructor de clase Destreza"""
        self.area = area
        self.herramienta = herramienta
        self.experiencia = experiencia

    def __str__(self):
        """Devuelve una cadena representativa de la Destreza"""
        return """Destreza en el área %s con la herramienta %s,
        tiene %s años de experiencia.""" % (
            str(self.area), self.experiencia, self.herramienta)


class JefeCuadrilla(Supervisor, Destreza):
    """Clase la cual representa al Jefe de Cuadrilla"""

    def __init__(self, cedula, nombre, apellido, sexo,
                 rol, area, herramienta, experiencia, cuadrilla):
        Supervisor.__init__(self, cedula, nombre, apellido, sexo, rol)
        Destreza.__init__(self, area, herramienta, experiencia)
        self.cuadrilla = cuadrilla

    def __str__(self):
        """Devuelve cadena representativa al Jefe de Cuadrilla"""
        jq = "{0}: {1} {2}, rol '{3}', tareas {4}, cuadrilla: {5}"
        return jq.format(
            self.__doc__[28:46], self.nombre, self.apellido,
            self.rol, self.consulta_tareas(), self.cuadrilla)
