import os
import snowflake.connector
from dotenv import load_dotenv 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def get_connection():
    '''
    '''
    load_dotenv()
    key_path = os.environ['SNOWFLAKE_PRIVATE_KEY_PATH']
    passphrase = os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE")


    # 1. Open the key file in binary mode ("rb")
    with open(key_path, "rb") as key_file:
        p_key = serialization.load_pem_private_key(
            key_file.read(),
            password=passphrase.encode() if passphrase else None,
            backend=default_backend(),
        )

    # 2. Convert to unencrypted PKCS8 DER bytes
    pkb = p_key.private_bytes(
        encoding = serialization.Encoding.DER,
        format = serialization.PrivateFormat.PKCS8,
        encryption_algorithm = serialization.NoEncryption(),
    )


    conn=snowflake.connector.connect(
            user = os.environ['SNOWFLAKE_USER'],
            account = os.environ['SNOWFLAKE_ACCOUNT'],
            role = os.environ['SNOWFLAKE_ROLE'],
            warehouse = os.environ['SNOWFLAKE_WAREHOUSE'],
            private_key = pkb
            )
    return conn
