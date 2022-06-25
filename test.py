import requests 

api = "https://dog.ceo/api/breeds/image/random"

r = requests.get(api)

imagem = r.json()['message']

hooks = open("hooks.txt", 'r')
print("webhook file fond, all good for now")

payload = {
    'content': imagem
}
for hook in hooks:
    r=requests.post(hook, data=payload)
    print("message sent")
