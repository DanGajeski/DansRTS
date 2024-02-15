import unit_data as ud
import dan_math as dm

class Entity:
    def __init__(self, Vec2d: ud.Vec2d, id):
        self.id = id
        self.img_info = ud.ImgInfo()
        self.pos = Vec2d
        self.img = self.img_info.main_character_img
        self.img_width = self.img_info.img_width
        self.img_height = self.img_info.img_height
        self.target_vec: ud.Vec2d
        self.distance_from_target_vec: float
        #low-level-tick-tied-entity-speed
        self.speed: int = 6
        self.aabb = ud.AABB(self.pos.x, self.pos.y, (self.pos.x + self.img_info.img_width), (self.pos.y + self.img_info.img_height))
        self.normalizer: dm.Normalizer

        self.immobile_tick_counter: int = 0

    def set_target_vec(self, target_vec: ud.Vec2d):
        self.target_vec = target_vec

    def update_normalizer(self):
        self.normalizer = dm.Normalizer(self.pos, self.target_vec)

    def move_entity(self):
        self.update_normalizer()

        self.pos.x += self.normalizer.normalized_movement_vec.x
        self.pos.y += self.normalizer.normalized_movement_vec.y
        self.aabb.x1 += self.normalizer.normalized_movement_vec.x
        self.aabb.y1 += self.normalizer.normalized_movement_vec.y
        self.aabb.x2 += self.normalizer.normalized_movement_vec.x
        self.aabb.y2 += self.normalizer.normalized_movement_vec.y

    def move_entity_only_x(self):
        self.update_normalizer()

        self.pos.x += self.normalizer.normalized_movement_vec.x
        self.aabb.x1 += self.normalizer.normalized_movement_vec.x
        self.aabb.x2 += self.normalizer.normalized_movement_vec.x

    def move_entity_only_y(self):
        self.update_normalizer()

        self.pos.y += self.normalizer.normalized_movement_vec.y
        self.aabb.y1 += self.normalizer.normalized_movement_vec.y
        self.aabb.y2 += self.normalizer.normalized_movement_vec.y

    def check_if_entity_at_target_vec(self):
        if self.pos.x < self.target_vec.x + 1 and self.pos.x > self.target_vec.x - 1 and self.pos.y < self.target_vec.y + 1 and self.pos.y > self.target_vec.y - 1:
            return True
        else:
            return False

