import requests
import cards_division

url='https://api.shisanshui.rtxux.xyz'
cards_list = []
max_list = []
def sign_in(username,password):
    global url
    payload={"username":username,"password":password}
    headers={'content-type': "application/json"}
    r=requests.post(url+'/auth/login',json=payload,headers=headers)
    if r.status_code==200:
        data = r.json()
        status = data['status']
        if status==0:
            token = data.get('data').get('token')
            f = open('token.txt', 'w')
            f.write(token)
            f.close()
            f=open('user_id.txt','w')
            user_id=data.get('data').get('user_id')
            f.write(str(user_id))
            f.close
        return status
    else:
        return r.status_code

def register(username,password):
    global url
    payload = {"username": username, "password": password}
    headers = {'content-type': "application/json"}
    r = requests.post(url + '/auth/register', json=payload,headers=headers)
    if r.status_code==200:
        data = r.json()
        status = data['status']
        return status
    else:
        return r.status_code

def logout():
    global url
    f = open('token.txt')
    token = f.readline()
    f.close
    headers = {"X-Auth-Token": token}
    r = requests.post(url + '/auth/logout', headers=headers)
    data = r.json()
    status = data['status']
    return status

def new_game_and_play():
    global url
    f=open('token.txt')
    token=f.readline()
    f.close
    headers={"X-Auth-Token":token}
    r=requests.post(url+'/game/open',headers=headers)
    data=r.json()
    print(data)
    status = data['status']
    game_id=data.get('data').get('id')
    cards_string=data.get('data').get('card')
    global cards_list
    global max_list
    cards_list=cards_string.split(' ')
    max_list=cards_division.divide_cards(cards_list)
    front = ' '.join(max_list[10:13])
    middle = ' '.join(max_list[5:10])
    rear = ' '.join(max_list[0:5])
    payload={
        "id":game_id,
        "card":[
            front,
            middle,
            rear
        ]
    }
    print(payload)
    headers = {
        'content-type': "application/json",
        "X-Auth-Token": token
    }
    r2=requests.post(url+'/game/submit',json=payload,headers=headers)
    data=r2.json()
    status2=data.get("status")
    print(status2)
    for i in range(0,13):
        if max_list[i][0]=='*':
            max_list[i]='^'+max_list[i][1:]
    return max_list

def get_rank():
    global url
    r=requests.get(url+'/game/rank')
    data=r.json()
    return data

def get_history_list(limit,page):
    global url
    f = open('token.txt')
    token = f.readline()
    f.close
    f = open('user_id.txt')
    user_id = int(f.readline())
    f.close
    params={
        "player_id":user_id,
        "limit":limit,
        "page":page
    }
    headers = {
        'content-type': "application/json",
        "X-Auth-Token": token
    }
    r=requests.get(url+'/history',params=params,headers=headers)
    data=r.json()
    return data

def get_history_details(game_id):
    global url
    f = open('token.txt')
    token = f.readline()
    f.close
    headers = {
        'content-type': "application/json",
        "X-Auth-Token": token
    }
    r = requests.get(url + '/history/'+str(game_id),headers=headers)
    data = r.json()
    return data

if __name__=='__main__':
    print(sign_in('111666','111666'))
    print(get_history_list(20,1))




