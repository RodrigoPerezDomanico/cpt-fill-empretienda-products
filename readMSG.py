from Messages import Messages as MESSAGES

def manageMessage(Title):
    raw_message=MESSAGES[Title] # completar luego con el mensaje que se obtiene del bot
    raw_message=raw_message.replace('*', '')
    raw_message=raw_message.replace('⚒️', '')
    raw_message=raw_message.replace('🔥', '')
    raw_message=raw_message.replace('📱', '')
    raw_message=raw_message.replace('▪️', '')
    raw_message=raw_message.replace('💥', '')

