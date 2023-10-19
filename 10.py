def filter_account(dictionary: dict, min_followers, max_followers):
    res = []
    for key, value in dictionary.items():
        print(key, value)
        if min_followers <= value <= max_followers:
            res.append(key)
    return sorted(res)


# Здесь вводить в задание надо только функции

print(
    filter_account({'@blogger13999': 2308,
                    '@dragondragon': 1473,
                    '@account': 1400,
                    '@flowers': 1250,
                    '@banana': 1500},
                   1400, 1500))
