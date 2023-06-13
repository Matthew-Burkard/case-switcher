"""Unit tests of each case, to each case, round-robin style."""
import unittest

import caseswitcher as cs


class CaseSwitchTest(unittest.TestCase):
    def __init__(self, *args) -> None:
        self.camel_sample = "coffeeJSONDonut"
        self.dot_sample = "coffee.json.donut"
        self.kebab_sample = "coffee-json-donut"
        self.pascal_sample = "CoffeeJSONDonut"
        self.path_sample = "coffee/json/donut"
        self.snake_sample = "coffee_json_donut"
        self.title_sample = "Coffee JSON Donut"
        self.mixed_sample = "avocado bagel-coffeeDONUTEclair_food.gravy/honey"
        self.lone_word_sample = "Honey"
        self.lone_upper_word_sample = "ICING"
        self.numbers = "JSON1Jelly23kebab"
        self.upper_snake = "AVOCADO_BAGEL_COFFEE_DONUT_ECLAIR_FOOD_GRAVY_HONEY"
        super(CaseSwitchTest, self).__init__(*args)

    # get_words Tests
    def test_get_words_from_camel(self) -> None:
        self.assertEqual(["coffee", "JSON", "Donut"], cs.get_words(self.camel_sample))

    def test_get_words_from_dot(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.dot_sample))

    def test_get_words_from_kebab(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.kebab_sample))

    def test_get_words_from_pascal(self) -> None:
        self.assertEqual(["Coffee", "JSON", "Donut"], cs.get_words(self.pascal_sample))

    def test_get_words_from_path(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.path_sample))

    def test_get_words_from_snake(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.snake_sample))

    def test_get_words_from_title(self) -> None:
        self.assertEqual(["Coffee", "JSON", "Donut"], cs.get_words(self.title_sample))

    def test_get_words_from_lone_word(self) -> None:
        self.assertEqual([self.lone_word_sample], cs.get_words(self.lone_word_sample))

    def test_get_words_from_lone_upper_word(self) -> None:
        self.assertEqual(
            [self.lone_upper_word_sample], cs.get_words(self.lone_upper_word_sample)
        )

    def test_get_words_from_nothing(self) -> None:
        self.assertEqual([], cs.get_words(""))

    def test_get_words_from_mix(self) -> None:
        self.assertEqual(
            ["avocado", "bagel", "coffee", "DONUT", "Eclair", "food", "gravy", "honey"],
            cs.get_words(self.mixed_sample),
        )

    def test_get_words_with_numbers(self) -> None:
        self.assertEqual(["JSON1", "Jelly23", "kebab"], cs.get_words(self.numbers))

    # to_camel Tests
    def test_to_camel_from_camel(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.camel_sample))

    def test_to_camel_from_dot(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.dot_sample))

    def test_to_camel_from_kebab(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.kebab_sample))

    def test_to_camel_from_pascal(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.pascal_sample))

    def test_to_camel_from_path(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.path_sample))

    def test_to_camel_from_snake(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.snake_sample))

    def test_to_camel_from_title(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.title_sample))

    def test_to_camel_from_lone_word(self) -> None:
        self.assertEqual("honey", cs.to_camel(self.lone_word_sample))

    def test_to_camel_from_lone_upper_word(self) -> None:
        self.assertEqual("icing", cs.to_camel(self.lone_upper_word_sample))

    def test_to_camel_from_nothing(self) -> None:
        self.assertEqual("", cs.to_camel(""))

    def test_to_camel_from_mix(self) -> None:
        self.assertEqual(
            "avocadoBagelCoffeeDONUTEclairFoodGravyHoney",
            cs.to_camel(self.mixed_sample),
        )

    def test_to_camel_from_all_upper(self) -> None:
        self.assertEqual(
            "avocadoBagelCoffeeDonutEclairFoodGravyHoney",
            cs.to_camel(self.upper_snake),
        )

    # to_dot Tests
    def test_to_dot_from_camel(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.camel_sample))

    def test_to_dot_from_dot(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.dot_sample))

    def test_to_dot_from_kebab(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.kebab_sample))

    def test_to_dot_from_pascal(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.pascal_sample))

    def test_to_dot_from_path(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.path_sample))

    def test_to_dot_from_snake(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.snake_sample))

    def test_to_dot_from_title(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.title_sample))

    def test_to_dot_from_lone_word(self) -> None:
        self.assertEqual("honey", cs.to_dot(self.lone_word_sample))

    def test_to_dot_from_lone_upper_word(self) -> None:
        self.assertEqual("icing", cs.to_dot(self.lone_upper_word_sample))

    def test_to_dot_from_nothing(self) -> None:
        self.assertEqual("", cs.to_dot(""))

    def test_to_dot_from_mix(self) -> None:
        self.assertEqual(
            "avocado.bagel.coffee.donut.eclair.food.gravy.honey",
            cs.to_dot(self.mixed_sample),
        )

    # to_kebab Tests
    def test_to_kebab_from_camel(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.camel_sample))

    def test_to_kebab_from_dot(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.dot_sample))

    def test_to_kebab_from_kebab(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.kebab_sample))

    def test_to_kebab_from_pascal(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.pascal_sample))

    def test_to_kebab_from_path(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.path_sample))

    def test_to_kebab_from_snake(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.snake_sample))

    def test_to_kebab_from_title(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.title_sample))

    def test_to_kebab_from_lone_word(self) -> None:
        self.assertEqual("honey", cs.to_kebab(self.lone_word_sample))

    def test_to_kebab_from_lone_upper_word(self) -> None:
        self.assertEqual("icing", cs.to_kebab(self.lone_upper_word_sample))

    def test_to_kebab_from_nothing(self) -> None:
        self.assertEqual("", cs.to_kebab(""))

    def test_to_kebab_from_mix(self) -> None:
        self.assertEqual(
            "avocado-bagel-coffee-donut-eclair-food-gravy-honey",
            cs.to_kebab(self.mixed_sample),
        )

    # to_pascal Tests
    def test_to_pascal_from_camel(self) -> None:
        self.assertEqual("CoffeeJSONDonut", cs.to_pascal(self.camel_sample))

    def test_to_pascal_from_dot(self) -> None:
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.dot_sample))

    def test_to_pascal_from_kebab(self) -> None:
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.kebab_sample))

    def test_to_pascal_from_pascal(self) -> None:
        self.assertEqual("CoffeeJSONDonut", cs.to_pascal(self.pascal_sample))

    def test_to_pascal_from_path(self) -> None:
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.path_sample))

    def test_to_pascal_from_snake(self) -> None:
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.snake_sample))

    def test_to_pascal_from_title(self) -> None:
        self.assertEqual("CoffeeJSONDonut", cs.to_pascal(self.title_sample))

    def test_to_pascal_from_lone_word(self) -> None:
        self.assertEqual(self.lone_word_sample, cs.to_pascal(self.lone_word_sample))

    def test_to_pascal_from_lone_upper_word(self) -> None:
        self.assertEqual("Icing", cs.to_pascal(self.lone_upper_word_sample))

    def test_to_pascal_from_nothing(self) -> None:
        self.assertEqual("", cs.to_pascal(""))

    def test_to_pascal_from_mix(self) -> None:
        self.assertEqual(
            "AvocadoBagelCoffeeDONUTEclairFoodGravyHoney",
            cs.to_pascal(self.mixed_sample),
        )

    def test_to_pascal_from_all_upper(self) -> None:
        self.assertEqual(
            "AvocadoBagelCoffeeDonutEclairFoodGravyHoney",
            cs.to_pascal(self.upper_snake),
        )

    # to_path Tests
    def test_to_path_from_camel(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.camel_sample))

    def test_to_path_from_dot(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.dot_sample))

    def test_to_path_from_kebab(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.kebab_sample))

    def test_to_path_from_pascal(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.pascal_sample))

    def test_to_path_from_path(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.path_sample))

    def test_to_path_from_snake(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.snake_sample))

    def test_to_path_from_title(self) -> None:
        self.assertEqual("coffee/json/donut", cs.to_path(self.title_sample))

    def test_to_path_from_lone_word(self) -> None:
        self.assertEqual(
            self.lone_word_sample.lower(), cs.to_path(self.lone_word_sample)
        )

    def test_to_path_from_lone_upper_word(self) -> None:
        self.assertEqual(
            self.lone_upper_word_sample.lower(), cs.to_path(self.lone_upper_word_sample)
        )

    def test_to_path_from_nothing(self) -> None:
        self.assertEqual("", cs.to_path(""))

    def test_to_path_from_mix(self) -> None:
        self.assertEqual(
            "avocado/bagel/coffee/donut/eclair/food/gravy/honey",
            cs.to_path(self.mixed_sample),
        )

    # to_snake Tests
    def test_to_snake_from_camel(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.camel_sample))

    def test_to_snake_from_dot(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.dot_sample))

    def test_to_snake_from_kebab(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.kebab_sample))

    def test_to_snake_from_pascal(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.pascal_sample))

    def test_to_snake_from_path(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.path_sample))

    def test_to_snake_from_snake(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.snake_sample))

    def test_to_snake_from_title(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.title_sample))

    def test_to_snake_from_lone_word(self) -> None:
        self.assertEqual("honey", cs.to_snake(self.lone_word_sample))

    def test_to_snake_from_lone_upper_word(self) -> None:
        self.assertEqual("icing", cs.to_snake(self.lone_upper_word_sample))

    def test_to_snake_from_nothing(self) -> None:
        self.assertEqual("", cs.to_snake(""))

    def test_to_snake_from_mix(self) -> None:
        self.assertEqual(
            "avocado_bagel_coffee_donut_eclair_food_gravy_honey",
            cs.to_snake(self.mixed_sample),
        )

    # to_title Tests
    def test_to_title_from_camel(self) -> None:
        self.assertEqual("Coffee JSON Donut", cs.to_title(self.camel_sample))

    def test_to_title_from_dot(self) -> None:
        self.assertEqual("Coffee Json Donut", cs.to_title(self.dot_sample))

    def test_to_title_from_kebab(self) -> None:
        self.assertEqual("Coffee Json Donut", cs.to_title(self.kebab_sample))

    def test_to_title_from_pascal(self) -> None:
        self.assertEqual("Coffee JSON Donut", cs.to_title(self.pascal_sample))

    def test_to_title_from_path(self) -> None:
        self.assertEqual("Coffee Json Donut", cs.to_title(self.path_sample))

    def test_to_title_from_snake(self) -> None:
        self.assertEqual("Coffee Json Donut", cs.to_title(self.snake_sample))

    def test_to_title_from_title(self) -> None:
        self.assertEqual("Coffee JSON Donut", cs.to_title(self.title_sample))

    def test_to_title_from_lone_word(self) -> None:
        self.assertEqual(self.lone_word_sample, cs.to_title(self.lone_word_sample))

    def test_to_title_from_lone_upper_word(self) -> None:
        self.assertEqual("Icing", cs.to_title(self.lone_upper_word_sample))

    def test_to_title_from_nothing(self) -> None:
        self.assertEqual("", cs.to_title(""))

    def test_to_title_from_mix(self) -> None:
        self.assertEqual(
            "Avocado Bagel Coffee DONUT Eclair Food Gravy Honey",
            cs.to_title(self.mixed_sample),
        )

    def test_to_title_from_all_upper(self) -> None:
        self.assertEqual(
            "Avocado Bagel Coffee Donut Eclair Food Gravy Honey",
            cs.to_title(self.upper_snake),
        )

    # to_upper_dot Tests
    def test_to_upper_dot_from_camel(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.camel_sample))

    def test_to_upper_dot_from_dot(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.dot_sample))

    def test_to_upper_dot_from_kebab(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.kebab_sample))

    def test_to_upper_dot_from_pascal(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.pascal_sample))

    def test_to_upper_dot_from_path(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.path_sample))

    def test_to_upper_dot_from_snake(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.snake_sample))

    def test_to_upper_dot_from_title(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.title_sample))

    def test_to_upper_dot_from_lone_word(self) -> None:
        self.assertEqual("HONEY", cs.to_upper_dot(self.lone_word_sample))

    def test_to_upper_dot_from_lone_upper_word(self) -> None:
        self.assertEqual(
            self.lone_upper_word_sample, cs.to_upper_dot(self.lone_upper_word_sample)
        )

    def test_to_upper_dot_from_nothing(self) -> None:
        self.assertEqual("", cs.to_upper_dot(""))

    def test_to_upper_dot_from_mix(self) -> None:
        self.assertEqual(
            "AVOCADO.BAGEL.COFFEE.DONUT.ECLAIR.FOOD.GRAVY.HONEY",
            cs.to_upper_dot(self.mixed_sample),
        )

    # to_upper_kebab Tests
    def test_to_upper_kebab_from_camel(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.camel_sample))

    def test_to_upper_kebab_from_dot(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.dot_sample))

    def test_to_upper_kebab_from_kebab(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.kebab_sample))

    def test_to_upper_kebab_from_pascal(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.pascal_sample))

    def test_to_upper_kebab_from_path(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.path_sample))

    def test_to_upper_kebab_from_snake(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.snake_sample))

    def test_to_upper_kebab_from_title(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.title_sample))

    def test_to_upper_kebab_from_lone_word(self) -> None:
        self.assertEqual("HONEY", cs.to_upper_kebab(self.lone_word_sample))

    def test_to_upper_kebab_from_lone_upper_word(self) -> None:
        self.assertEqual(
            self.lone_upper_word_sample, cs.to_upper_kebab(self.lone_upper_word_sample)
        )

    def test_to_upper_kebab_from_nothing(self) -> None:
        self.assertEqual("", cs.to_upper_kebab(""))

    def test_to_upper_kebab_from_mix(self) -> None:
        self.assertEqual(
            "AVOCADO-BAGEL-COFFEE-DONUT-ECLAIR-FOOD-GRAVY-HONEY",
            cs.to_upper_kebab(self.mixed_sample),
        )

    # to_upper_snake Tests
    def test_to_upper_snake_from_camel(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.camel_sample))

    def test_to_upper_snake_from_dot(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.dot_sample))

    def test_to_upper_snake_from_kebab(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.kebab_sample))

    def test_to_upper_snake_from_pascal(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.pascal_sample))

    def test_to_upper_snake_from_path(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.path_sample))

    def test_to_upper_snake_from_snake(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.snake_sample))

    def test_to_upper_snake_from_title(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.title_sample))

    def test_to_upper_snake_from_lone_word(self) -> None:
        self.assertEqual("HONEY", cs.to_upper_snake(self.lone_word_sample))

    def test_to_upper_snake_from_lone_upper_word(self) -> None:
        self.assertEqual(
            self.lone_upper_word_sample, cs.to_upper_snake(self.lone_upper_word_sample)
        )

    def test_to_upper_snake_from_nothing(self) -> None:
        self.assertEqual("", cs.to_upper_snake(""))

    def test_to_upper_snake_from_mix(self) -> None:
        self.assertEqual(
            "AVOCADO_BAGEL_COFFEE_DONUT_ECLAIR_FOOD_GRAVY_HONEY",
            cs.to_upper_snake(self.mixed_sample),
        )
