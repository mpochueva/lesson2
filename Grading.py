dict_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
             {'school_class': '4b', 'scores': [2, 4, 3, 5, 3]},
             {'school_class': '4c', 'scores': [3, 5, 5, 5, 3]}]

score_amount = 0
score_sum = 0
av_score_dict = {}
for i in dict_list:
    score_amount += len(i['scores'])
    score_sum2 = 0
    for j in i['scores']:
        score_sum2 +=j
        score_sum += j
    av_score_dict[i['school_class']] = round(score_sum2/len(i['scores']))


print("Средний балл по школе:", round(score_sum/score_amount))
for i in av_score_dict:
    print('Средний балл по классу', i, '-', av_score_dict[i])


