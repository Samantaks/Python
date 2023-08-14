import requests

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    

cep = '65053190'


dados_cep = consultar_cep(cep)
print(dados_cep)
    