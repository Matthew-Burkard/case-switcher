import unittest

import caseswitcher as cs


class CaseSwitchTest(unittest.TestCase):
    def __init__(self, *args) -> None:
        self.camel_sample = "coffeeJSONDonut"
        self.pascal_sample = "CoffeeJSONDonut"
        self.kebab_sample = "coffee-json-donut"
        self.snake_sample = "coffee_json_donut"
        self.title_sample = "Coffee Json Donut"
        self.dot_sample = "coffee.json.donut"
        super(CaseSwitchTest, self).__init__(*args)

    # get_words Tests
    def test_get_words_from_camel(self) -> None:
        self.assertEqual(["coffee", "JSON", "Donut"], cs.get_words(self.camel_sample))

    def test_get_words_from_pascal(self) -> None:
        self.assertEqual(["Coffee", "JSON", "Donut"], cs.get_words(self.pascal_sample))

    def test_get_words_from_kebab(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.kebab_sample))

    def test_get_words_from_snake(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.snake_sample))

    def test_get_words_from_title(self) -> None:
        self.assertEqual(["Coffee", "JSON", "Donut"], cs.get_words(self.title_sample))

    def test_get_words_from_dot(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.dot_sample))

    # to_dot Tests
    def test_to_dot(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_camel(self.camel_sample))
        self.assertEqual("coffee.json.donut", cs.to_camel(self.pascal_sample))
        self.assertEqual("coffee.json.donut", cs.to_camel(self.kebab_sample))
        self.assertEqual("coffee.json.donut", cs.to_camel(self.snake_sample))
        self.assertEqual("coffee.json.donut", cs.to_camel(self.title_sample))
        self.assertEqual("coffee.json.donut", cs.to_camel(self.dot_sample))

    # to_camel Tests
    def test_to_camel(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.camel_sample))
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.pascal_sample))
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.kebab_sample))
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.snake_sample))
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.title_sample))
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.dot_sample))

    # to_pascal Tests
    def test_to_pascal(self) -> None:
        self.assertEqual("CoffeeJSONDonut", cs.to_pascal(self.camel_sample))
        self.assertEqual("CoffeeJSONDonut", cs.to_pascal(self.pascal_sample))
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.kebab_sample))
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.snake_sample))
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.title_sample))
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.dot_sample))

    # to_kebab Tests
    def test_to_kebab(self) -> None:
        self.assertEqual("Coffee-JSON-Donut", cs.to_kebab(self.camel_sample))
        self.assertEqual("Coffee-JSON-Donut", cs.to_kebab(self.pascal_sample))
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.kebab_sample))
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.snake_sample))
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.title_sample))
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.dot_sample))

    # to_snake Tests
    def test_to_snake(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.camel_sample))
        self.assertEqual("coffee_json_donut", cs.to_snake(self.pascal_sample))
        self.assertEqual("coffee_json_donut", cs.to_snake(self.kebab_sample))
        self.assertEqual("coffee_json_donut", cs.to_snake(self.snake_sample))
        self.assertEqual("coffee_json_donut", cs.to_snake(self.title_sample))
        self.assertEqual("coffee_json_donut", cs.to_snake(self.dot_sample))

    # to_title Tests
    def test_to_title(self) -> None:
        self.assertEqual("Coffee JSON Donut", cs.to_title(self.camel_sample))
        self.assertEqual("Coffee JSON Donut", cs.to_title(self.pascal_sample))
        self.assertEqual("Coffee Json Donut", cs.to_title(self.kebab_sample))
        self.assertEqual("Coffee Json Donut", cs.to_title(self.snake_sample))
        self.assertEqual("Coffee Json Donut", cs.to_title(self.title_sample))
        self.assertEqual("Coffee Json Donut", cs.to_title(self.dot_sample))
