import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from manageData import manageData
GROUP_CHAT_ID='-738642398'
emojis=[]
KWORDS=['iphone', 'gb', 'xiaomi', 'samsung']

def cleanEmojis(Pre_Message_text):
    # Function made for cleaning message, eraseing emojis
    Message_text=Pre_Message_text
    for emoji in emojis:
        Message_text=Message_text.replace(emoji,'')
    return Message_text



    pass
def regMessage(Chat_Id,PRODUCTS):
    # Register message
    Response_text=_sendMessage(Chat_Id,PRODUCTS)
    print(Response_text)

def _sendMessage(PRODUCTS):
    # Send Message to group with products and prices changed
    Response_text='Productos Modificados:\n'
    for product in PRODUCTS:
        Response_text+= product.join(' ') + '\n'
    bot.send_message(chat_id=GROUP_CHAT_ID,text=Response_text)
    return Response_text
    
def editWEB(PRODUCTS):
    # edit WEB products price from PRODUCTS detected in message
    pass

def NewIphone(update,context):
    Chat_Id=update.message.chat_id
    Pre_Message_text=update.message.text
    # print(Pre_Message_text)
    Message_text=cleanEmojis(Pre_Message_text)
    currency='USD'
    regMessage(Chat_Id,PRODUCTS)
    Response_text=manageData(Message_text,currency)
    s
    bot.send_message(chat_id=update.message.chat_id,text=Response_text)

def OldIphone(update,context):
    Chat_Id=update.message.chat_id
    Pre_Message_text=update.message.text
    # print(Pre_Message_text)
    Message_text=cleanEmojis(Pre_Message_text)
    currency='USD'
    regMessage(Chat_Id,PRODUCTS)
    Response_text=manageData(Message_text,currency)
    bot.send_message(chat_id=update.message.chat_id,text=Response_text)

def VideoCard(update,context):
    Chat_Id=update.message.chat_id
    Pre_Message_text=update.message.text
    
    Message_text=cleanEmojis(Pre_Message_text)
    currency='Pesos'
    regMessage(Chat_Id,PRODUCTS)
    Response_text=manageData(Message_text,currency)
    bot.send_message(chat_id=update.message.chat_id,text=Response_text)





bot = telegram.Bot(token=TOKEN)
updater = Updater(bot.token,use_context=True)

dispatcher = updater.dispatcher

USDHandler= CommandHandler('Nuevos', NewIphone)
USDHandler= CommandHandler('Usados', OldIphone)
PesosHandler= CommandHandler('Placas', VideoCard)
dispatcher.add_handler(USDHandler)
dispatcher.add_handler(PesosHandler)

# Responses= MessageHandler(Filters.text, Response)
# start_handler = CommandHandler('start', start)

# dispatcher.add_handler(start_handler)

# mayusculas_handler = CommandHandler('mayusculas', mayusculas, pass_args=True)

# dispatcher.add_handler(mayusculas_handler)

updater.start_polling()