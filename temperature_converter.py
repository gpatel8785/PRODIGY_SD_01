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
    """
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Convert Celsius to Kelvin"""
        return celsius + 273.15

if __name__ == "__main__":
    print("Temperature Converter - Initial Setup")