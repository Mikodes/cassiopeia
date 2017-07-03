import cassiopeia as cass


def print_t3_runes():
    for rune in cass.get_runes():
        if rune.tier == 3:
            print(rune.name)


if __name__ == "__main__":
    print_t3_runes()
