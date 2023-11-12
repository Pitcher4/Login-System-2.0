import hashlib
import secrets


class User:

    SALT_LENGTH = 128

    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.salt = secrets.randbits(self.SALT_LENGTH)
        self.password_hash = self.hash_password(password, self.salt)

    def hash_password(self, password, salt):
        return hashlib.sha3_512(f"{password}{salt}".encode("UTF-8")).hexdigest()
