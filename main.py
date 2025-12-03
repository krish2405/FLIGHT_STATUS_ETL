import requests
import json
import logging
import csv


logging.basicConfig(filename="etl_error.log", level=logging.INFO)
url_user = "https://jsonplaceholder.typicode.com/users"
url_post="https://jsonplaceholder.typicode.com/posts"

response_user = requests.get(url_user)
print(response_user.status_code)
user_table=[]
post_table=[]
if response_user.status_code==200:
        users =response_user.json()
        if len(users):
                for user in users:
                    try:
                        if  user['name'] and user['email'] and user['address']['city'] and ('@' in user['email']):
                            print(user)
                            user_table.append({
                                          'user_id': user.get('id'),
                                          'name': user.get('name'),
                                           'email':user.get('email'),
                                           'city': user.get('address').get('city'),
                                           'latitude': user.get('address').get('geo').get('lat'),
                                           'longitude': user.get('address').get('geo').get('lng'),
                                           'company':user.get('company').get('name')
                                     })
                            
                    except Exception as ES:
                           logging.info(f"{ES}")
                           exit()

else:
    logging.info(f"User API failed with status {response_user.status_code}")
    exit()

print("Users extracted:", len(user_table))
  
with open("din_user.csv",'w') as du:
    writer=csv.DictWriter(du,fieldnames=['user_id','name','email','city','latitude','longitude','company'])
    writer.writeheader()
    print("-------------------------------")
    # print(user_table) 
    writer.writerows(user_table)

response_posts = requests.get(url_post)
print(response_posts .status_code)
if response_posts .status_code==200:
        posts =response_posts.json()
        if len(posts):
                for post in posts:
                    try:
                        if  post['userId'] and post['id'] and post['title']:
                               pass
                    
                    except Exception as ES:
                           logging.info(f"{ES}")
                           exit
                
                           
                           
                    
        
        print(posts)

with open("city_regions.json",'r') as jr:
        city_regions=json.load(jr)
        print(city_regions)


 