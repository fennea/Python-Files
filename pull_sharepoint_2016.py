import requests
from requests_ntlm import HttpNtlmAuth
import csv

def get_roster(username, password):

    site_url = ""


    file_name = '' # should include file extension

    full_url = site_url + file_name

   

    headers = {'accept': 'application/json;odata=verbose'}

    user_request = requests.get(full_url, headers=headers, auth=HttpNtlmAuth(username, password), verify=False)

 

    read_wrapper = csv.reader(user_request.text.strip().split('\n'))

    full_roster = list(read_wrapper)

 

    return full_roster

username = ''
password = ''

get_roster(username, password)