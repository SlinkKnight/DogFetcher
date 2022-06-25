import requests

api = "https://dog.ceo/api/breeds/image/random"

r = requests.get(api)

imagem = r.json()['message']
print(r.json()['status'])

f = open("python-vicenzo/hooks.txt", 'r')
 
hooks = f.readlines()
print(f"# webhook file found!, all good for now")

payload = {
    'content': imagem
}

for item in hooks:
    r = requests.post(item, data=payload)
    print(f"# code {r.status_code} in {item}")
    print(f"# discord responded with {r.content}")
