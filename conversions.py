#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 6 by Diandra Vega"""


def convertCelsiusToKelvin(celsius):
    """Convert Celsius to Kelvin"""
    to_kelvin = float(celsius) + 273.15
    return to_kelvin


def convertCelsiusToFahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    to_fahrenheit = float(celsius) * 9 / 5 + 32
    return to_fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    to_celsius = (float(fahrenheit) - 32) * 5 / 9
    return to_celsius


def convertFahrenheitToKelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    to_kelvin = (float(fahrenheit) + 459.67) * 5 / 9
    return to_kelvin


def convertKelvinToFahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    to_fahrenheit = float(kelvin) * 9 / 5 - 459.67
    return to_fahrenheit


def convertKelvinToCelsius(kelvin):
    """Convert Kelvin to Celsius"""
    to_celsius = kelvin - 273.15
    return to_celsius
