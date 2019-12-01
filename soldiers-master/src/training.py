from typing import List, Union

STATE = List[List[str]]
arrows = ["↑", "↓", "→", "←"]


def init() -> STATE:
    return [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "↓", "↓", "↓", " ", " "],
        [" ", " ", "↓", "↓", "↓", " ", " "],
        [" ", " ", "↓", "↓", "↓", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]


def train(command: str, soldiers: STATE) -> STATE:
    commands = {"Turn on me!": turn_on_me,
                "Turn West!": turn_west,
                "Turn East!": turn_east,
                "Turn South!": turn_south,
                "Go Forward!": go_forward}
    return commands[command](soldiers)


def turn_west(soldiers):

    for i, row in enumerate(soldiers):
        for j, position in enumerate(row):
            if position in arrows:
                soldiers[i][j] = "←"
    return soldiers


def turn_east(soldiers):

    for i, row in enumerate(soldiers):
        for j, position in enumerate(row):
            if position in arrows:
                soldiers[i][j] = "→"
    return soldiers


def turn_south(soldiers):
    for i, row in enumerate(soldiers):
        for j, position in enumerate(row):
            if position in arrows:
                soldiers[i][j] = "↓"
    return soldiers


def turn_on_me(soldiers):4
    for i, row in enumerate(soldiers):
        for j, position in enumerate(row):
            if position in arrows:
                soldiers[i][j] = "↑"
    return soldiers


def go_forward(soldiers):
    for row_id, row in enumerate(soldiers):
        for pos_id, position in enumerate(row):
            if position == "←":
                soldiers[row_id ][pos_id - 1] = position
                soldiers[row_id][pos_id] = " "
            if position == "↑":
                soldiers[row_id - 1][pos_id ] = position
                soldiers[row_id][pos_id] = " "
            if position == "↓":
                #Żołnierze sie kopiuja w niesk, zauważone brak czasu ale są pomysły.
                soldiers[row_id + 1][pos_id] = position
                soldiers[row_id][pos_id] = " "
            if position == "→":
                soldiers[row_id][pos_id + 1] = position
                soldiers[row_id][pos_id] = " "
    return soldiers


def transform_to_str(soldiers: STATE) -> str:
    return "\n".join(str(row) for row in soldiers)



