import random
from analyzer import analyze_all


def selectRandomWord(list_str, speechs, rand, noun=False):
    new_speechs = []
    for speech in speechs:
        speech_list = speech.split("\t")
        if noun:
            if "特殊" in speech_list[1]:
                continue
            rand_noun = random.randint(0, 10)
            if rand_noun <= 2:
                p = str(speech_list[0])
                new_speechs.append(p)
            else:
                if speech_list[1] == list_str[1] and speech_list[2] == list_str[2]:
                    p = str(speech_list[0])
                    new_speechs.append(p)
        else:
            if speech_list[1] == list_str[1] and speech_list[2] == list_str[2]:
                p = str(speech_list[0])
                new_speechs.append(p)
            
    if new_speechs:
        rand_int = random.randint(0, 10)
        if rand_int <= rand:
            new_speech = random.choice(new_speechs)
            return new_speech
        else:
            return list_str[0]
    else:
        return list_str[0]
        

def makeSentenceList():
    """
        
    """
    with open("templates/files/鳥の冒険.txt", 'r', encoding='utf_8') as f:
        lines = f.readlines()
    
    with open("templates/words/ヨウム_名詞.txt", "r", encoding="utf-8") as f:
        nouns = f.readlines()
            
    with open("templates/words/ヨウム_助動詞.txt", "r", encoding="utf-8") as f:
        auxiliary_verbs = f.readlines()
        
    with open("templates/words/ヨウム_助詞.txt", "r", encoding="utf-8") as f:
        particles = f.readlines()
    
    with open("templates/words/ヨウム_動詞.txt", "r", encoding="utf-8") as f:
        verbs = f.readlines()
        
    with open("templates/words/ヨウム_感動詞.txt", "r", encoding="utf-8") as f:
        f_verbs = f.readlines()
        
    random_str = random.choice(lines)
    #print(random_str)
    
    analyzed_list = analyze_all(random_str)
    
    new_str = ""
    rand_feel = random.randint(0,10)
    if rand_feel <= 4:
        feel = random.choice(f_verbs)
        feel_list = feel.split("\t")
        new_str += feel_list[0] + "、"
        
    for list_str in analyzed_list:
        if "括弧" in list_str[1]:
            continue
        if "代名詞," in list_str[1]:
            new_str += list_str[0]
            
        elif "名詞," in list_str[1]:
            new_str += selectRandomWord(list_str, nouns, 8, True)
            
        elif "助動詞," in list_str[1]:
            new_str += selectRandomWord(list_str, auxiliary_verbs, 1)
                            
        elif "助詞," in list_str[1]:
            new_str += selectRandomWord(list_str, particles, 1)
                
        elif "動詞," in list_str[1]:
            new_verbs = []
            for verb in verbs:
                verb_list = verb.split("\t")
                if verb_list[1] == list_str[1]\
                    and verb_list[2] == list_str[2]\
                        and verb_list[0][-1] == list_str[0][-1]:
                    v = str(verb_list[0])
                    #print(verb_list[0] + "===" + list_str[0])
                    new_verbs.append(v)
            if new_verbs:
                rand_int = random.randint(0, 10)
                if rand_int <= 5:
                    new_verb = random.choice(new_verbs)
                    #print("動詞: ", new_verb)
                    new_str += new_verb
                else:
                    new_str += list_str[0]
            else:
                new_str += list_str[0]
        else:
            new_str += list_str[0]
        #print(list_str)
        
    result = new_str.rstrip("。") + "！"
    
    return result
        

def makeSentenceList2(storage):
    """

    Args:
        storage (_type_): _description_

    Returns:
        _type_: _description_
    """
    items = analyze_all(storage)
    storage_list = storage.split(",")
    
    with open("templates/files/鳥の冒険.txt", 'r', encoding='utf_8') as f:
        lines = f.readlines()
        
    text = random.choice(lines)
    
    line_list = analyze_all(text)
    
    new_words = []
    for item in storage_list:
        analyzed_items = analyze_all(item)
        #print(analyzed_items)
        for analyzed_item in analyzed_items:
            if "名詞," in analyzed_item[1]:
                new_words.append(analyzed_item[0])
            
    #print(new_storage)
    
    result = ""
    for line in line_list:
        if "記号,括弧" in line[1]:
            continue
        rand_storage = random.choice(storage_list)
        items = analyze_all(rand_storage)
        if items == []:
            result += line[0]
            continue
        item = random.choice(items)
        #print("item: ",item)
        #print("line: ",line)
        if line[1] == item[1] and line[2] == item[2]:
                
            result += item[0]
                
        else:
            rand_int = random.randint(0,5)
            if rand_int < 3:
                result += line[0]
            elif rand_int < 4:
                if len(new_words) == 0:
                    result += line[0]
                else:
                    word = random.choice(new_words)
                    result += word
             
    result = result.rstrip("。")
    result += "！？"
    return result

                
if __name__ == "__main__":
    #print(makeMarkovList("おはよう、こんにちは、そしてこんばんは\n"))
    print(makeSentenceList2("忍者って何がすごいのか,侍の魂を持っていらっしゃる,とにかく面白い文章を書けるといいよね"))