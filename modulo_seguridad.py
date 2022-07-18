class Sistema_Admin:
    pass

class Usuario:
    def __init__(self,nombre,cedula,telefono,correo,tipo_usuario):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.tipo_usuario = tipo_usuario

class Opciones_Sis(Usuario):
    def __init__(self,nomb,cedu,tele,correo,tipo_user,id_rol,nombre_opcion):
        super().__init__(nomb,cedu,tele,correo,tipo_user)
        self.id_rol = id_rol
        self.nombre_opcion = nombre_opcion

class Rol(Opciones_Sis):
    def __init__(self, nomb, cedu, tele, correo, tipo_user, id_rol, nombre_opcion, tipo_rol, sueldo):
        super().__init__(nomb, cedu, tele, correo, tipo_user, id_rol, nombre_opcion)
        self.tipo_rol = tipo_rol
        self.sueldo = sueldo

class Operaciones(Rol):
    def __init__(self, nomb, cedu, tele, correo, tipo_user, id_rol, nombre_opcion, tipo_rol, sueldo, horas_activo, operaciones_realizadas):
        super().__init__(nomb, cedu, tele, correo, tipo_user, id_rol, nombre_opcion, tipo_rol, sueldo)
        self.horas_activo = horas_activo
        self.operaciones_realizadas = operaciones_realizadas

class Modulo_Seguridad:
    def operaciones(self):
        pass