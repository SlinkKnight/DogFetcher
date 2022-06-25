import requests 

api="https://dog.ceo/api/breeds/image/random"
r=requests.get(api)
imagem=r.json()['message']
payload={
    'content': imagem
}
r=requests.post(open("hooks.txt", 'r'),data=payload)
