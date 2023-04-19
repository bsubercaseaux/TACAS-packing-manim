from manim import *
import numpy as np

class CurvedEdge(ArcBetweenPoints):
    def __init__(self, start, end, angle=..., radius=None, buff=0, **kwargs):
        if buff > 0:
            start_to_end = (end - start)
            start_to_end = np.array([start_to_end[0], start_to_end[1]])
            rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            rotation_matrix_end = np.array([[np.cos(PI - angle), -np.sin(PI - angle)], [np.sin(PI - angle), np.cos(PI - angle)]])
            new_v_start = rotation_matrix@(start_to_end / np.linalg.norm(start_to_end)) * buff
            new_v_end = rotation_matrix_end@(start_to_end / np.linalg.norm(start_to_end)) * buff
            padded_new_v_start = np.array([new_v_start[0], new_v_start[1], 0])
            padded_new_v_end = np.array([new_v_end[0], new_v_end[1], 0])
            
            start += padded_new_v_start
            end += padded_new_v_end
    
        super().__init__(start, end, -angle, radius, **kwargs)
        