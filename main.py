from bot import Bot
from asyncio import run as arun 

# run bot from corrent file 
if __name__ == '__main__':
    path = "../token.txt"
    with open(path,"r",encoding='utf-8') as f:
        token = f.readline().rstrip("050fa23e453578beb0321fbaa6d29e76dbd8b03148af11530a092aee86196c38")
        room_id = f.readline().rstrip("660e6448818d797101c5d230")
    arun(Bot().run(room_id, token))
