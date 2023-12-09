def 喵喵(喵w):
    a = {"m": "喵", "e": "呜", "o": "~", "w": "w"}
    呜呜 = ""
    爱 = 0

    while 爱 < len(喵w):
        喵呜 = 喵w[爱]
        爱 += 1

        nya = ""
        while 爱 < len(喵w) and 喵w[爱].isdigit():
            nya += 喵w[爱]
            爱 += 1

        qwq = int(nya) if nya else 1
        呜呜 += a[喵呜] * qwq

    return 呜呜


def 喵(喵w: str):
    print(喵w)
    喵w = 喵喵(喵w)
    print(喵w)


if __name__ == "__main__":
    喵w = "ew2oe3we2mw2ewom2e3wmwowome2mw3oewoemw2om4emw2omwowowoemw2ome2woewe3mwmwomw3mewe2w3oe2wewomem2woe3w4owow"
    喵(喵w)
