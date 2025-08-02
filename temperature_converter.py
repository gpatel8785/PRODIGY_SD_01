#!/usr/bin/env python3
"""
PRODIGY_SD_01 - Temperature Conversion Program
Prodigy InfoTech Software Development Internship - Task 01

A comprehensive Python program that converts temperatures between 
Celsius, Fahrenheit, and Kelvin scales.

Author: Gaurav Patel
Date: 02, August 2025
Task: Build a Temperature Conversion Program
"""

import sys
from typing import Dict, Tuple, Optional

class TemperatureConverter:
    """
    A comprehensive temperature conversion class supporting Celsius, Fahrenheit, and Kelvin.
    Includes validation for absolute zero limits and error handling.
    """
    
    # Absolute zero constants for validation
    ABSOLUTE_ZERO = {
        'C': -273.15,  # Celsius
        'F': -459.67,  # Fahrenheit  
        'K': 0.0       # Kelvin
    }
    
    UNIT_NAMES = {
        'C': 'Celsius',
        'F': 'Fahrenheit', 
        'K': 'Kelvin'
    }
    
    UNIT_SYMBOLS = {
        'C': '°C',
        'F': '°F',
        'K': 'K'
    }

    @classmethod
    def validate_temperature(cls, temperature: float, unit: str) -> Tuple[bool, str]:
        """
        Validate temperature against absolute zero limits
        
        Args:
            temperature: Temperature value to validate
            unit: Unit of measurement ('C', 'F', 'K')
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        unit = unit.upper()
        if unit not in cls.ABSOLUTE_ZERO:
            return False, f"Invalid unit '{unit}'. Use C, F, or K."
        
        absolute_zero = cls.ABSOLUTE_ZERO[unit]
        if temperature < absolute_zero:
            return False, f"Temperature cannot be below absolute zero ({absolute_zero}{cls.UNIT_SYMBOLS[unit]})"
        
        return True, ""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Convert Celsius to Kelvin"""
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """Convert Fahrenheit to Kelvin"""
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Convert Kelvin to Celsius"""
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """Convert Kelvin to Fahrenheit"""
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

if __name__ == "__main__":
    print("Temperature Converter - Initial Setup")