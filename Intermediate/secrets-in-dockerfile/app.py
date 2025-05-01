import os

def main():
    api_key = os.getenv("API_KEY")
    # Just print it so we can see it in the running container logs
    print(f"[app.py] Loaded API_KEY: {api_key}")

if __name__ == "__main__":
    main()
