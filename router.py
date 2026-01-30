def call_simple_model(prompt):
    return f"[SIMPLE MODEL] Processed: {prompt}"

def call_medium_model(prompt):
    return f"[MEDIUM MODEL] Processed: {prompt}"

def call_hard_model(prompt):
    return f"[HARD MODEL] Processed: {prompt}"

def route_prompt(prompt, difficulty):
    if difficulty == "simple":
        return call_simple_model(prompt)
    elif difficulty == "medium":
        return call_medium_model(prompt)
    else:
        return call_hard_model(prompt)
