#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 6 by Diandra Vega"""


import conversions
import unittest


class conversionTests(unittest.TestCase):
    """Class for testing conversion functionality"""
    celsius = range(1, 5)
    kelvin = 278.15
    fahrenheit = 32.0
    #to_celsius_from_kel = kelvin - 273.15
    #to_celsius_from_fh = (fahrenheit - 32) * 5/9


    def testConvertCelsiusToKelvin(self):
        """convertCelsiusToKelvin gives correct Kelvin conversion"""
        for val in celsius:
            to_kelvin = celsius + 273.15
            result = conversions.convertCelsiusToKelvin(val)
            self.assertEqual(to_kelvin, result)


    def testConvertCelsiusToFahrenheit(self):
        """convertCelsiusToFahrenheit gives correct Fahrenheit conversion"""
        for val in celsius:
            to_fahrenheit = celsius * (9 / 5) + 32
            result = conversions.convertCelsiusToFahrenheit(val)
            self.assertEqual(to_fahrenheit, result)


if __name__ == '__main__':
    unittest.main()
