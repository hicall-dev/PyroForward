# CEK ID
from pyrogram import Client
app = Client("my_account")
@app.on_message()
def dump(client, message):
    if(message.chat.id):
        print("id :" , message.chat.id)
app.run()