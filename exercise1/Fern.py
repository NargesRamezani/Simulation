import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import random



def f1(a):
    c = np.array([2, 4])  # نقطه ثابت
    theta_deg = -3
    theta = np.radians(theta_deg)
    scale_factor = 7 / 8.4

    point_scaled = (a - c) * scale_factor + c
    point_translated = point_scaled - c

    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]])

    point_rotated = rotation_matrix @ point_translated
    point_final = point_rotated + c
    
    return point_final



def f2(a):
    c = np.array([0.5, 0.2])  # نقطه ثابت
    theta_deg = 50
    theta = np.radians(theta_deg)
    scale_factor = 1.5 / 5

    point_scaled = a * scale_factor
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]])

    point_rotated = rotation_matrix @ point_scaled
    point_final = point_rotated + c
    
    return point_final


def f3(a):
    c = np.array([0.6, 0.3])  # نقطه ثابت
    theta_deg = -60
    theta = np.radians(theta_deg)
    shear_factor = 0.3
    scale_factor = 1.5 / 5

    point_scaled = a * scale_factor
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]])
    shear_matrix = np.array([
        [1, shear_factor],
        [0, 1]])

    point_rotated = rotation_matrix @ point_scaled
    point_sheared = shear_matrix @ point_rotated
    point_final = point_sheared + c
    
    return point_final

def f4(a):
    c = np.array([0.7, 0.4])  # نقطه ثابت
    scale_factor = 1.5 / 10

    point_final = a * scale_factor + c
    
    return point_final


