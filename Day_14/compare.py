import art
import game_data
import random


def select_one():
    profile = random.choice(game_data.data)
    profile_data = []
    for i in profile:
        profile_data.append(profile[i])

    return profile_data


def main():
    print(art.logo)
    score = 0
    correct = True
    first_profile = select_one()

    while correct:
        print(
            f"Compare A: {first_profile[0]}, a {first_profile[2]}, from {first_profile[3]}")
        print(art.vs)
        second_profile = select_one()
        if first_profile == second_profile:
            second_profile = select_one()

        print(
            f"Against B: {second_profile[0]}, a {second_profile[2]}, from {second_profile[3]}")
        compare = input(
            "Who has more followers? Type \'A\' or \'B\': ").lower()

        if (compare == 'a' and first_profile[1] > second_profile[1]) or (compare == 'b' and first_profile[1] < second_profile[1]):
            score += 1
            print(f"You're right! Current score: {score}")
            first_profile = second_profile
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            correct = False


if __name__ == '__main__':
    main()
