import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from PIL import Image, ImageTk  

load_dotenv()

def get_osu_user_stats(username):
    url = "https://osu.ppy.sh/api/get_user"
    params = {
        'k': os.getenv('OSU_API_KEY'),
        'u': username
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            user_data = response.json()[0]
            return user_data
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"
<<<<<<< HEAD
def get_user_top_play_and_beatmap(username):
    top_play_url = "https://osu.ppy.sh/api/get_user_best"
    params = {
        'k': os.getenv('OSU_API_KEY'),
        'u': username,
        'limit': 1  
    }

    try:
        top_play_response = requests.get(top_play_url, params=params)
        if top_play_response.status_code == 200:
            top_play_data = top_play_response.json()[0]
            beatmap_id = top_play_data['beatmap_id']
            
            
            beatmap_url = "https://osu.ppy.sh/api/get_beatmaps"
            beatmap_params = {
                'k': os.getenv('OSU_API_KEY'),
                'b': beatmap_id
            }
            beatmap_response = requests.get(beatmap_url, params=beatmap_params)
            if beatmap_response.status_code == 200:
                beatmap_data = beatmap_response.json()[0]
                
                image_url = f"https://b.ppy.sh/thumb/{beatmap_id}l.jpg"
                return {
                    'top_play': top_play_data,
                    'beatmap_image_url': image_url,
                    'beatmap': beatmap_data
                }
            else:
                print("Failed to fetch beatmap details")
                return None
        else:
            print("Failed to fetch user's top play")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

=======
>>>>>>> 2d1f7a9671b2aa94690632dd0d844a4e70a121b2

def fetch_avatar(url):
    try:
        response = requests.get(url)
<<<<<<< HEAD
        response.raise_for_status()  
=======
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
>>>>>>> 2d1f7a9671b2aa94690632dd0d844a4e70a121b2
        image = Image.open(requests.get(url, stream=True).raw)
        image.thumbnail((100, 100))  
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error fetching avatar: {e}")
        return None

def on_submit():
    username = user_name_entry.get()
    user_data = get_osu_user_stats(username)
<<<<<<< HEAD
    top_play_data = get_user_top_play_and_beatmap(username)

    if isinstance(user_data, dict):
        stats = (f"Username: {user_data['username']}\n"
                 f"Rank: {user_data['pp_rank']}\n"
                 f"Performance Points: {user_data['pp_raw']}\n"
                 f"Total Score: {user_data['total_score']}\n")
        if top_play_data:
        
            top_score_pp = top_play_data['top_play']['pp']
            beatmap_name = top_play_data['beatmap']['title']
            stats += f"Highest PP Score: {top_score_pp}\n"
            stats += f"Top Play Beatmap: {beatmap_name}\n"
            
           
            beatmap_image_url = top_play_data['beatmap_image_url']
            beatmap_image = fetch_avatar(beatmap_image_url)
            if beatmap_image:
                beatmap_image_label.config(image=beatmap_image)
                beatmap_image_label.image = beatmap_image
        avatar_url = f"https://a.ppy.sh/{user_data['user_id']}"  
=======

    if isinstance(user_data, dict):
        stats = f"Username: {user_data['username']}\nRank: {user_data['pp_rank']}\nPerformance Points: {user_data['pp_raw']}"
        avatar_url = f"https://a.ppy.sh/{user_data['user_id']}"
>>>>>>> 2d1f7a9671b2aa94690632dd0d844a4e70a121b2
        avatar_image = fetch_avatar(avatar_url)
        if avatar_image:
            avatar_label.config(image=avatar_image)
            avatar_label.image = avatar_image  
    else:
<<<<<<< HEAD
        stats = "Error fetching user data"

    result_label.config(text=stats)

root = tk.Tk()
root.title("osu! User Stats")


label = tk.Label(root, text="Enter osu! username:", bg='lightblue')
label.pack()
user_name_entry = tk.Entry(root, width=50)
user_name_entry.pack()
submit_button = tk.Button(root, text="Get Stats", command=on_submit)
submit_button.pack()
avatar_label = tk.Label(root, bg='lightblue')
avatar_label.pack()
result_label = tk.Label(root, text="", bg='lightblue')
result_label.pack()
beatmap_image_label = tk.Label(root)
beatmap_image_label.pack()


root.mainloop()
=======
        stats = user_data 

    result_label.config(text=stats)

# Set up the main window
root = tk.Tk()
root.title("osu! User Stats")

tk.Label(root, text="Enter osu! username:").pack()
user_name_entry = tk.Entry(root)
user_name_entry.pack()
submit_button = tk.Button(root, text="Get Stats", command=on_submit)
submit_button.pack()
avatar_label = tk.Label(root)
avatar_label.pack()
result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
>>>>>>> 2d1f7a9671b2aa94690632dd0d844a4e70a121b2
