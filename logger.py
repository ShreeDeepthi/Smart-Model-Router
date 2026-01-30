import datetime

def log_request(prompt, difficulty):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | {difficulty} | {prompt}\n")
