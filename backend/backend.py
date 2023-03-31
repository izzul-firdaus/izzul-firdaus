import backend.backend_temporary as temp
import sqlite3

# get user ID, -1 if invalid
def login(uname: str, upass: str):
    if uname in temp.db_userlogins and (result := temp.db_userlogins[uname])[0] == upass:
        return result[1]
    return -1


# get all data of a user
def get_user_data(uid: int):
    if uid in temp.db_userdata:
        return temp.db_userdata[uid]
    return None

conn = sqlite3.connect('test.db')


