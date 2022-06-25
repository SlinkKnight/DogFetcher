import requests 

api = "https://dog.ceo/api/breeds/image/random"

r = requests.get(api)

imagem = r.json()['message']
print(r.json()['status'])

f = open("hooks.txt", 'r')

hooks = f.read()
print(f"webhook file fond, all good for now {hooks}")

payload = {
    'content': imagem
}
for hook in hooks:
    r=requests.post(hook, data=payload)
    print("message sent")
