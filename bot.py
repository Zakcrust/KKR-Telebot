import telebot
from flask import Flask, request
from crontab import CronTab
import os
import random
import time


#add new cron job
job  = CronTab().new(command='/usr/bin/echo')

#job settings
job.hour.every(1)


class data_bot:

    def __init__(self, started_game = False, cid = ""):
        self. started_game = started_game
        self.cid = cid


    def get_started_game(self):
        return self.started_game


    def get_cid(self):
        return self.cid

    
    def set_started_game(self, x):
        self.started_game = x
    

    def set_cid(self, x):
        self.cid = x

    
    pass


class rmath:

    def __init__(self, rmath_started = False, answer = 0):
        self.rmath_started = rmath_started
        self.answer = answer

    def get_rmath_started(self):
        return self.rmath_started


    def get_answer(self):
        return self.answer


    def set_rmath_started(self, x):
        self.rmath_started = x
    
    
    def set_answer(self, x):
        self.answer = x

    pass


class findxsquare:

    def __init__(self, xsquare_started = False, answer1 = 0, answer2 = 0, answer1_found = False, answer2_found = False):
        self.xsquare_started = xsquare_started
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer1_found = answer1_found
        self.answer2_found = answer2_found


    def get_findxsquare_started(self):
        return self.xsquare_started


    def get_answer1(self):
        return self.answer1


    def get_answer2(self):
        return self.answer2

    def get_answer1_found(self):
        return self.answer1_found

    def get_answer2_found(self):
        return self.answer2_found


    def set_findxsquare_started(self, x):
        self.xsquare_started = x


    def set_answer1(self, x):
        self.answer1 = x

    def set_answer2(self, x):
        self.answer2 = x

    def set_answer1_found(self, x):
        self.answer1_found = x

    def set_answer2_found(self, x):
        self.answer2_found = x    


    def reset_answer_found(self):
        self.answer1_found = False
        self.answer2_found = False

    def any_value_answered(self):
        return (self.answer1_found or self.answer2_found)

    def all_values_answered(self):
        return (self.answer1_found and self.answer2_found)
            
    pass


class data_user:

    def __init__(self, user = [],user_id = "",xp = 0 ,level = 0):
        self.user = user
        user_id = ""
        xp = 0
        level = 0
    
    pass
## Telebot token intialization
TOKEN = "INSERT TELEGRAM BOT TOKEN"
bot = telebot.TeleBot(token=TOKEN)

## Flask server initialization
server = Flask(__name__)


def bot_timer(seconds):
    t = time.process_time()
    elapsed_time = time.process_time() - t
    while elapsed_time < float(seconds):
        elapsed_time = time.process_time() - t
        pass
    pass

def bot_timer_timeout():
    timeout = True
    pass

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['hello']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Welcome to KKR '+message.from_user.first_name+'!')

@bot.message_handler(commands=['help']) # help message handler
def send_help(message):
    bot.reply_to(message, '/hello\n/rmath - Start a mini-game (some random math equations)\n/findxsquare - Start a mini-game (random algebra x-square equations)')
    
@bot.message_handler(commands=['findxsquare'])
def find_x_square(message):
    DataBot.set_cid(message.chat.id)
    if DataBot.get_started_game() and FindXSquare.get_findxsquare_started():
        bot.send_message(message.chat.id,'A game is still running. finish the game by completing the challenges or use /finishgame')
    else:
        DataBot.set_started_game(True)
        FindXSquare.set_findxsquare_started(True)
        bot.send_message(message.chat.id,'A game just started.\nsome random equations will be appeared and you have to answer it correctly')
        random_game = random.randint(0,101)
        if random_game > 50:
            return xsquare_game(message)
        else:
            return xsquare_game_advanced(message)

def xsquare_game(message):
    x = random.randint(-10,11)
    b_x = 2*x
    c = x*x
    FindXSquare.set_answer1(x)
    FindXSquare.set_answer2(x)
    question = "x^2 + "+str(b_x)+"x + "+str(c)
    bot.send_message(message.chat.id,question)
    pass

def xsquare_game_advanced(message):
    x1 = random.randint(-5,5)
    x2 = random.randint(-5,5)
    b_x = x1+x2
    c = x1*x2
    FindXSquare.set_answer1(x1)
    FindXSquare.set_answer2(x2)
    question = "x^2 + "+str(b_x)+"x + "+str(c)
    bot.send_message(message.chat.id,question)
    pass

@bot.message_handler(commands=['rmath'])
def random_number_math(message):
    DataBot.set_cid(message.chat.id)
    if DataBot.get_started_game() and RMath.get_rmath_started():
        bot.send_message(message.chat.id,'A game is still running. finish the game by completing the challenges or use /finishgame')
    else:
        DataBot.set_started_game(True)
        RMath.set_rmath_started(True)
        bot.send_message(message.chat.id,'A game just started.\nsome random equations will be appeared and you have to answer it correctly')
        return rmath_game(message)


def rmath_game(message):
    print(DataBot.get_started_game())
    print(RMath.get_rmath_started())
    if DataBot.get_started_game() and RMath.get_rmath_started():
            print("game started")
            opr1 = random.randint(1, 101)
            opr2 = random.randint(1, 101)
            answer = opr1 + opr2
            RMath.set_answer(answer)
            msg = bot.send_message(message.chat.id, str(opr1)+' + '+str(opr2)+' = ')
            print(msg)
            return msg
    pass


@bot.message_handler(commands=['finishgame'])
def finish_current_game(message):
    if DataBot.get_started_game():
        DataBot.set_started_game(False)

        if RMath.get_rmath_started():
            RMath.set_rmath_started(False)

        if FindXSquare.get_findxsquare_started():
            FindXSquare.set_findxsquare_started(False)

        bot.send_message(message.chat.id,'game has been ended')
    else:
        bot.send_message(message.chat.id,'no game is running')
    pass


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_user_answer(message):
    print(message.text)
    print(DataBot.get_cid())
    if DataBot.get_started_game():

        if RMath.get_rmath_started():
            print(RMath.get_answer())
            if message.text == str(RMath.get_answer()):
                bot.send_message(DataBot.get_cid(),message.from_user.first_name+' has the answer. it is '+message.text)
                DataBot.set_started_game(False)
                RMath.set_rmath_started(False)
                bot.send_message(DataBot.get_cid(),'game has been ended')
            pass
        
        elif FindXSquare.get_findxsquare_started():
            print(FindXSquare.get_answer1())
            print(FindXSquare.get_answer2())

            if message.text == str(FindXSquare.get_answer1()) and (not FindXSquare.get_answer1_found()) :
                FindXSquare.set_answer1_found(True)
                bot.send_message(DataBot.get_cid(),message.from_user.first_name+' has the answer. it is '+message.text)    

                if FindXSquare.get_answer1() == FindXSquare.get_answer2() and FindXSquare.any_value_answered():
                    FindXSquare.reset_answer_found()
                    DataBot.set_started_game(False)
                    FindXSquare.set_findxsquare_started(False)
                    bot.send_message(DataBot.get_cid(),"Game has been ended")
    
                if not FindXSquare.all_values_answered():
                    bot.send_message(DataBot.get_cid(),"another x value is still not been answered")
                    return
                else:
                    FindXSquare.reset_answer_found()
                    DataBot.set_started_game(False)
                    FindXSquare.set_findxsquare_started(False)
                    bot.send_message(DataBot.get_cid(),"Game been ended")             
                
            elif message.text == str(FindXSquare.get_answer2()) and (not FindXSquare.get_answer2_found()) :
                FindXSquare.set_answer2_found(True)
                bot.send_message(DataBot.get_cid(),message.from_user.first_name+' has the answer. it is '+message.text)

                if FindXSquare.get_answer1() == FindXSquare.get_answer2() and FindXSquare.any_value_answered():
                    FindXSquare.reset_answer_found()
                    DataBot.set_started_game(False)
                    FindXSquare.set_findxsquare_started(False)
                    bot.send_message(DataBot.get_cid(),"Game has been ended")
                
                if not FindXSquare.all_values_answered():
                    bot.send_message(DataBot.get_cid(),"another x value is still not been answered")
                    return
                else:
                    FindXSquare.reset_answer_found()
                    DataBot.set_started_game(False)
                    FindXSquare.set_findxsquare_started(False)
                    bot.send_message(DataBot.get_cid(),"Game has been ended")

            pass


        pass

    pass



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-kkr.herokuapp.com/' + TOKEN)
    return "!", 200

    
if __name__ == "__main__":
    DataBot = data_bot()
    RMath = rmath()
    FindXSquare = findxsquare()
    print(data_bot().get_started_game())
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
