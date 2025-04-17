import datetime
import os
import random
from typing import List
from flask import Flask, json, make_response, redirect, render_template, request, session, url_for
from dotenv import load_dotenv
from selenium import webdriver
from random_logs import makeRandomList, makeRandomList2
from random_sentence import makeSentenceList, makeSentenceList2


app: Flask = Flask(__name__, static_folder='static')  
    
# 環境変数を読み込み、セッションのシークレットキーを設定
load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

def initialize_session():
    session.clear()
    session["user_logs"] = [
        
    ]
    session["youmu_logs"] = [
        
    ]
    
@app.route("/")
def index():
    initialize_session()
    return render_template("index.html")


@app.route("/talking")
def start_talking():
    
    return render_template("talking.html")


@app.route("/talking", methods=["POST"])
def talk():
    user_input: str = request.form.get("user_input") # ユーザーが送信したメッセージを取得
    user_storage: str = request.form.get("user_storage") # ローカルストレージのuser_logsを取得
    youmu_storage: str = request.form.get("youmu_storage") # ローカルストレージのyoumu_logsを取得
    
    user_s_list = user_storage.split(",") # user_storageで取得した文字列を分割して配列にする
    
    #print("user: ",user_storage, "youmu: ", youmu_storage)
    
    user_session: List = session["user_logs"] # セッションのuser_logsを取得
    
    # セッションuser_logsにuser_inputの値を加え、再度セッションuser_logsに設定する
    user_session.append(user_input) 
    session["user_logs"] = user_session
    
    youmu_session: List = session["youmu_logs"] # セッションのyoumu_logsを取得
    
    piyo_list = ["ぴよぴよ！","ぴよっ！","ぴー！","ぴよぴよぴよぴよ・・・！"]
    rand_int = random.randint(0, len(user_s_list)+5)
    if rand_int <= 1 + len(user_s_list) % 2: # ぴよぴよと返す
        youmu_message = random.choice(piyo_list)
        youmu_session.append(youmu_message)
        #print("ぴよ")
    elif rand_int <= 2 + len(user_s_list) % 3: # オウム返し
        youmu_message = user_input
        youmu_session.append(user_input)
        #print("オウム返し")
    elif rand_int <= 6 + len(user_s_list) % 5: # random.txt、またはuser_storageからランダムに文章を抽出する
        youmu_message = makeRandomList()
        youmu_session.append(youmu_message)
        #print("ランダム1")
    elif rand_int <=  len(user_s_list) / 2 + 4: # random.txt、またはuser_storageからランダムに文章を抽出する
        youmu_message = makeRandomList2(list(user_s_list))
        youmu_session.append(youmu_message)
        #print("ランダム2")
    elif rand_int <= len(user_s_list) / 2 + 8 and len(user_s_list) >= 7: # user_storageと鳥の冒険.txtを混ぜて文章にする
        youmu_message = makeSentenceList2(user_storage)
        youmu_session.append(youmu_message)
        #print("センテンス2")
    elif rand_int <= len(user_s_list) + 2 and len(user_s_list) >= 7: # 単語集と鳥の冒険.txtを混ぜて文章にする
        youmu_message = makeSentenceList()
        youmu_session.append(youmu_message)
        #print("センテンス1")
    else:
        youmu_message = random.choice(piyo_list)
        youmu_session.append(youmu_message)
        #print("ぴよ")
    
    session["youmu_logs"] = youmu_session
    print(len(user_s_list))
    print("ぴよ", 1 + len(user_s_list) % 2, "オウム返し", 2 + len(user_s_list) % 3, "ランダム1", 4 + len(user_s_list) % 5,
          "ランダム2", len(user_s_list) / 2 + 1, "センテンス2", len(user_s_list) / 2 + 8, "センテンス1", len(user_s_list) + 2)
    message = youmu_message
    #print("message",message)
    #print("user_session: ", session["user_logs"], "youmu_session: ", session["youmu_logs"])
    
    if user_storage == None:
        user_storage = ""
    
    user_storage += user_input + ","
    
    if youmu_storage == None:
        youmu_storage = ""
    
    youmu_storage += message + ","
        
    print("user_storage: ", user_storage, "youmu_storage: ", youmu_storage)
    
    return render_template("talking.html", 
                           logs=zip(user_session, youmu_session), 
                           message=message,
                           user_storage=user_storage,
                           youmu_storage=youmu_storage)

    
if __name__ == "__main__":
    app.run(debug=True)

