from argon2 import PasswordHasher, exceptions

ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(hash: str, password: str) -> bool:
    try:
        return ph.verify(hash, password)
    except exceptions.VerifyMismatchError:
        return False

if __name__ == "__main__":
    senha = "SenhaMuitoForte123!"
    hash_senha = hash_password(senha)
    print(f"Hash gerado: {hash_senha}")
    print("Verificação correta:", verify_password(hash_senha, senha))
    print("Verificação incorreta:", verify_password(hash_senha, "senhaErrada"))
