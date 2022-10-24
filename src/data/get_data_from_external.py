#Getting data from external sources - blockchain explorers - Etherscan, Ethplorer, GCP

from bs4 import BeautifulSoup
import json
import cloudscraper

def wallet_normal_transactions(address, api_key):

    scraper = cloudscraper.create_scraper()

    response = scraper.get("http://api.etherscan.io/api?module=account&action=txlist&address="+address+"&startblock=0&endblock=99999999&sort=asc&apikey="+api_key)
    normal_txn = json.loads(BeautifulSoup(response.text, 'html.parser').text)['result']
    
    return normal_txn

def wallet_internal_transactions(address, api_key):

    scraper = cloudscraper.create_scraper()

    response = scraper.get("http://api.etherscan.io/api?module=account&action=txlistinternal&address="+address+"&startblock=0&endblock=99999999&sort=asc&apikey="+api_key)
    internal_txn = json.loads(BeautifulSoup(response.text, 'html.parser').text)['result']
    
    return internal_txn

def wallet_token_balance(address, token_address, api_key):
    #Returns the current balance of an ERC-20 token (token_address) of an address (address).

    scraper = cloudscraper.create_scraper()
    
    response = scraper.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress="+token_address+"&address="+address+"&apikey="+api_key)
    response_to_json = json.loads(BeautifulSoup(response.text, 'html.parser').text)
    token_balance_of_address = response_to_json['result']
        
    return token_balance_of_address

def wallet_balance(address,api_key):
    
    scraper = cloudscraper.create_scraper()

    response = scraper.get("http://api.ethplorer.io/getAddressInfo/"+address+"?apiKey="+api_key)
    html_soup = json.loads(BeautifulSoup(response.text, 'html.parser').text)
    eth_balance = html_soup['ETH']['balance']*html_soup['ETH']['price']['rate']
    
    tokens=pd.DataFrame(html_soup['tokens'])
    tokens['name']=tokens['tokenInfo'].apply(lambda x : x['name'] if 'name' in x else x['address'])
    tokens['decimals']=tokens['tokenInfo'].apply(lambda x : int(x['decimals']))
    tokens['symbol']=tokens['tokenInfo'].apply(lambda x : str(x['symbol']).lower().replace(" ", ""))
    tokens['price USD'] = [0 if i not in a_dictionary else i for i in tokens['symbol']]
    tokens['price USD'] = tokens['price USD'].replace(a_dictionary).astype(float)
    tokens['balance']=tokens['balance']/(10**tokens['decimals'].values)
    tokens=tokens[tokens['price USD']!='False'][['name','balance','price USD']]
    tokens['total']=tokens['balance']*tokens['price USD']
    tokens=tokens.sort_values(by='total',ascending=False)
    tokens_balance = round(tokens.total.sum(),2)
    
    return [eth_balance,tokens_balance]