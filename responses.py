from power_outage import get_power_outage


# hi = {'yo', 'hi', 'hallo', 'hey', 'wassup'}
# bye = {'bye', 'cya'}
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Enter a message'
    
    elif 'hello' in lowered:
        return 'Hello! How can I help you today'
    
    elif 'bye' in lowered:
        return 'Bye!!!'
    
    elif 'power cut' in lowered:
        return get_power_outage()
    
    else:
        return 'Please enter a proper command'
