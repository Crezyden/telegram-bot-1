    
from http import server
import os
from aiogram import types
from telebot import types
import datetime
from datetime import datetime
import telebot  
from bs4 import BeautifulSoup
import requests
import config



bot = telebot.TeleBot(config.TOKEN, parse_mode='html')
# dispatcher =bot.dispatcherZZZ 
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("🌦 Kāds laiks ir Liepājā?")
    item2 = types.KeyboardButton("🔍 Kopigais informacija par pilsetu!")
    item3 = types.KeyboardButton("🆘 Nepieciešama palīdzība!")
    item4 = types.KeyboardButton("📰 Ziņas!")
    item5 = types.KeyboardButton("🗺 Pilsētas ceļvedis")
    markup.add(item1,item2,item3,item4, item5) 
    bot.send_message(message.chat.id, "<b>{0.username}</b>, добро пожаловать! \n Я - личный ваш асистен по Лиепае! \n Какая помошь требуеться? \n Готов с удоволствием помочь!". format(message.from_user, bot.get_me()),
    reply_markup=markup)

@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == '🌦 Kāds laiks ir Liepājā?':
        mgr = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=56.5048435&lon=21.0070903&appid=6eb7e46c79d381e6ad175382aa50e4cd&units=metric")
        data = mgr.json()
        cur_weather = data["main"]["temp"]
        wind = data["wind"]["speed"] 
        today = datetime.today()
        global answer
        answer = 'Сегодня, ' + (today.strftime("%d/%m/%Y")) +'\n'
        answer += 'Temperatura Liepaja: ' + (str(cur_weather)) + ' Gradi.' + '\n' + 'Vēja ātrums:'+ (str(wind)) + ' m/s \n'
        bot.send_message(message.chat.id, answer)
    elif message.text == '🔍 Kopigais informacija par pilsetu!':
        infolist ='Rajons: Kurzeme \n Pilsētas tiesības: 1625. gada \n Pilsetas platiba: 68 km(2) \n Iedzīvotāji: 67 964 \n Mājaslapa: https://www.liepaja.lv/'  
        bot.send_message(message.chat.id, infolist)
    elif message.text == '🆘 Nepieciešama palīdzība!':
        markups = types.InlineKeyboardMarkup(row_width=1)
        items1 = types.InlineKeyboardButton(text='SOS', callback_data="med" )
        items2 = types.InlineKeyboardButton(text='Tūrisma palidziba', callback_data='Travel')
        markups.add(items1,items2)
        bot.send_message(message.chat.id,'Kāda palīdzība jums ir vajadzīga?', reply_markup=markups)
        # news(message)
    else:
        if message.text == "📰 Ziņas!":
            markups = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            news1 = types.KeyboardButton("Sports")
            news2 = types.KeyboardButton("Kulturvide")
            news3 = types.KeyboardButton("Izklaide")
            news4 = types.KeyboardButton("Kriminlzinas")
            back = types.KeyboardButton("Atpakal")
            back = types.KeyboardButton("Atpakal")
            markups.add(news1,news2,news3,news4,back)
            bot.send_message(message.chat.id, 'Выберите что хотите почитать' , reply_markup=markups) 
            # papers = news()
            # bot.send_message(message.chat.id, papers) 
        elif message.text == "Atpakal":            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton("🌦 Kāds laiks ir Liepājā?")
            item2 = types.KeyboardButton("🔍 Kopigais informacija par pilsetu!")
            item3 = types.KeyboardButton("🆘 Nepieciešama palīdzība!")
            item4 = types.KeyboardButton("📰 Ziņas!")
            item5 = types.KeyboardButton("🗺 Pilsētas ceļvedis")
            markup.add(item1,item2,item3,item4, item5)
            bot.send_message(message.chat.id, 'Какая помощь требуеться' , reply_markup=markup) 
# news
        if message.text =='Sports':
            url='https://www.liepajniekiem.lv/sports/'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            news = soup.find('div', class_='heading-box lead-with-blur')
            post = soup.find('div', class_='col-12 col-lg-8 news-boxes-area list-area')
            i = 4
            # post = soup.find('article')
            article_card = soup.find('div', class_='row')
            for article_card in post:
                # while post < i:
                article_title =  post.find("h2", ).text.strip()
                article_descr =  post.find('p').text.strip()
                article_url = post.find("a", href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n\n'+article_descr+'\n\n'+article_url+'\n'
                if post.index(article_card) ==1:
                        break   
            bot.send_message(message.chat.id,caption)

        elif message.text == 'Kulturvide':
            url='https://www.liepajniekiem.lv/zinas/kulturvide/'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            news = soup.find('div', class_='heading-box lead-with-blur')
            post = soup.find('div', class_='col-12 col-lg-8 news-boxes-area list-area')
            i = 4
            # post = soup.find('article')
            article_card = soup.find('div', class_='row')
            for article_card in post:
            # while post < i:
                article_title =  post.find("h2", ).text.strip()
                article_descr =  post.find('p').text.strip()
                article_url = post.find("a", href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n\n'+article_descr+'\n\n'+article_url+'\n'
                if post.index(article_card) ==1:
                        break 
                bot.send_message(message.chat.id,caption)
        elif message.text == 'Izklaide':
            url='https://www.liepajniekiem.lv/izklaide/'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            news = soup.find('div', class_='heading-box lead-with-blur')
            post = soup.find('div', class_='col-12 col-lg-8 news-boxes-area list-area')
            i = 4
            # post = soup.find('article')
            article_card = soup.find('div', class_='row')
            for article_card in post:
            # while post < i:
                article_title =  post.find("h2", ).text.strip()
                article_descr =  post.find('p').text.strip()
                article_url = post.find("a", href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n\n'+article_descr+'\n\n'+article_url+'\n'
                if post.index(article_card) ==1:
                        break 
                bot.send_message(message.chat.id,caption)
        elif message.text == 'Kriminlzinas':
            url='https://www.liepajniekiem.lv/zinas/kriminalzinas-negadijumi/'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            news = soup.find('div', class_='heading-box lead-with-blur')
            post = soup.find('div', class_='col-12 col-lg-8 news-boxes-area list-area')
            i = 4
            # post = soup.find('article')
            article_card = soup.find('div', class_='row')
            for article_card in post:
            # while post < i:
                article_title =  post.find("h2", ).text.strip()
                article_descr =  post.find('p').text.strip()
                article_url = post.find("a", href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n\n'+article_descr+'\n\n'+article_url+'\n'
                if post.index(article_card) ==1:
                        break 
                bot.send_message(message.chat.id,caption)
        elif message.text == '🗺 Pilsētas ceļvedis':
            markupd = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            back = types.KeyboardButton("Atpakal")
            info = 'Ko jus velotiet darit Liepaja? \n1) Paēst\n2) Paskatit kaut ko \n3)Palikt viesnīcā \n Ievad ciparinš' 
            markupd.add(back) 
            bot.send_message(message.chat.id, info)
        if message.text == '1':
            infos = 'Kur grib paest?\n1)Pilseta \n2)Kurzeme regiona \n Uzrakst pirmu burtvs'
            # await 
            bot.send_message(message.chat_id, infos)
        if message.text == '2':
            infos = 'Ko grib apskatit?\n1)Dabu \n2) Vestures arhetektura \n3)Skaistas vietas\n Uzrakst pirmu burtvs'
            # await 
            bot.send_message(message.chat_id, infos)
# def est(message: types.Message): 
        if message.text == '3':
            # header = 
            url='https://liepaja.travel/planot/naktsmitnes/'
            page = requests.get(url)
            # page = requests(url )
            soup = BeautifulSoup(page.text, 'html.parser')
            article_card = soup.find_all('article', class_="card")
            for article in article_card:
                article_img =  article.find("img", class_='card__image', src=True)['src'].strip()
                # article_img = article.urlretrieve("img", class_='card__image' "...\img.jpg")
                # article_img =  article_card.find("img", class_='card__image' )
                article_title =  article.find("h3", class_='card__title' ).text.strip()
                article_descr =  article.find('div', class_="card__content").text.strip()
                icon=article.find("i", class_='inline-icon inline-icon--secondary material-icons')
                icon.decompose() 
                article_loc =  article.find('div', class_='card__note d-none d-lg-block').text.strip()
                # for art in article_loc:   
                article_url = article.find('a', class_='overlay-link', href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n'+article_descr+'\nLocacija: <b>'+article_loc+'</b>\n'+ article_url+'\n'
                bot.send_message(message.chat.id,caption)
                bot.send_photo(message.chat.id,article_img +'\n' )
        if message.text == 'P':
            # header = 
            url='https://liepaja.travel/est-un-izklaideties/kur-paest/?region=2'
            page = requests.get(url)
            # page = requests(url )
            soup = BeautifulSoup(page.text, 'html.parser')
            article_card = soup.find_all('article', class_="card")
            for article in article_card:
                article_img =  article.find("img", class_='card__image', src=True)['src'].strip()
                # article_img = article.urlretrieve("img", class_='card__image' "...\img.jpg")
                # article_img =  article_card.find("img", class_='card__image' )
                article_title =  article.find("h3", class_='card__title' ).text.strip()
                article_descr =  article.find('div', class_="card__content").text.strip()
                icon=article.find("i", class_='inline-icon inline-icon--secondary material-icons')
                icon.decompose() 
                article_loc =  article.find('div', class_='card__note d-none d-lg-block').text.strip()
                # for art in article_loc:   
                article_url = article.find('a', class_='overlay-link', href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n'+article_descr+'\nLocacija: <b>'+article_loc+'</b>\n'+ article_url+'\n'
                bot.send_message(message.chat.id,caption)
                bot.send_photo(message.chat.id,article_img +'\n' )
        if message.text == 'K':
            # header = 
            url='https://liepaja.travel/est-un-izklaideties/kur-paest/?region=3'
            page = requests.get(url)
            # page = requests(url )
            soup = BeautifulSoup(page.text, 'html.parser')
            article_card = soup.find_all('article', class_="card")
            for article in article_card:
                article_img =  article.find("img", class_='card__image', src=True)['src'].strip()
                # article_img = article.urlretrieve("img", class_='card__image' "...\img.jpg")
                # article_img =  article_card.find("img", class_='card__image' )
                article_title =  article.find("h3", class_='card__title' ).text.strip()
                article_descr =  article.find('div', class_="card__content").text.strip()
                icon=article.find("i", class_='inline-icon inline-icon--secondary material-icons')
                icon.decompose() 
                article_loc =  article.find('div', class_='card__note d-none d-lg-block').text.strip()
                # for art in article_loc:   
                article_url = article.find('a', class_='overlay-link', href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n'+article_descr+'\nLocacija: <b>'+article_loc+'</b>\n'+ article_url+'\n'
                bot.send_message(message.chat.id,caption)
                bot.send_photo(message.chat.id,article_img +'\n' )  
        if message.text == 'D':
            # header = 
            url='https://liepaja.travel/darit-redzet/daba/'
            page = requests.get(url)
            # page = requests(url )
            soup = BeautifulSoup(page.text, 'html.parser')
            article_card = soup.find_all('article', class_="card")
            for article in article_card:
                article_img =  article.find("img", class_='card__image', src=True)['src'].strip()
                # article_img = article.urlretrieve("img", class_='card__image' "...\img.jpg")
                # article_img =  article_card.find("img", class_='card__image' )
                article_title =  article.find("h3", class_='card__title' ).text.strip()
                article_descr =  article.find('div', class_="card__content").text.strip()
                icon=article.find("i", class_='inline-icon inline-icon--secondary material-icons')
                icon.decompose() 
                article_loc =  article.find('div', class_='card__note d-none d-lg-block').text.strip()
                # for art in article_loc:   
                article_url = article.find('a', class_='overlay-link', href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n'+article_descr+'\nLocacija: <b>'+article_loc+'</b>\n'+ article_url+'\n'
                bot.send_message(message.chat.id,caption)
                bot.send_photo(message.chat.id,article_img +'\n' )  
                
        if message.text == 'V':
            # header = 
            url='https://liepaja.travel/darit-redzet/kultura-un-tradicijas/'
            page = requests.get(url)
            # page = requests(url )
            soup = BeautifulSoup(page.text, 'html.parser')
            article_card = soup.find_all('article', class_="card")
            for article in article_card:
                article_img =  article.find("img", class_='card__image', src=True)['src'].strip()
                # article_img = article.urlretrieve("img", class_='card__image' "...\img.jpg")
                # article_img =  article_card.find("img", class_='card__image' )
                article_title =  article.find("h3", class_='card__title' ).text.strip()
                article_descr =  article.find('div', class_="card__content").text.strip()
                icon=article.find("i", class_='inline-icon inline-icon--secondary material-icons')
                icon.decompose() 
                article_loc =  article.find('div', class_='card__note d-none d-lg-block').text.strip()
                # for art in article_loc:   
                article_url = article.find('a', class_='overlay-link', href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n'+article_descr+'\nLocacija: <b>'+article_loc+'</b>\n'+ article_url+'\n'
                bot.send_message(message.chat.id,caption)
                bot.send_photo(message.chat.id,article_img +'\n' )  
                
        if message.text == 'S':
            # header = 
            url='https://liepaja.travel/darit-redzet/apskates-vietas/'
            page = requests.get(url)
            # page = requests(url )
            soup = BeautifulSoup(page.text, 'html.parser')
            article_card = soup.find_all('article', class_="card")
            for article in article_card:
                article_img =  article.find("img", class_='card__image', src=True)['src'].strip()
                # article_img = article.urlretrieve("img", class_='card__image' "...\img.jpg")
                # article_img =  article_card.find("img", class_='card__image' )
                article_title =  article.find("h3", class_='card__title' ).text.strip()
                article_descr =  article.find('div', class_="card__content").text.strip()
                icon=article.find("i", class_='inline-icon inline-icon--secondary material-icons')
                icon.decompose() 
                article_loc =  article.find('div', class_='card__note d-none d-lg-block').text.strip()
                # for art in article_loc:   
                article_url = article.find('a', class_='overlay-link', href=True)['href'].strip()
                caption = '<b>'+article_title+'</b>\n'+article_descr+'\nLocacija: <b>'+article_loc+'</b>\n'+ article_url+'\n'
                bot.send_message(message.chat.id,caption)
                bot.send_photo(message.chat.id,article_img +'\n' )  
                
        

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data =='med':
                helpi = '🚑 Neatliekamā medicīniskā palīdzība - 113 \n🚒 Ugunsdzēsības dienests - 112 \n🚓 Policija - 110'
                bot.send_message(call.message.chat.id, helpi)
                # bot.send_message()
            elif call.data == 'Travel':
                pho = '+3712940211'
                emai= 'info@liepaja.travel'
                loc = 'Rožu laukums 5/6'
                conta = '📞 '+(str(pho))+'\n📃 '+(str(emai)) + '\n🌍 '+(str('Rožu laukums 5/6')) +'\n' 
                bot.send_message(call.message.chat.id,conta)
                # print(cont)


                # helpiss = '🚓 Policija - 110'
    except Exception as e:
        print(repr(e))
                # bot.send_message(call.message.chat.id, helpiss)
# @bot.message_handler(content_types=['text'])
#RUN
# bot.polling(none_stop=True, interval=0) 
@server.route('/'+config.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(requests.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook(url='https://morning-cove-27367.herokuapp.com/'+ config.TOKEN)
    return "!", 200

if __name__ == "__name__":
    server.run(host="0.0.0.0", post=int(os.environ.get('PORT',5000)))