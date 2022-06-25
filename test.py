import requests 

api = "https://dog.ceo/api/breeds/image/random"

r = requests.get(api)

imagem = r.json()['message']
print(r.json()['status'])

hooks = open("hooks.txt", 'r')
print(f"webhook file fond, all good for now {hooks}")

payload = {
    'content': imagem
}
for hook in hooks.read():
    r=requests.post(hook, data=payload)
    print("message sent")
