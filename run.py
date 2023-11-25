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

def fetch_avatar(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        image = Image.open(requests.get(url, stream=True).raw)
        image.thumbnail((100, 100))  
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error fetching avatar: {e}")
        return None

def on_submit():
    username = user_name_entry.get()
    user_data = get_osu_user_stats(username)

    if isinstance(user_data, dict):
        stats = f"Username: {user_data['username']}\nRank: {user_data['pp_rank']}\nPerformance Points: {user_data['pp_raw']}"
        avatar_url = f"https://a.ppy.sh/{user_data['user_id']}"
        avatar_image = fetch_avatar(avatar_url)
        if avatar_image:
            avatar_label.config(image=avatar_image)
            avatar_label.image = avatar_image  
    else:
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
