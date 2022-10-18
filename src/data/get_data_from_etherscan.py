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