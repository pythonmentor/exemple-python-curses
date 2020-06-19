import curses


def center(screen, lines):
    """Generator centering the lines at the center of the screen."""
    height, width = screen.getmaxyx()
    y = (height - len(lines)) // 2
    for i, line in enumerate(lines):
        x = (width - len(line)) // 2
        yield y + i, x, line


def clear(screen):
    """clear the screen with the chosen default background color."""
    screen.clear()
    height, width = screen.getmaxyx()
    text = "\n".join(" " * (width - 1) for _ in range(height - 1))
    screen.addstr(0, 0, text, curses.color_pair(1))


def main(screen):
    """Main entry point of the example."""
    # setting cursor visibility
    curses.curs_set(False)

    # setting color pairs and clearing the screen with the choosen colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    clear(screen)

    lines = [
        "Petit exemple de code avec curses",
        "---------------------------------",
        "",
        "Appuyez sur n'importe quelle touche pour quitter...",
    ]

    for y, x, line in center(screen, lines):
        screen.addstr(y, x, line, curses.color_pair(1))

    screen.refresh()
    # waiting the user press a key to quit the example
    key = screen.getch()


if __name__ == "__main__":
    curses.wrapper(main)
