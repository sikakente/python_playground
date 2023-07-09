# spare
# strike

# [1, 2, 3, 4, 5, 5] = 20
# [5, 5, 4, 3, 2, 1] = 24
# 10 + 4 + 4 + 3 + 2 + 1
# [10,10, 10] = 60
# 10 + (10, 10) + 10 + (10) + 10
# [10, 5, 1, 4, 6] = 32
# 10 + (5+1) + 5 + 1 + 4 + 6
# [0, 0, 0]

def get_score(throws):
    score = 0
    reset_pair = False
    score_so_far = 0
    throws_seen = 0

    # pair nums < 10
    for idx, value in enumerate(throws):
        score_so_far += value
        throws_seen += 1
        if throws_seen == 2:
            throws_seen = 0
            # calculate bonus
            if score_so_far == 10:
                score += 10 + calculate_bonuses(idx, throws)
        elif value == 10:
            score += 10 + calculate_bonuses(idx, throws)
        else:
            score += value

    return score


def calculate_bonuses(idx, throws):
    bonus = 0
    for i in range(idx, len(throws)):
        if i < len(throws) - 1:
            if throws[i + 1] == 10:
                bonus += 10
                bonus += calculate_bonuses(idx + 1, throws)
            else:
                bonus += throws[i + 1]
                if i + 2 < len(throws):
                    bonus += throws[i + 2]

    return bonus
