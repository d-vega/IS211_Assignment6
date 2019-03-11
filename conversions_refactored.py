#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Refactored version of conversions.py for IS211 Assignment 6"""


class ConversionNotPossible(Exception):
    """Custom class for conversion errors"""
    pass

def convert(fromUnit, toUnit, value):
    """Docstring 1"""


    ## Convert Temperatures ##


    if fromUnit.lower() == "celsius" and toUnit.lower() == "kelvin":
        celsius_to_kelvin = float(value) + 273.15
        return celsius_to_kelvin

    elif fromUnit.lower() == "celsius" and toUnit.lower() == "fahrenheit":
        celsius_to_fahrenheit = float(value) * 9 / 5 + 32
        return celsius_to_fahrenheit

    elif fromUnit.lower() == "fahrenheit" and toUnit.lower() == "celsius":
        fahrenheit_to_celsius = (float(value) - 32) * 5 / 9
        return fahrenheit_to_celsius

    elif fromUnit.lower() == "fahrenheit" and toUnit.lower() == "kelvin":
        fahrenheit_to_kelvin = (float(value) + 459.67) * 5 / 9
        return fahrenheit_to_kelvin

    elif fromUnit.lower() == "kelvin" and toUnit.lower() == "fahrenheit":
        kelvin_to_fahrenheit = float(value) * 9 / 5 - 459.67
        return kelvin_to_fahrenheit

    elif fromUnit.lower() == "kelvin" and toUnit.lower() == "celsius":
        kelvin_to_celsius = float(value) - 273.15
        return kelvin_to_celsius


    ## Convert Distance ##


    elif fromUnit.lower() == "yards" and toUnit.lower() == "miles":
        yards_to_miles = float(value) / 1760
        return yards_to_miles

    elif fromUnit.lower() == "yards" and toUnit.lower() == "meters":
        yards_to_meters = float(value) / 1.094
        return yards_to_meters

    elif fromUnit.lower() == "meters" and toUnit.lower() == "yards":
        meters_to_yards = float(value) * 1.094
        return meters_to_yards

    elif fromUnit.lower() == "meters" and toUnit.lower() == "miles":
        meters_to_miles = float(value) / 1609.344
        return meters_to_miles

    elif fromUnit.lower() == "miles" and toUnit.lower() == "yards":
        miles_to_yards = float(value) * 1760
        return miles_to_yards

    elif fromUnit.lower() == "miles" and toUnit.lower() == "meters":
        miles_to_meters = float(value) * 1609.344
        return miles_to_meters

    elif fromUnit.lower() == toUnit.lower():
        return value

    else:
        raise ConversionNotPossible("Invalid units used")
