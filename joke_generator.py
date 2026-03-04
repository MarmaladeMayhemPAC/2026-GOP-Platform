import requests

def get_random_joke():
    """Fetch a random joke from JokeAPI"""
    url = "https://v2.jokeapi.dev/joke/Any"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        joke_data = response.json()
        
        if joke_data['type'] == 'single':
            print(joke_data['joke'])
        else:
            print(joke_data['setup'])
            print(joke_data['delivery'])
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

if __name__ == "__main__":
    get_random_joke()