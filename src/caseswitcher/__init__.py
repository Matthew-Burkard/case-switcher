def to_camel(string: str) -> str:
    words = get_words(string)
    if len(words) > 0:
        return words[0].lower() + "".join(map(lambda w: w.capitalize(), words[1:]))
    return string.lower()


def to_dot(string: str) -> str:
    return ".".join(map(lambda w: w.lower(), get_words(string)))


def to_pascal(string: str) -> str:
    words = get_words(string)
    return "".join(w.capitalize() for w in words)


def to_kebab(string: str) -> str:
    return "-".join(get_words(string))


def to_snake(string: str) -> str:
    return "_".join(map(lambda w: w.lower(), get_words(string)))


def to_title(string: str) -> str:
    words = get_words(string)
    if len(words) > 0:
        return " ".join(w.capitalize() for w in words)
    return string.capitalize()


def get_words(string: str) -> list[str]:
    return []
