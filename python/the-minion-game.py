def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    score = {"stuart": 0, "kevin": 0}
    for idx, letter in enumerate(string):
        if letter in vowels:
            score["kevin"] += len(string) - idx
        else:
            score["stuart"] += len(string) - idx
    if score["stuart"] == score["kevin"]:
        print("Draw")
        return
    max_key = max(score, key=score.get)
    print(max_key.capitalize(), score[max_key])


if __name__ == '__main__':
    s = input()
    minion_game(s)
