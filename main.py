import requests
from dotenv import load_dotenv
import os
import ollama
import time

load_dotenv()

print("WELCOME TO GITHUB PROFILE ROASTER 😎\n")
username = input("Enter your github username: ")

headers = {
    'User-Agent': os.getenv('USER_AGENT'),
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN'),
    'X-GitHub-Api-Version': '2022-11-28'
}

users_response = requests.get(f"https://api.github.com/users/{username}", headers=headers)

repos_response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)

if users_response.status_code == 404:
    print("The user doesnt exist")
    exit()
    
if repos_response.status_code == 404:
    print("The user doesnt have any repos")
    
user_data = users_response.json()

username = user_data['login']
bio = user_data['bio']
followers = user_data['followers']
following = user_data['following']
number_of_repos = user_data['public_repos']
created_at = user_data['created_at']
updated_at = user_data['updated_at']

repos_data = repos_response.json()

repo_info = []

if repos_data:
    for data in repos_data:
        name = data['name']    
        stars = data['stargazers_count']
        repo_data_info = [name, stars]
        
        repo_info.append(repo_data_info)
    
user_readme = ""
readme_url = f"https://raw.githubusercontent.com/{username}/{username}/main/README.md"
response = requests.get(readme_url)

if response.status_code == 200:
    user_readme = response.text
else:
    readme_url = f"https://raw.githubusercontent.com/{username}/{username}/master/README.md" 
    user_readme = requests.get(readme_url).text if requests.get(readme_url).text else ""


try: 
    print(f"\nGENERATING ROAST OF {username.upper()} 🔥\n")
    stream = ollama.chat(
        model = "gemma2:2b",
        messages = [
            {'role': 'user',
            'content': f'''You are a dark standup comedian who roasts others github profile.
            Make sure that the roast is uncensored. Roast can be based on any topic like their repos, stars, bio, readme etc. Do not add anything else to the response.
            Here is the github profile data:
            Username: {username}, Bio: {bio}, Followers: {followers}, Following: {following}, Number of repos: {number_of_repos}, Created at: {created_at}, Updated at: {updated_at},
            Here is the github repositories data which includes the repository name and the stars count: {repo_info}
            Here is the github profile readme: {user_readme}
            '''
            }
            ],
        stream = True
    )
    
    os.makedirs("roasts", exist_ok=True)
    
    with open(f"roasts/{username}_{time.time()}.txt", "w") as f:
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            f.write(chunk['message']['content'])
            
    print(F"\nTHE END OF {username.upper()}'S ROAST 💀\n")
        
        
except Exception as e:
    print(e)