def solution(genres, plays):
    genre_dict = {}
    top_genres = {}
    
    for idx in range(len(genres)):
        crt_g = genres[idx]
        crt_p = plays[idx]
        
        if crt_g not in genre_dict:
            genre_dict[crt_g] = crt_p
        else:
            genre_dict[crt_g] += crt_p
            
        if crt_g not in top_genres:
            top_genres[crt_g] = [(idx, crt_p)]
        else:
            top_genres[crt_g].append((idx, crt_p))
            top_genres[crt_g].sort(key = lambda x: -x[1])
            if len(top_genres[crt_g]) >= 3:
                top_genres[crt_g].pop(2)
        
        print(genre_dict)
        print(top_genres)
    
    answer = []
    for key, val in sorted(genre_dict.items(), key=lambda x: -x[1]):
        answer.extend([idx for idx, _ in top_genres[key]])
        print(answer)
    return answer