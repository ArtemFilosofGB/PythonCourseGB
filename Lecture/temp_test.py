def reducer(score_data1, score_data2):
    if score_data1 is None and score_data2 is None:
        return None
    elif score_data1 is None:
        return score_data2
    elif score_data2 is None:
        return score_data1
    else:
        score=[]
        if len(score_data1)==1:
            n, mean, M2 = 0, 0.0, 0
            score.append(score_data1[0])
        else:
            n, mean, M2 = score_data1
            score.append(score_data2[0])
    for sc in score:
        n += 1
        delta = score - mean
        mean += delta / n
        M2 += delta * (score - mean)
    return n, mean, M2