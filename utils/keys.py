from Crypto.PublicKey import RSA

#lybrairie a porter general dans le projet


def generate_keys():
    """
    Generate a public/private key pair using RSA.
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

print(generate_keys())  