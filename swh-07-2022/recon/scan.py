import requests

"""
lista = [
    "/admin",
    "/index.php",
    "/admin.php",
    "/backend",
    "/app.js",
    "/.htaccess",
    "/login",
    "/flag.txt",
    "/flag"
]
"""
lista = open('arquivos.txt','r')
# lista = open('big.txt', 'r')
# lista = open('common.txt', 'r')
site = "https://worksn.com.br/"

for item in lista.readlines():
    request = requests.get(site + item)
    tamanho_resposta = len(request.text)

    if(tamanho_resposta > 0):
        print("Arquivo encontrado: "+site+item)
    #if(request.status_code == 200):
        #print("Arquivo encontrado: "+item)
