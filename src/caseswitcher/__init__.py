import re


def to_camel(string: str) -> str:
    words = get_words(string)
    if len(words) > 0:
        return words[0].lower() + "".join(map(_capitalize, words[1:]))
    return string.lower()


def to_dot(string: str) -> str:
    return ".".join(map(lambda w: w.lower(), get_words(string)))


def to_pascal(string: str) -> str:
    words = get_words(string)
    return "".join(map(_capitalize, words))


def to_kebab(string: str) -> str:
    return "-".join(map(lambda w: w.lower(), get_words(string)))


def to_snake(string: str) -> str:
    return "_".join(map(lambda w: w.lower(), get_words(string)))


def to_title(string: str) -> str:
    words = get_words(string)
    if len(words) > 0:
        return " ".join(map(_capitalize, words))
    return string.capitalize()


def get_words(string: str) -> list[str]:
    words = [it for it in re.split(r"\b|_", string) if it and it not in ". -_"]
    # Split on upper then lower: "oneTwo" -> ["one", "Two"]
    for word in words:
        camel_words = re.split(r"(?<=[a-z])(?=[A-Z])", word)
        if len(camel_words) > 1:
            words.remove(word)
            words.extend(camel_words)
    # Split on upper then upper + lower: "JSONWord" -> ["JSON", "Word"]
    for word in words:
        camel_words = re.split(r"(?<=[A-Z])(?=[A-Z][a-z])", word)
        if len(camel_words) > 1:
            words.remove(word)
            words.extend(camel_words)
    return words


def _capitalize(word: str) -> str:
    return word if word.isupper() else word.capitalize()
