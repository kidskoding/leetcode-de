def flatten_dict(input_dict):
    result = {}
    
    def flatten_dict_recursive(curr, parent_key):
        for key, value in curr.items():
            updated_key = f"{parent_key}_{key}" if parent_key else key
            
            if isinstance(value, dict):
                flatten_dict_recursive(value, updated_key)
            else:
                result[updated_key] = value
                
    flatten_dict_recursive(input_dict, '')
    return result