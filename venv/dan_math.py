import unit_data as ud
import math

class Normalizer:
    def __init__(self, current_vec: ud.Vec2d, target_vec: ud.Vec2d):
        self.current_vec = current_vec
        self.target_vec = target_vec
        self.action_angle: float
        self.normalized_x: float
        self.normalized_y: float
        self.normalized_movement_vec: ud.Vec2d

        self.set_action_angle()
        self.set_normalized_x()
        self.set_normalized_y()
        self.get_movement_vector()

    def set_action_angle(self):
        self.action_angle = math.atan2((self.target_vec.y - self.current_vec.y), (self.target_vec.x - self.current_vec.x))

    def set_normalized_x(self):
        self.normalized_x = math.cos(self.action_angle)

    def set_normalized_y(self):
        self.normalized_y = math.sin(self.action_angle)

    def get_movement_vector(self):
        self.normalized_movement_vec = ud.Vec2d(self.normalized_x, self.normalized_y)
        return self.normalized_movement_vec