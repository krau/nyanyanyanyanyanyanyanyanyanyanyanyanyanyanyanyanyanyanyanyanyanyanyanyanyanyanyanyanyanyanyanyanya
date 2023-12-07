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
    "喵喵喵喵~",
    "喵喵喵w~",
    "喵呜喵呜~",
]


def 喵喵喵(喵: str):
    喵喵w = "".join(["{0:016b}".format(ord(c)) for c in 喵])
    喵呜呜 = ""
    for 呜呜喵 in range(0, len(喵喵w), 2):
        喵呜呜 += 喵w(喵喵w[呜呜喵 : 呜呜喵 + 2])
    喵呜呜 = 喵呜呜.replace(" ", random.choice(喵喵))
    return 喵呜呜


if __name__ == "__main__":
    喵 = "呜呜喵喵喵喵~呜呜ww呜呜喵喵喵喵~喵喵ww喵w喵喵喵喵~喵喵喵www呜呜呜喵呜喵喵喵喵~喵w呜喵喵喵喵~喵喵喵喵喵~呜w喵喵呜呜呜喵喵喵喵喵~喵w喵喵呜喵ww呜喵喵喵喵~喵喵"
    print(喵喵喵(喵))
