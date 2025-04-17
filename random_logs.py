
import random
from analyzer import analyze_all

def makeRandomList():
    """
        Cookieとrandom.txtからランダムリストを作成する
        
        Args:
            logs_list (list): ランダム回答で使用するリスト
        
    """
    with open("templates/files/random.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    
    random_str = random.choice(lines).rstrip("\n")
    
    return random_str


def makeRandomList2(logs_list):
    """
        Cookieとrandom.txtからランダムリストを作成する
        
        Args:
            logs_list (list): ランダム回答で使用するリスト
        
    """
    with open("templates/files/random.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    if "" in logs_list:
        logs_list.remove("")
    new_lines = logs_list + lines
    #print("new_lines : ", new_lines)
    random_line = random.choice(new_lines).rstrip("\n")
    #print(random_line)
    random_lines = analyze_all(random_line)
    
    #print(random_lines)
    result = ""
    for line in random_lines:
        logs_str = "".join(logs_list)
        random_logs = analyze_all(logs_str)
        log_word = random.choice(random_logs)
        #print(log_word)
        if line[1] == log_word[1] and line[2] == log_word[2]:
            result += log_word[0]
            #print("log")
        else:
            result += line[0]
            #print("line")
    
    return result


if __name__ == "__main__":
    print(makeRandomList2(["坊主が上手に屏風に坊主の絵を描いた","ころね食べたいね","こんばんはって言ってみなよ。言えるものならね"]))