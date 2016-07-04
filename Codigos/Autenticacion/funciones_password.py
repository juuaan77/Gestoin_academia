import re
import hashlib


def crear_hash(password):
    m = hashlib.sha256()
    m.update(password.encode())
    password_hash = m.hexdigest()

    return password_hash


def clave_valida(clave):
    result = re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}", clave)
    return True if result else False