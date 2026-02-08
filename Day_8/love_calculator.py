def calculate_love_score(first_name, second_name):
    FIRST_WORD = 'TRUE'
    SECOND_WORD = 'LOVE'
    combined_name = first_name + second_name

    true_counter = 0
    love_counter = 0

    for i in FIRST_WORD.lower():
        for j in combined_name.lower():
            if i == j:
                true_counter += 1

    for i in SECOND_WORD.lower():
        for j in combined_name.lower():
            if i == j:
                love_counter += 1

    print((true_counter*10) + love_counter)


calculate_love_score("Angela Yu", "Jack Bauer")
