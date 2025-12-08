def parse_log(log_str):
    if not log_str:
        return {}
    
    log_as_map = {}
    log_components = log_str.split(';')
    
    for x in log_components:
        key, value = x.split('=', 1)
        
        key = key.strip()
        value = value.strip()
        
        if value == 'NULL':
            log_as_map[key] = None
        else:
            log_as_map[key] = value
        
    return log_as_map