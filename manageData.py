def cleanEmojis(Pre_Message_text):
    # Function made for cleaning message, eraseing emojis
    Message_text=Pre_Message_text
    for emoji in emojis:
        Message_text=Message_text.replace(emoji,'')
    return Message_text

def getPrices(line,text):
    # words=line.split(' ')
    # for word in words:
    #     print(word)
    pass

def getProductLines(text):
    # lines= text.splitlines()
    # product_lines=[]
    # for line in lines:
    #     words=line.split(' ')
    #     for idx, word in enumerate(words):
    #         if word
    pass

def caracterizeMessage(text):
    text=text.splitlines
    product_lines=getProductLines(text)
    PRODUCTS=[]
    for line in product_lines:
        product,price = getPrices(line,text)
        PRODUCTS.append([product,price])
    return PRODUCTS

def manageData(text):
    text=cleanEmojis(text)
    PRODUCTS=caracterizeMessage(text)

    return PRODUCTS