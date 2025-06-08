from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

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

if __name__ == "__main__":
    chave = AESGCM.generate_key(bit_length=256)
    texto = b"Informacao secreta ultra segura"
    criptografado = encrypt_data(chave, texto)
    print(f"Criptografado: {criptografado.hex()}")
    original = decrypt_data(chave, criptografado)
    print(f"Decriptado: {original.decode()}")
