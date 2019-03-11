#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 6 by Diandra Vega"""


import conversions
import conversions_refactored
import unittest
import random


class conversionTests(unittest.TestCase):
    """Class for testing conversion functionality in conversions.py"""
    nums = random.sample(range(1, 100), 5)


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


    def testItemEqualsSelf(self):
        """convert() returns itself when converted from itself"""
        testcase = ['yards',
                    'miles',
                    'meters',
                    'fahrenheit',
                    'celsius',
                    'kelvin']

        for val in testcase:
            unit1=unit2 = val

            for num in self.nums:
                self.assertEqual(conversions_refactored.convert(unit1, unit2,
                                                                num), num)


class conversionsRefactoredTests(unittest.TestCase):
    """Unit testing for conversions_refactored.py"""
    nums = random.sample(range(1, 100), 5)


    def testConvertTemperatures(self):
        """convert() returns correct temperature unit conversions"""

        for val in self.nums:
            celsius_to_kelvin = float(val) + 273.15
            celsius_to_fahrenheit = float(val) * 9 / 5 + 32
            fahrenheit_to_celsius = (float(val) - 32) * 5 / 9
            fahrenheit_to_kelvin = (float(val) + 459.67) * 5 / 9
            kelvin_to_fahrenheit = float(val) * 9 / 5 - 459.67
            kelvin_to_celsius = float(val) - 273.15


            test1 = conversions_refactored.convert("celsius", "kelvin", val)
            test2 = conversions_refactored.convert("celsius", "fahrenheit",
                                                     val)
            test3 = conversions_refactored.convert("fahrenheit", "celsius",
                                                     val)
            test4 = conversions_refactored.convert("fahrenheit", "kelvin",
                                                     val)
            test5 = conversions_refactored.convert("kelvin", "fahrenheit",
                                                     val)
            test6 = conversions_refactored.convert("kelvin", "celsius", val)


            self.assertEqual(celsius_to_kelvin, test1,
                             "Celsius to Kelvin conversion failed")
            self.assertEqual(celsius_to_fahrenheit, test2,
                             "Celsius to Fahrenheit conversion failed")
            self.assertEqual(fahrenheit_to_celsius, test3,
                             "Fahrenheit to Celsius conversion failed")
            self.assertEqual(fahrenheit_to_kelvin, test4,
                             "Fahrenheit to Kelvin conversion failed")
            self.assertEqual(kelvin_to_fahrenheit, test5,
                             "Kelvin to Fahrenheit conversion failed")
            self.assertEqual(kelvin_to_celsius, test6,
                             "Kelvin to Celsius conversion failed")


    def testConvertDistance(self):
        """convert() returns correct distance conversions"""

        for val in self.nums:
            yards_to_miles = float(val) / 1760
            yards_to_meters = float(val) / 1.094
            meters_to_yards = float(val) * 1.094
            meters_to_miles = float(val) / 1609.344
            miles_to_yards = float(val) * 1760
            miles_to_meters = float(val) * 1609.344


            test1 = conversions_refactored.convert("yards", "miles", val)
            test2 = conversions_refactored.convert("yards", "meters", val)
            test3 = conversions_refactored.convert("meters", "yards", val)
            test4 = conversions_refactored.convert("meters", "miles", val)
            test5 = conversions_refactored.convert("miles", "yards", val)
            test6 = conversions_refactored.convert("miles", "meters", val)


            self.assertEqual(yards_to_miles, test1,
                             "Yards to Miles conversion failed")
            self.assertEqual(yards_to_meters, test2,
                             "Yards to Meters conversion failed")
            self.assertEqual(meters_to_yards, test3,
                             "Meters to Yards conversion failed")
            self.assertEqual(meters_to_miles, test4,
                             "Meters to Miles conversion failed")
            self.assertEqual(miles_to_yards, test5,
                             "Miles to Yards conversion failed")
            self.assertEqual(miles_to_meters, test6,
                             "Miles to Meters conversion failed")


    def testInvalidUnits(self):
        """convert() fails with invalid units"""
        testcase = {'test1': 'cat',
                    'test2': 'dog',
                    'test3': 'bird',
                    'test4': 'cow',
                    'test5': 'pig'}

        for key, val in testcase.iteritems():
            unit1 = key
            unit2 = val

            for num in self.nums:
                self.assertRaises(conversions_refactored.ConversionNotPossible,
                                  conversions_refactored.convert, unit1, unit2,
                                  num)


if __name__ == '__main__':
    unittest.main()
