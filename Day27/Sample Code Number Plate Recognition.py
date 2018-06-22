# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:37:59 2018

@author: reeti
"""

 #Description:Car License plate detection of Great Britain
 #Author: Forsk Technologies
 #Version:1.1
 #Revision Date:27/08/2016


from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("63f13516-7ff4-4f9b-b7fb-67360cecf331", "v1") #apikey

params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
#params = {'file': 'E:/abcd.mp4', 'source_location': 'GB'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print response

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)