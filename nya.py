def 喵呜(喵w: str) -> str:
    a = {"喵": "m", "呜": "e", "~": "o", "w": "w"}
    meow = ""
    qwq = 喵w[0]
    呜呜 = 1

    for w in 喵w[1:]:
        if w == qwq:
            呜呜 += 1
        else:
            meow += a[qwq] + str(呜呜) if 呜呜 > 1 else a[qwq]
            qwq = w
            呜呜 = 1

    meow += a[qwq] + str(呜呜) if 呜呜 > 1 else a[qwq]

    return meow


def 喵(喵w: str):
    print(喵w)
    喵w = 喵呜(喵w)
    print(喵w)


if __name__ == "__main__":
    喵w = "呜ww~呜呜呜w呜呜喵ww呜w~喵喵呜呜呜w喵w~w~喵呜呜喵www~呜w~呜喵ww~喵喵喵喵呜喵ww~喵w~w~w~呜喵ww~喵呜呜w~呜w呜呜呜喵w喵w~喵www喵呜w呜呜www~呜呜w呜w~喵呜喵喵w~呜呜呜wwww~w~w"
    喵(喵w)
