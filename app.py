from telebot import TeleBot
app = TeleBot(__name__)



@app.route("/menu") 
#@app.route("/menu")  
#significa: se mensagem for igual a o parâmetro passado no (), execute a função com o nome pcmd(tem que trocar)
def pcmd(message):
   sender = message['chat']['id']
   app.send_message(sender, """
Menu m7 bot kakakakak

   """)
   
   
if __name__ == '__main__':
    app.config['api_key'] = 'tua key'
    app.poll(debug=True)
    