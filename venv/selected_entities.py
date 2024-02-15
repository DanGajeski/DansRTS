import canvas_entities as ce
import unit_data as ud
import dan_math as dm

class Selected_Entities:
    def __init__(self):
        self.selected = []
        self.all = []
        self.target_vec: ud.Vec2d

    def add_to_selected_entities(self, new_entity):
        self.selected.append(new_entity)

    #possibly update later to utilize an entity ID?
    def remove_from_selected_entities(self, current_entity):
        self.selected.remove(current_entity)

    def remove_all_selected_entities(self):
        for count in self.selected:
            self.selected.pop()

    def is_empty(self):
        return self.selected == []

    def move_entities(self, target_vec: ud.Vec2d, all_entities: list):
        self.all = all_entities
        self.set_target_vec(target_vec)
        for entity in self.selected:
            for count in range(entity.speed):
                if not entity.check_if_entity_at_target_vec():
                        #if-no-collision
                    if self.check_entity_collision(entity):
                        entity.move_entity()
                        #if-collision
                    else:
                        if self.check_entity_x_collision(entity):
                            entity.move_entity_only_x()
                        elif self.check_entity_y_collision(entity):
                            entity.move_entity_only_y()

    def set_target_vec(self, target_vec: ud.Vec2d):
        self.target_vec = target_vec
        for entity in self.selected:
            entity.set_target_vec(self.target_vec)

    #aabb_blocker_tester_method
    #UPDATE=-> To include simple x and y movement if multiple entities stuck
    def check_entity_collision(self, entity):
        entity.update_normalizer()

        test_entity_displacement: int = 10

        can_move: bool = True
        test_movement_aabb = ud.AABB(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2)

        test_movement_aabb.x1 += entity.normalizer.normalized_movement_vec.x
        test_movement_aabb.y1 += entity.normalizer.normalized_movement_vec.y
        test_movement_aabb.x2 += entity.normalizer.normalized_movement_vec.x
        test_movement_aabb.y2 += entity.normalizer.normalized_movement_vec.y

        for other_entity in self.all:
            if other_entity.id != entity.id:
                #blocker_aabb_test = ud.AABB(other_entity.aabb.x1 - test_entity_displacement, other_entity.aabb.y1 - test_entity_displacement, other_entity.aabb.x2 + test_entity_displacement, other_entity.aabb.y2 + test_entity_displacement)
                #if blocker_aabb_test.check_aabb_in_aabb(test_movement_aabb):
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move

    def check_entity_x_collision(self, entity):
        entity.update_normalizer()

        can_move: bool = True
        test_movement_aabb = ud.AABB(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2)

        test_movement_aabb.x1 += entity.normalizer.normalized_movement_vec.x
        test_movement_aabb.x2 += entity.normalizer.normalized_movement_vec.x

        for other_entity in self.all:
            if other_entity.id != entity.id:
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move

    def check_entity_y_collision(self, entity):
        entity.update_normalizer()

        can_move: bool = True
        test_movement_aabb = ud.AABB(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2)

        test_movement_aabb.y1 += entity.normalizer.normalized_movement_vec.y
        test_movement_aabb.y2 += entity.normalizer.normalized_movement_vec.y

        for other_entity in self.all:
            if other_entity.id != entity.id:
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move






















