import edgedb
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


SECRET_KEY= "572c45dd4baac80ee05b008ed6cb9e76693045537a971a7e0d0d376a9feb271d"

ACCESS_TOKEN_EXPIRE_MINUTES = 2

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

client = edgedb.create_client()
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    a = client.query("""
        SELECT User{
            *
        }
        filter .username = <str>$username 
    """ , username = username)
    if a:
        return a[0]
    return None
