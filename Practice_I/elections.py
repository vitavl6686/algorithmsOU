
def find_winner(votes: list) -> str:
    candidates = dict()

    for cand in votes:
        if cand in candidates:
            candidates[cand] += 1
        else:
            candidates[cand] = 1
    
    winner = None
    max1 = 0
    max2 = 0

    for cand in candidates:
        if candidates[cand] > max1:
            max1 = candidates[cand]
            winner = cand
        else:
            if candidates[cand] > max2:
                max2 = candidates[cand]
        
    if max1 == max2:
        return "second_round"
             
    return winner

    
