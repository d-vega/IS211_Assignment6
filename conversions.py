#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 6 by Diandra Vega"""


def convertCelsiusToKelvin(celsius):
    """Convert Celsius to Kelvin.

    ARGS:
        celsius (int): Numerical value to be converted to Kelvin.

    RETURNS:
        float: Returns floating numerical value of Kelvin.

    EXAMPLES:
        >>> convertCelsiusToKelvin(23)
        296.15
    """
    to_kelvin = float(celsius) + 273.15
    return to_kelvin


def convertCelsiusToFahrenheit(celsius):
    """Convert Celsius to Fahrenheit.

    ARGS:
        celsius (int): Numerical value to be converted to Fahrenheit.

    RETURNS:
        float: Returns floating numerical value of Fahrenheit.

    EXAMPLES:
        >>> convertCelsiusToFahrenheit(18)
        64.4
    """
    to_fahrenheit = float(celsius) * 9 / 5 + 32
    return to_fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    """Convert Fahrenheit to Celsius.

    ARGS:
        fahrenheit (int): Numerical value to be converted to Celsius.

    RETURNS:
        float: Returns floating numerical value of Celsius.

    EXAMPLES:
        >>> convertFahrenheitToCelsius(23)
        28.8888888889
    """
    to_celsius = (float(fahrenheit) - 32) * 5 / 9
    return to_celsius


def convertFahrenheitToKelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin.

    ARGS:
        fahrenheit (int): Numerical value to be converted to Kelvin.

    RETURNS:
        float: Returns floating numerical value of Kelvin.

    EXAMPLES:
        >>> convertFahrenheitToKelvin(78)
        298.705555556
    """
    to_kelvin = (float(fahrenheit) + 459.67) * 5 / 9
    return to_kelvin


def convertKelvinToFahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit.

    ARGS:
        kelvin (int): Numerical value to be converted to Fahrenheit.

    RETURNS:
        float: Returns floating numerical value of Fahrenheit.

    EXAMPLES:
        >>> convertKelvinToFahrenheit(301)
        82.13
    """
    to_fahrenheit = float(kelvin) * 9 / 5 - 459.67
    return to_fahrenheit


def convertKelvinToCelsius(kelvin):
    """Convert Kelvin to Celsius.

    ARGS:
        kelvin (int): Numerical value to be converted to Celsius.

    RETURNS:
        float: Returns floating numerical value of Celsius.

    EXAMPLES:
        >>> convertKelvinToCelsius(393)
        119.85
    """
    to_celsius = kelvin - 273.15
    return to_celsius
