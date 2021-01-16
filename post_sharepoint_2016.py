import csv
import os
import requests
import time
import json
from requests_ntlm import HttpNtlmAuth

def post_to_sharepoint():

    username = ''
    password = ''
    folder_name = ''
    file_array = []

    # ******************************************************************************************
    # You cannot upload a variable to sharepoint. You must upload a file. This is file creation.

    # filepath to save files to local hard drive.
    save_file_path = "local_hd" + username + "folder_names"

    # Checks to see if the folder exists. If so it doesnt make the directory.
    # If it doesn't exist, it makes the directory.
    os.makedirs(save_file_path + "\\" + folder_name, exist_ok = True)

 

    full_save_path = save_file_path + "\\" + folder_name


    # this is everything needed to save a file

    file_name = "file_name.csv"

    file_name_path = full_save_path + "\\" + file_name

    # w means write the file. We're building a new file whether one exists or not. 
    # It will write over the top of the current file with that name.
    with open(file_name_path, 'w', newline="") as finished:
        write_function = csv.writer(finished)
        write_function.writerows(file_array)

   # ******************************************************************************************
   # All SharePoint from Here down

    sharePointUrl = ''
    sharepoint_folder = ''

    folderUrl = 'sharepoint_folders'

    folderUrl = folderUrl + sharepoint_folder


    # Sets up the url for requesting a file upload
    requestUrl = sharePointUrl + "/_api/web/GetFolderByServerRelativeUrl('" + folderUrl + "')/Files/add(url='" + file_name + "',overwrite='true')"


    file = open(file_name_path, 'rb')



    # Setup the required headers for communicating with SharePoint
    # Using JSon to get information to SharePoint. Sneaky, but works.

    headers = {'Content-Type': 'application/json; odata=verbose', 'accept': 'application/json;odata=verbose'}

    

    # Execute a request to get the FormDigestValue. This will be used to authenticate our upload request

    r = requests.post(sharePointUrl + "/_api/contextinfo",auth=HttpNtlmAuth(username,password), headers=headers, verify=False)



    formDigestValue = r.json()['d']['GetContextWebInformation']['FormDigestValue']

    # print(formDigestValue)

    # Update headers to use the newly acquired FormDigestValue

    POSTheaders = {'Accept':'application/json; odata=verbose','Content-Type':'application/json; odata=verbose', 'X-RequestDigest':formDigestValue, 'binaryStringRequestBody':'true'}

    

    # Execute the request. If you run into issues, inspect the contents of uploadResult
    # Covid-19 caused working from home. Member would have network latency issues. three second retry fixed the problem. 

    try:

        requests.post(requestUrl,auth=HttpNtlmAuth(username,password), headers=POSTheaders, data=file.read(), verify = False)

    except:

        time.sleep(3)

        requests.post(requestUrl,auth=HttpNtlmAuth(username,password), headers=POSTheaders, data=file.read(), verify = False)

    # print(uploadResult.content)


post_to_sharepoint()
