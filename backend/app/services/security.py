import bcrypt
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_salt() -> str:
    return bcrypt.gensalt().decode()


def verify_password(plain_password: str, hash_password: str) -> bool:
    return password_context.verify(plain_password, hash_password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)
