import sys
import os
from argon2 import PasswordHasher, exceptions
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(hash: str, password: str) -> bool:
    try:
        return ph.verify(hash, password)
    except exceptions.VerifyMismatchError:
        return False

def encrypt_data(key: bytes, data: bytes) -> bytes:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, None)
    return nonce + ct

def decrypt_data(key: bytes, encrypted_data: bytes) -> bytes:
    aesgcm = AESGCM(key)
    nonce = encrypted_data[:12]
    ct = encrypted_data[12:]
    return aesgcm.decrypt(nonce, ct, None)

def main():
    print("=== SecureDevPack CLI ===")
    print("1 - Hash de senha")
    print("2 - Verificar hash de senha")
    print("3 - Criptografar texto")
    print("4 - Decriptografar texto")
    print("0 - Sair")
    chave = AESGCM.generate_key(bit_length=256)
    while True:
        opcao = input("Escolha a opção: ").strip()
        if opcao == '1':
            senha = input("Digite a senha para hash: ")
            h = hash_password(senha)
            print(f"Hash gerado: {h}")
        elif opcao == '2':
            hash_input = input("Digite o hash: ")
            senha = input("Digite a senha para verificar: ")
            ok = verify_password(hash_input, senha)
            print("Senha válida?" , ok)
        elif opcao == '3':
            texto = input("Digite o texto para criptografar: ").encode()
            ct = encrypt_data(chave, texto)
            print(f"Texto criptografado (hex): {ct.hex()}")
        elif opcao == '4':
            ct_hex = input("Digite texto criptografado (hex): ")
            try:
                ct = bytes.fromhex(ct_hex)
                original = decrypt_data(chave, ct)
                print("Texto decriptografado:", original.decode())
            except Exception as e:
                print("Erro ao descriptografar:", e)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
