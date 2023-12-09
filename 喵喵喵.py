def 喵w(喵: str) -> str:
    match 喵:
        case "喵":
            return "00"
        case "呜":
            return "01"
        case " ":
            return "10"
        case "w":
            return "11"


喵喵 = [
    "喵~",
    "w~",
    "呜~",
]

喵喵喵喵喵 = range
qwq = len
owo = chr


def 喵喵喵(喵: str):
    for 喵喵喵 in 喵喵:
        喵 = 喵.replace(喵喵喵, " ")
    喵呜 = ""
    for 呜呜 in 喵:
        喵呜 += 喵w(呜呜)
    呜喵 = ""
    for 喵喵喵喵 in 喵喵喵喵喵(0, qwq(喵呜), 16):
        呜喵 += owo(int(喵呜[喵喵喵喵 : 喵喵喵喵 + 16], 2))
    return 呜喵


if __name__ == "__main__":
    喵 = "呜w~w~ww~喵w~w呜呜wwww呜呜"
    print(喵喵喵(喵))
