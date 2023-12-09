import random


def 喵w(喵: str) -> str:
    match 喵:
        case "00":
            return "喵"
        case "01":
            return "呜"
        case "10":
            return " "
        case "11":
            return "w"


喵喵 = [
    "喵~",
    "w~",
    "呜~",
]


def 喵喵喵(喵: str):
    喵喵w = "".join(["{0:016b}".format(ord(meow)) for meow in 喵])
    喵呜呜 = ""
    for 呜呜喵 in range(0, len(喵喵w), 2):
        喵呜呜 += 喵w(喵喵w[呜呜喵 : 呜呜喵 + 2])
    喵呜呜 = 喵呜呜.replace(" ", random.choice(喵喵))
    return 喵呜呜


if __name__ == "__main__":
    喵 = "呜喵~喵喵~喵呜喵呜呜呜w喵喵喵呜喵~呜w呜呜喵喵~喵~喵呜喵ww呜呜喵~呜呜w呜呜喵呜ww呜喵~喵喵ww喵w呜呜wwww呜呜呜呜呜喵喵~喵w喵呜w喵~呜呜呜w呜呜喵~喵呜喵www呜喵ww呜喵~喵喵"
    print(喵喵喵(喵))
