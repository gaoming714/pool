import os
import requests, json

# get IP from pool.jokepy.top, (or jokepy.top:8008 )
# return json
#{ "2miners":{"eth":"0.0.0.0:2020","ctxt":"1.1.1.1"}
#
# }

ip_res = requests.get("http://pool.pokescript.com/")
ip_str = json.loads(ip_res.text).get("2miners").get("ctxc")

# debug
# ip_str = "51.195.4.174"

with open('nickname.txt', 'r', encoding='utf-8') as f:
    nickname = f.read()


gminer_str = "miner" + " "
algo_str = "--algo cortex" + " "
server_str = "--server " + ip_str + " "
user_str = "--user 0xbb9085b9dce864400a5707928b1781e4ca398975." + nickname + " "
api_str = "--api 9000"


command = gminer_str + algo_str + server_str + user_str + api_str 

print(command)

os.system(command)