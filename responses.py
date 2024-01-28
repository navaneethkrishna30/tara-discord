from power_outage import get_power_outage


# hi = {'yo', 'hi', 'hallo', 'hey', 'wassup'}
# bye = {'bye', 'cya'}
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Enter a fucking message you moron'
    
    elif 'hello' in lowered:
        return 'wtf do you want come to the point'
    
    elif 'bye' in lowered:
        return 'fuck of nigga'
    
    elif 'power cut' in lowered:
        return get_power_outage()
    
    else:
        return 'Bitch type sth I can understand'