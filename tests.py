#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 6 by Diandra Vega"""


import conversions
import unittest
import random


class conversionTests(unittest.TestCase):
    """Class for testing conversion functionality"""
    nums = random.sample(range(1, 100), 5)
    fahrenheit = random.sample(range(1, 100), 5)
    #to_celsius_from_kel = kelvin - 273.15
    #to_celsius_from_fh = (fahrenheit - 32) * 5/9


    def testConvertCelsiusToKelvin(self):
        """convertCelsiusToKelvin returns correct Kelvin conversion"""
        for celsius in self.nums:
            to_kelvin = float(celsius) + 273.15
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(to_kelvin, result)


    def testConvertCelsiusToFahrenheit(self):
        """convertCelsiusToFahrenheit returns correct Fahrenheit conversion"""
        for celsius in self.nums:
            to_fahrenheit = float(celsius) * 9 / 5 + 32
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(to_fahrenheit, result)


    def testConvertFahrenheitToCelsius(self):
        """convertFahrenheitToCelsius returns correct Celsius conversion"""
        for fahrenheit in self.nums:
            to_celsius = (float(fahrenheit) - 32) * 5 / 9
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(to_celsius, result)


    def testConvertFahrenheitToKelvin(self):
        """convertFahrenheitToKelvin returns correct Kelvin conversion"""
        for fahrenheit in self.nums:
            to_kelvin = (float(fahrenheit) + 459.67) * 5 / 9
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(to_kelvin, result)


    def testConvertKelvinToFahrenheit(self):
        """convertKelvinToFahrenheit returns correct Fahrenheit conversion"""
        for kelvin in self.nums:
            to_fahrenheit = float(kelvin) * 9 / 5 - 459.67
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(to_fahrenheit, result)


    def testConvertKelvinToCelsius(self):
        """convertKelvinToCelsius returns correct Celsius conversion"""
        for kelvin in self.nums:
            to_celsius = float(kelvin) - 273.15
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(to_celsius, result)


if __name__ == '__main__':
    unittest.main()
