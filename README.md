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
  <?xml version="1.0" encoding="UTF-8"?>
  <svg xmlns="http://www.w3.org/2000/svg" width="99" height="20">
    <linearGradient id="b" x2="0" y2="100%">
      <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
      <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <mask id="a">
      <rect width="99" height="20" rx="3" fill="#fff"/>
    </mask>
    <g mask="url(#a)">
      <path fill="#555" d="M0 0h63v20H0z"/>
      <path fill="#4c1" d="M63 0h36v20H63z"/>
      <path fill="url(#b)" d="M0 0h99v20H0z"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
      <text x="31.5" y="15" fill="#010101" fill-opacity=".3">coverage</text>
      <text x="31.5" y="14">coverage</text>
      <text x="80" y="15" fill="#010101" fill-opacity=".3">100%</text>
      <text x="80" y="14">100%</text>
    </g>
  </svg>
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
pip install case-switcher
```

### Demo

```pycon
>>> import caseswitcher
>>>
>>> sample = "avocado bagel-coffeeDONUTEclair_food.gravy"
>>>
>>> caseswitcher.to_camel(sample)
'avocadoBagelCoffeeDONUTEclairFoodGravy'
>>> caseswitcher.to_dot(sample)
'avocado.bagel.coffee.donut.eclair.food.gravy'
>>> caseswitcher.to_kebab(sample)
'avocado-bagel-coffee-donut-eclair-food-gravy'
>>> caseswitcher.to_pascal(sample)
'AvocadoBagelCoffeeDONUTEclairFoodGravy'
>>> caseswitcher.to_snake(sample)
'avocado_bagel_coffee_donut_eclair_food_gravy'
>>> caseswitcher.to_title(sample)
'Avocado Bagel Coffee DONUT Eclair Food Gravy'
>>> caseswitcher.to_upper_dot(sample)
'AVOCADO.BAGEL.COFFEE.DONUT.ECLAIR.FOOD.GRAVY'
>>> caseswitcher.to_upper_kebab(sample)
'AVOCADO-BAGEL-COFFEE-DONUT-ECLAIR-FOOD-GRAVY'
>>> caseswitcher.to_upper_snake(sample)
'AVOCADO_BAGEL_COFFEE_DONUT_ECLAIR_FOOD_GRAVY'
```
