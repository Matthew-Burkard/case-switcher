import unittest

import caseswitcher as cs


class CaseSwitchTest(unittest.TestCase):
    def __init__(self, *args) -> None:
        self.camel_sample = "coffeeJSONDonut"
        self.dot_sample = "coffee.json.donut"
        self.kebab_sample = "coffee-json-donut"
        self.pascal_sample = "CoffeeJSONDonut"
        self.snake_sample = "coffee_json_donut"
        self.title_sample = "Coffee JSON Donut"
        self.mixed_sample = "avocado bagel-coffeeDONUTEclair_food.gravy"
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

    def test_get_words_from_snake(self) -> None:
        self.assertEqual(["coffee", "json", "donut"], cs.get_words(self.snake_sample))

    def test_get_words_from_title(self) -> None:
        self.assertEqual(["Coffee", "JSON", "Donut"], cs.get_words(self.title_sample))

    def test_get_words_from_mix(self) -> None:
        self.assertEqual(
            ["avocado", "bagel", "coffee", "DONUT", "Eclair", "food", "gravy"],
            cs.get_words(self.mixed_sample),
        )

    # to_camel Tests
    def test_to_camel_from_camel(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.camel_sample))

    def test_to_camel_from_dot(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.dot_sample))

    def test_to_camel_from_kebab(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.kebab_sample))

    def test_to_camel_from_pascal(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.pascal_sample))

    def test_to_camel_from_snake(self) -> None:
        self.assertEqual("coffeeJsonDonut", cs.to_camel(self.snake_sample))

    def test_to_camel_from_title(self) -> None:
        self.assertEqual("coffeeJSONDonut", cs.to_camel(self.title_sample))

    def test_to_camel_from_mix(self) -> None:
        self.assertEqual(
            "avocadoBagelCoffeeDONUTEclairFoodGravy", cs.to_camel(self.mixed_sample)
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

    def test_to_dot_from_snake(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.snake_sample))

    def test_to_dot_from_title(self) -> None:
        self.assertEqual("coffee.json.donut", cs.to_dot(self.title_sample))

    def test_to_dot_from_mix(self) -> None:
        self.assertEqual(
            "avocado.bagel.coffee.donut.eclair.food.gravy", cs.to_dot(self.mixed_sample)
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

    def test_to_kebab_from_snake(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.snake_sample))

    def test_to_kebab_from_title(self) -> None:
        self.assertEqual("coffee-json-donut", cs.to_kebab(self.title_sample))

    def test_to_kebab_from_mix(self) -> None:
        self.assertEqual(
            "avocado-bagel-coffee-donut-eclair-food-gravy",
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

    def test_to_pascal_from_snake(self) -> None:
        self.assertEqual("CoffeeJsonDonut", cs.to_pascal(self.snake_sample))

    def test_to_pascal_from_title(self) -> None:
        self.assertEqual("CoffeeJSONDonut", cs.to_pascal(self.title_sample))

    def test_to_pascal_from_mix(self) -> None:
        self.assertEqual(
            "AvocadoBagelCoffeeDONUTEclairFoodGravy", cs.to_pascal(self.mixed_sample)
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

    def test_to_snake_from_snake(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.snake_sample))

    def test_to_snake_from_title(self) -> None:
        self.assertEqual("coffee_json_donut", cs.to_snake(self.title_sample))

    def test_to_snake_from_mix(self) -> None:
        self.assertEqual(
            "avocado_bagel_coffee_donut_eclair_food_gravy",
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

    def test_to_title_from_snake(self) -> None:
        self.assertEqual("Coffee Json Donut", cs.to_title(self.snake_sample))

    def test_to_title_from_title(self) -> None:
        self.assertEqual("Coffee JSON Donut", cs.to_title(self.title_sample))

    def test_to_title_from_mix(self) -> None:
        self.assertEqual(
            "Avocado Bagel Coffee DONUT Eclair Food Gravy",
            cs.to_title(self.mixed_sample),
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

    def test_to_upper_dot_from_snake(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.snake_sample))

    def test_to_upper_dot_from_title(self) -> None:
        self.assertEqual("COFFEE.JSON.DONUT", cs.to_upper_dot(self.title_sample))

    def test_to_upper_dot_from_mix(self) -> None:
        self.assertEqual(
            "AVOCADO.BAGEL.COFFEE.DONUT.ECLAIR.FOOD.GRAVY",
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

    def test_to_upper_kebab_from_snake(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.snake_sample))

    def test_to_upper_kebab_from_title(self) -> None:
        self.assertEqual("COFFEE-JSON-DONUT", cs.to_upper_kebab(self.title_sample))

    def test_to_upper_kebab_from_mix(self) -> None:
        self.assertEqual(
            "AVOCADO-BAGEL-COFFEE-DONUT-ECLAIR-FOOD-GRAVY",
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

    def test_to_upper_snake_from_snake(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.snake_sample))

    def test_to_upper_snake_from_title(self) -> None:
        self.assertEqual("COFFEE_JSON_DONUT", cs.to_upper_snake(self.title_sample))

    def test_to_upper_snake_from_mix(self) -> None:
        self.assertEqual(
            "AVOCADO_BAGEL_COFFEE_DONUT_ECLAIR_FOOD_GRAVY",
            cs.to_upper_snake(self.mixed_sample),
        )
