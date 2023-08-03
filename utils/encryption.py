import os

from Cryptodome.PublicKey import RSA
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP

class RSACrypt:
    private_key = "keys\private.pem"
    public_key = "keys\public.pem"
    
    def __init__(self) -> None:
        if not os.path.isfile(self.public_key):
            self.generate_keys()
    
    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        with open(self.private_key, "wb") as private_out:
            private_out.write(private_key)

        with open(self.public_key, "wb") as public_out:
            public_out.write(key.publickey().export_key())
            
    def encrypt(self, data):
        data = data.encode("utf-8") 
        recipient_key = RSA.import_key(open(self.public_key).read())
        cipher_rsa = PKCS1_OAEP.new(recipient_key)

        session_key = get_random_bytes(16)
        enc_session_key = cipher_rsa.encrypt(session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        
        with open(r"encrypted\text.bin", "wb") as bin_out:
            for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
                bin_out.write(x)
                
    def decrypt(self, private_key, encrypted_file):

        private_key = RSA.import_key(open(private_key).read())

        with open(encrypted_file, "rb") as bin_file:
            enc_session_key, nonce, tag, ciphertext = \
            [bin_file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        
        return data.decode("utf-8") 

