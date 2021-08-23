def solution(table, languages, preference):
    answer = []
    lang2preference={l:p for l,p in zip(languages,preference)}
    
    for desc in table:
        desc=desc.split()
        job=desc[0]
        langs=desc[1:]
        score=0
        for idx,lang in enumerate(langs):
            if lang in languages:
                score+=(5-idx)*lang2preference[lang]
        answer.append([job,score])
        
    
    return sorted(answer,key=lambda x:(-x[1],x[0]))[0][0]