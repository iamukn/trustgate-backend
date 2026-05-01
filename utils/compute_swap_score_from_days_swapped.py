def compute_new_swap_score_based_on_days(days: float):

    score = 0

    days = int(days)
    
    if days == 0:
        score = 60

    elif days == 1:
        score = 58

    elif days >= 2 and days <= 5:
        score = 50

    elif days >= 6 and days <= 10:
        score = 40

    elif days >= 11 and days <= 20:
        score = 20

    else:
        score = 0

    return score
