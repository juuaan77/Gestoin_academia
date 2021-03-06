from .funciones_password import crear_hash
from .funciones_password import clave_valida


class Autenticador:
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

        self.autenticado = False
        self.privilegios = None
        self.user = None

    def crear_usuario(self, user, password, privilegios=3):
        if self.autenticado and self.privilegios == 1:
            # Checkear longitud de la clave
            if not clave_valida(password):
                raise ErrorFormatoClave

            # Crear hash del password
            password_hash = crear_hash(password)

            # Crear sql query
            query = "INSERT INTO usuarios(username, password, privilegios) values('{}', '{}', {})".format(user,
                                                                                                          password_hash,
                                                                                                          privilegios)

            # Ejecutar sql query
            try:
                self.cursor.execute(query)
                self.db.commit()
                return True
            except Exception as e:
                raise ErrorCrearUsuario
        else:
            raise ErrorAutenticacionPrivilegios

    def eliminar_usuario(self, username):
        if self.autenticado and self.privilegios == 1:
            query = "DELETE FROM usuarios WHERE username = '{}'".format(username)

            try:
                    self.cursor.execute(query)
                    self.db.commit()
                    return True
            except Exception as e:
                raise ErrorEliminarUsuario
        else:
            raise ErrorEliminarUsuario

    def autenticar(self, user, password):
        query = "SELECT * FROM usuarios WHERE username = '{}'".format(user)

        try:
            self.cursor.execute(query)

            datos = self.cursor.fetchone()
            stored_hash = datos[2]
            privilegios = datos[3]

            password_hash = crear_hash(password)

            if stored_hash == password_hash:
                self.autenticado = True
                self.user = user
                self.privilegios = privilegios
                return True
            else:
                raise ErrorAutenticacion
        except Exception as e:
            raise ErrorAutenticacion

    def desautenticar(self):
        self.autenticado = False
        self.user = None
        self.privilegios = None

    def cambiar_clave(self, new_password):
        if not clave_valida(new_password):
            raise ErrorFormatoClave

        new_hashed_password = crear_hash(new_password)

        if self.autenticado:
            query = "UPDATE usuarios SET password = '{}'" \
                    "WHERE username = '{}'".format(new_hashed_password, self.user)

            try:
                self.cursor.execute(query)
                self.db.commit()
                return True
            except Exception as e:
                raise ErrorCambiarClave
        else:
            raise ErrorAutenticacionPrivilegios


class ErrorAutenticacion(Exception):
    def __str__(self):
        return "El usuario no se pudo autenticar, verifique que la combinación de usuario y contraseña sea correcta"


class ErrorAutenticacionPrivilegios(Exception):
    def __str__(self):
        return "El usuario no está autenticado o no tiene suficientes privilegios."


class ErrorCrearUsuario(Exception):
    def __str__(self):
        return "El usuario no se pudo crear, verifque que no exista otro usuario con el mismo nombre."


class ErrorEliminarUsuario(Exception):
    def __str__(self):
        return "El usuario no se pudo eliminar, verifque que el nombre de usuario exista."


class ErrorCambiarClave(Exception):
    def __str__(self):
        return "No se pudo cambiar la clave."


class ErrorFormatoClave(Exception):
    def __str__(self):
        return "Clave no válida, verifique que contenga al menos ocho caracteres, mayúscula, minúscula y número."
