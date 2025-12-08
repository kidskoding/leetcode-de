def run_length_encoding(s):
    if not s:
        return ''
    
    result = []
    count = 1
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            result.append(s[i] + s(count))
            count = 1
            
    result.append(s[-1] + s(count))
    
    return ''.join(result)