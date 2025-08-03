# We need the 'requests' library to make HTTP requests
import requests
# We use the 'json' library to pretty-print the result
import json

def get_single_todo():
    """
    Makes a single API call to fetch one 'To-Do' item.
    """
    # 1. Define the URL of the API endpoint we want to call
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    
    print(f"Making a request to: {api_url}")

    try:
        # 2. Send an HTTP GET request to the URL
        response = requests.get(api_url)
        
        # 3. Check if the request was successful (e.g., status code 200 OK)
        # This will raise an error for bad responses (like 404 Not Found or 500 Server Error)
        response.raise_for_status()
        
        # 4. Parse the JSON response text into a Python dictionary
        data = response.json()
        
        # 5. Display the fetched data in a readable format
        print("\n--- Success! Data received: ---")
        print(json.dumps(data, indent=2))

    except requests.exceptions.RequestException as e:
        # This block will run if there's a network error or a bad status code
        print(f"\n--- An error occurred: {e} ---")


# Run the function when the script is executed
if __name__ == "__main__":
    get_single_todo()