import praw
import json
import os
import sys

def credentials():
	f = open("config.json", "r")
	data = json.load(f)
	cred = (data["id"], data["secret"], data["agent"], data["user"], data["pass"])
	f.close()
	return cred

reddit = praw.Reddit(client_id=credentials()[0],
                     client_secret=credentials()[1],
                     user_agent=credentials()[2],
                     username=credentials()[3],
                     password=credentials()[4])


