import requests
from discord.ext import commands
from discord.utils import get
import random

with open("tokens.txt", "r") as file:
    allText = file.read()
    tokens = list(map(str, allText.split()))
    random.shuffle(tokens)

proxies = {
   'http': 'http://xxx:xxx@xxx.com:xxx',
   'https': 'http://xxx:xxx@xxx.com:xxx',
}

channelid = "333333333333333333"
messageid = "333333333333333333"

emoji1= "\U0001F525"
emoji2= "\U0001F680"
emoji3= "\U0001F4AF"
emoji4= "\U0001F4AA"
emoji5= "\U00002705"
emoji6= "\U0001F44D"
emoji7= "\U0001F60D"

emoji1count=0
emoji2count=0
emoji3count=0
emoji4count=0
emoji5count=0
emoji6count=0
emoji7count=0

emoji1maks=random.randint(50,55)
emoji2maks=random.randint(45,50)
emoji3maks=random.randint(40,45)
emoji4maks=random.randint(35,40)
emoji5maks=random.randint(30,35)
emoji6maks=random.randint(25,30)
emoji7maks=random.randint(20,25)

for x in range(1000):
    def react1():
        global emoji1count
        global emoji2count
        global emoji3count
        global emoji4count
        global emoji5count
        global emoji6count
        global emoji7count
        token = {
                'authorization': "{token}".format(token=tokens[x])
        }
        print(token)
        react1=emoji1
        react2=emoji2
        react3=emoji3
        react4=emoji4
        react5=emoji5
        react6=emoji6
        react7=emoji7
        url = (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react1}/@me")
        url2= (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react2}/@me")
        url3= (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react3}/@me")
        url4= (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react4}/@me")
        url5= (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react5}/@me")
        url6= (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react6}/@me")
        url7= (f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{react7}/@me")
       
        #1111111111111111
        print(emoji1count)
        if emoji1count < emoji1maks:
            requests.put(url,headers=token, proxies=proxies)
            emoji1count+=1
        else:
            print(emoji1+" reached limit."+"("+str(emoji1maks)+")")
            pass

        #2222222222222222
        print(emoji2count)
        if emoji2count < emoji2maks:
            requests.put(url2,headers=token, proxies=proxies)
            emoji2count+=1
        else:
            print(emoji2+" reached limit."+"("+str(emoji2maks)+")")      
            pass
        
        #3333333333333333
        print(emoji3count)
        if emoji3count < emoji3maks:
            requests.put(url3,headers=token, proxies=proxies)
            emoji3count+=1
        else:
            print(emoji3+" reached limit."+"("+str(emoji3maks)+")")   
            pass          
        
        #4444444444444444
        print(emoji4count)
        if emoji4count < emoji4maks:
            requests.put(url4,headers=token, proxies=proxies)
            emoji4count+=1
        else:
            print(emoji4+" reached limit."+"("+str(emoji4maks)+")")   
            pass    
        #5555555555555555
        print(emoji5count)
        if emoji5count < emoji5maks:
            requests.put(url5,headers=token, proxies=proxies)
            emoji5count+=1
        else:
            print(emoji5+" reached limit."+"("+str(emoji5maks)+")")   
            pass        
        
        #6666666666666666
        print(emoji6count)
        if emoji6count < emoji6maks:
            requests.put(url6,headers=token, proxies=proxies)
            emoji6count+=1
        else:
            print(emoji6+" reached limit."+"("+str(emoji6maks)+")")   
            pass      

        #7777777777777777
        print(emoji7count)
        if emoji7count < emoji7maks:
            requests.put(url7,headers=token, proxies=proxies)
            emoji7count+=1
        else:
            print(emoji7+" reached limit."+"("+str(emoji7maks)+")")   
            pass        
    react1()