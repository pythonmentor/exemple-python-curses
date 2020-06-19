import curses


def center(screen, lines):
    height, width = screen.getmaxyx()
    y = (height - len(lines)) // 2

    for i, line in enumerate(lines):
        x = (width - len(line)) // 2
        yield y + i, x, line


def main(screen):
    screen.clear()
    curses.curs_set(False)

    lines = [
        "Petit exemple de code avec curses",
        "---------------------------------",
        "",
        "Appuyez sur n'importe quelle touche pour quitter...",
    ]

    for y, x, line in center(screen, lines):
        screen.addstr(y, x, line)

    key = screen.getch()


if __name__ == "__main__":
    curses.wrapper(main)
