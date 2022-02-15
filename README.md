<div align=center>
<!-- Title: -->
  <h1>Case Switcher</h1>
<!-- Labels: -->
  <!-- First row: -->
  <img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg"
   height="20"
   alt="License: AGPL v3">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg"
   height="20"
   alt="Code style: black">
  <img src="https://img.shields.io/pypi/v/case-switcher.svg"
   height="20"
   alt="PyPI version">
  <img src="https://img.shields.io/badge/coverage-100%25-success"
   height="20"
   alt="Code Coverage">
  <h3>Change casing of a string.</h3>
</div>

This library provides functions to change the casing convention of a
string.

Supported cases:
- camelCase
- dot.case
- kebab-case
- PascalCase
- snake_case
- Title Case
- UPPER.DOT.CASE
- UPPER-KEBAB-CASE
- UPPER_SNAKE_CASE

### Install

```shell
poetry add case-switcher
```

```shell
pip install case-switcher
```

### Demo

```python
import caseswitcher

sample = "avocado bagel-coffeeDONUTEclair_food.gravy"

caseswitcher.to_camel(sample)  # -> "avocadoBagelCoffeeDONUTEclairFoodGravy"
caseswitcher.to_dot(sample)  # -> "avocado.bagel.coffee.donut.eclair.food.gravy"
caseswitcher.to_kebab(sample)  # -> "avocado-bagel-coffee-donut-eclair-food-gravy"
caseswitcher.to_pascal(sample)  # -> "AvocadoBagelCoffeeDONUTEclairFoodGravy"
caseswitcher.to_snake(sample)  # -> "avocado_bagel_coffee_donut_eclair_food_gravy"
caseswitcher.to_title(sample)  # -> "Avocado Bagel Coffee DONUT Eclair Food Gravy"
caseswitcher.to_upper_dot(sample)  # -> "AVOCADO.BAGEL.COFFEE.DONUT.ECLAIR.FOOD.GRAVY"
caseswitcher.to_upper_kebab(sample)  # -> "AVOCADO-BAGEL-COFFEE-DONUT-ECLAIR-FOOD-GRAVY"
caseswitcher.to_upper_snake(sample)  # -> "AVOCADO_BAGEL_COFFEE_DONUT_ECLAIR_FOOD_GRAVY"
```
