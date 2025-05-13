# -*- coding: utf-8 -*-
"""
Created on Mon May 12 16:16:51 2025

@author: Brett
"""

def miles_to_km(miles):
    try:
        return round(float(miles) * 1.60934, 2)
    except ValueError:
        raise ValueError("Input must be a number")