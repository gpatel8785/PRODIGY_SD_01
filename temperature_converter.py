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


    @classmethod
    def convert_temperature(cls, temperature: float, from_unit: str) -> Dict[str, float]:
        """
        Convert temperature from one unit to all other units
        
        Args:
            temperature: Temperature value to convert
            from_unit: Original unit ('C', 'F', 'K')
            
        Returns:
            Dictionary with converted temperatures in all units
        """
        from_unit = from_unit.upper()
        
        # Validate input
        is_valid, error_msg = cls.validate_temperature(temperature, from_unit)
        if not is_valid:
            raise ValueError(error_msg)
        
        # Convert to all units
        if from_unit == 'C':
            celsius = temperature
            fahrenheit = cls.celsius_to_fahrenheit(temperature)
            kelvin = cls.celsius_to_kelvin(temperature)
        elif from_unit == 'F':
            fahrenheit = temperature
            celsius = cls.fahrenheit_to_celsius(temperature)
            kelvin = cls.fahrenheit_to_kelvin(temperature)
        elif from_unit == 'K':
            kelvin = temperature
            celsius = cls.kelvin_to_celsius(temperature)
            fahrenheit = cls.kelvin_to_fahrenheit(temperature)
        else:
            raise ValueError(f"Invalid unit '{from_unit}'. Use C, F, or K.")
        
        return {
            'celsius': celsius,
            'fahrenheit': fahrenheit,
            'kelvin': kelvin
        }
def display_header():
    """Display program header with task information"""
    print("=" * 60)
    print("???  TEMPERATURE CONVERSION PROGRAM")
    print("   Prodigy InfoTech Software Development Internship")
    print("   Task-01: Temperature Conversion Program")
    print("=" * 60)
    print()

def display_menu():
    """Display unit selection menu"""
    print("?? Available Temperature Units:")
    print("   [C] Celsius (°C)")
    print("   [F] Fahrenheit (°F)")  
    print("   [K] Kelvin (K)")
    print()

def get_temperature_input() -> Tuple[float, str]:
    """
    Get temperature value and unit from user input
    
    Returns:
        Tuple of (temperature_value, unit)
    """
    while True:
        try:
            # Get temperature value
            temp_input = input("???  Enter temperature value: ").strip()
            if not temp_input:
                print("? Please enter a temperature value.")
                continue
                
            temperature = float(temp_input)
            
            # Get unit
            display_menu()
            unit_input = input("?? Enter unit (C/F/K): ").strip().upper()
            
            if unit_input not in ['C', 'F', 'K']:
                print("? Invalid unit. Please enter C, F, or K.")
                continue
                
            return temperature, unit_input
            
        except ValueError:
            print("? Invalid temperature value. Please enter a number.")
            continue
    
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

