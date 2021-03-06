import requests
from config import api_key
import pymongo

##########################
##### Query From API #####
##########################

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.homes_db

def query_city(region_id, num_homes):

    url = "https://unofficial-redfin.p.rapidapi.com/properties/list"
 
    querystring = {
		"region_id":region_id,
		"region_type":"6",
		"uipt":"1,2,3,4,7,8",
		"status":"9",
		"num_homes":num_homes,
		}

    headers = {
		"X-RapidAPI-Key": api_key,
		"X-RapidAPI-Host": "unofficial-redfin.p.rapidapi.com"
	}

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
	
    query_dict = {
        'region_id': int(region_id),
		'response_json': data,
	}
	
    return query_dict

# populate_db function queries with the following region ids for dev purposes
# def populate_db():
#     region_id = [29470, 18142, 30756, 17151, 30818]
#     for i in region_id:
#         q = query_city(i, 50)
#         db.cities.insert_one(q)
# populate_db()