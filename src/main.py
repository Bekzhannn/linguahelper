import telebot
import xlrd
import os
from random import (randint, random)

rb = xlrd.open_workbook('../inputs/Savedtranslations.xlsx')
sheet = rb.sheet_by_index(0)
mysheet = []
for i in range(sheet.nrows):
    mysheet.append([sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2), sheet.cell_value(i, 3)])
n = len(mysheet)
print(n)
''' All data from the exsel file is inserted into the mysheet '''

def rand():
    '''
    Get randomly one translation from given file
       Returns
       -------
       str
           Random translated phrase/sentence
    '''
    rm = randint(0, n)
    return mysheet[rm][0] + ' ----- ' + mysheet[rm][1] + '\n' + mysheet[rm][2] + ' ----- ' + mysheet[rm][3]

def checklang():
    lan = set()
    for i in range(n):
       lan.add(str(mysheet[i][0]) + " ---- " + str(mysheet[i][1]))
    return lan
    ''' 
     
     Returns
       -------
      function returned set languages '''

def randtwo(ls, sr):
    '''
       Get randomly one translation from given file
          Parameters
          ----------
          ls: str
              Language to translate from
          sr: str
              Language to translate to
          Returns
          -------
          str
              Random translated phrase/sentence
       '''
    rm = randint(0, n-1)
    print(rm)
    while (True):
        if(ls == mysheet[rm][0] and sr == mysheet[rm][1]):
            break
        else:
            rm = randint(0, n-1)
    return mysheet[rm][0] + ' ----- ' + mysheet[rm][1] + '\n' + mysheet[rm][2] + ' ----- ' + mysheet[rm][3]



TOKEN = "1001230120:AAHB5gaj02BOsMTENcNDBGJFgKOzNYm4L70"
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, rand())


@bot.message_handler(commands=['frenchenglish'])
def englishfrench(message):
    ''' function randomly selects and displays words from an Exsel file,only
    translate words from French to English.
    '''
    bot.send_message(message.chat.id, randtwo('French','English'))


@bot.message_handler(commands=['englishfrench'])
def frenchenglish(message):
    ''' function randomly selects and displays words from an Exsel file,
    only translating words from English to French.
    '''
    bot.send_message(message.chat.id, randtwo('English','French'))

@bot.message_handler(commands=["listoflanguages"])
def handle_start(message):
    '''list of language combinations'''
    user_markup =telebot.types.ReplyKeyboardMarkup()
    for i in checklang():
        user_markup.row(i)
    bot.send_message(message.chat.id,'Selected language!!!',reply_markup=user_markup)



@bot.message_handler(content_types=['text'])
def main(message):
    '''choice of language combinations'''
    checklan = str(message.text)
    lans = checklan.split(' ---- ')
    bot.send_message(message.chat.id, randtwo(lans[0], lans[1]))

if __name__ == '__main__':
     bot.polling(none_stop=True)


