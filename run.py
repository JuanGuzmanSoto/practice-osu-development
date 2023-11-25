import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_osu_user_stats(username):
    url = "https://osu.ppy.sh/api/get_user"
    params = {
        'k': os.getenv('OSU_API_KEY'), 
        'u': username
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        user_data = response.json()[0]
        return {
            'username': user_data['username'],
            'rank': user_data['pp_rank'],
            'performance_points': user_data['pp_raw']
        }
    else:
        return f"Error: {response.status_code}"

username = input("Enter osu! username: ")
user_stats = get_osu_user_stats(username)
print(user_stats)