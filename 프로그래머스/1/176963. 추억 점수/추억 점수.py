def solution(name, yearning, photo):
    yearning_dict = {n: y for n, y in zip(name, yearning)}
    
    result = []
    
    for pic in photo:
        total_yearning = 0
        
        for person in pic:
            if person in yearning_dict:
                total_yearning += yearning_dict[person]
        
        result.append(total_yearning)
    
    return result