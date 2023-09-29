from fastapi import FastAPI, APIRouter
import edgedb

from auth.security import get_password_hash, get_user, verify_password
from auth.user import CreateUser, UserBook

client = edgedb.create_client()

app = FastAPI()

router = APIRouter(tags=["User"], prefix="/user")
router1 = APIRouter(tags=["Booking"], prefix="/booking")

@router.post("/")
async def root(data: CreateUser):
    client.query("""
        INSERT User {
            username := <str>$username,
            password := <str>$password
        }
    """, username=data.username, password=get_password_hash(data.password))
    return "КИРИЛЛ ПУПСИК"

@router.delete("/")
async def del_user(data: CreateUser):
    user = get_user(data.username)
    if not user:
        return False
    if not verify_password(data.password, user.password):
        return False
    client.query("""
        delete User{
            *
        }
        filter .username = <str>$username 
    """ , username = user.username)
    return user.id


@router.post("/login")
def authenticate_user(data: CreateUser):
    user = get_user(data.username)
    if not user:
        return False
    if not verify_password(data.password, user.password):
        return False
    return "ОНО РАБОТАЕТ"

@router1.post("/")
def get_session(data: UserBook):
    user = get_user(data.username)
    if not user:
        return False
    if not verify_password(data.password, user.password):
        return False
    client.query("""
        INSERT Booking{
            user := (SELECT User {*} filter .id = <uuid>$user_id),
            comment := <str>$comment,
            start_time := <datetime>$start_time,
            end_time := <datetime>$end_time
        }
    """, user_id = user.id ,comment = data.comment, start_time = data.start_time, end_time = data.end_time)


app.include_router(router1)
app.include_router(router)