"""Module with functions to change casing of a string."""
import re

from typing import Union

__all__ = (
    "get_words",
    "to_camel",
    "to_dot",
    "to_kebab",
    "to_pascal",
    "to_snake",
    "to_title",
    "to_upper_dot",
    "to_upper_kebab",
    "to_upper_snake",
)


def to_camel(string: str) -> str:
    """Return a version of the string in camelCase format."""
    words = get_words(string)
    first_word = ""
    if len(words) > 0:
        first_word = words[0] if words[0].isupper() else words[0].lower()
    return first_word + "".join(map(_capitalize, words[1:]))


def to_dot(string: str) -> str:
    """Return a version of the string in dot.case format."""
    return ".".join(map(lambda w: w.lower(), get_words(string)))


def to_kebab(string: str) -> str:
    """Return a version of the string in kebab-case format."""
    return "-".join(map(lambda w: w.lower(), get_words(string)))


def to_pascal(string: str) -> str:
    """Return a version of the string in PascalCase format."""
    return "".join(map(_capitalize, get_words(string)))


def to_path(string: str) -> str:
    """Return a version of the string in path/case format."""
    return "/".join(map(lambda w: w.lower(), get_words(string)))


def to_snake(string: str) -> str:
    """Return a version of the string in snake_case format."""
    return "_".join(map(lambda w: w.lower(), get_words(string)))


def to_title(string: str) -> str:
    """Return a version of the string in Title Case format."""
    return " ".join(map(_capitalize, get_words(string)))


def to_upper_dot(string: str) -> str:
    """Return a version of the string in UPPER.DOT.CASE format."""
    return ".".join(map(lambda w: w.upper(), get_words(string)))


def to_upper_kebab(string: str) -> str:
    """Return a version of the string in UPPER-KEBAB-CASE format."""
    return "-".join(map(lambda w: w.upper(), get_words(string)))


def to_upper_snake(string: str) -> str:
    """Return a version of the string in UPPER_SNAKE_CASE format."""
    return "_".join(map(lambda w: w.upper(), get_words(string)))


def get_words(string: str) -> list[str]:
    """Get a list of the words in a string in the order they appear."""
    words = [it for it in re.split(r"\b|_", string) if re.match(r"[\d\w]", it)]
    # Split on lower then upper: "oneTwo" -> ["one", "Two"]
    words = _split_words_on_regex(words, re.compile(r"(?<=[a-z])(?=[A-Z])"))
    # Split on upper then upper + lower: "JSONWord" -> ["JSON", "Word"]
    words = _split_words_on_regex(words, re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])"))
    # Split on number + letter: "TO1Cat23dog" -> ["TO1", "Cat23", "dog"]
    words = _split_words_on_regex(words, re.compile(r"(?<=\d)(?=[A-Za-z])"))
    return words


def _capitalize(word: str) -> str:
    return word if word.isupper() else word.capitalize()


def _split_words_on_regex(words: list[str], regex: Union[re.Pattern, str]) -> list[str]:
    words = words.copy()
    for i, word in enumerate(words):
        split_words = re.split(regex, word)
        if len(split_words) > 1:
            words.pop(i)
            for j, sw in enumerate(split_words):
                words.insert(i + j, sw)
    return words
