from pyrogram import Client
my_file = open('username.txt', 'r')
app = Client("my_account")

username = my_file.read()
@app.on_message()

def dump(client, message):
    if(type(message.chat.username) == str):
        if message.chat.username in username: 
            print("Got message from")
            print("username: " + message.chat.username)
            print("message\t: " + message.text)
            if(message.forward(input_your_id_here)):
                print("Status\t: Message Has Been Forwarded")
                print("=============================")
app.run()