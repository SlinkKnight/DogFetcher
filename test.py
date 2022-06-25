import requests 

api="https://dog.ceo/api/breeds/image/random"
r=requests.get(api)
imagem=r.json()['message']
payload={
    'content': imagem
}
r=requests.post("https://discord.com/api/webhooks/976193399810064424/-2viIUqPyvMaLTHJcHwDNQ9F4EfkVLJbahs7F6EUHU41T-MkI6hz2JZcfyzWy05qCWgN",data=payload)