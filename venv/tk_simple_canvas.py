import tkinter as tk
import unit_data as ud
import canvas_entities as ce
import selected_entities as se
import dan_math as dm
import math as math


class TkWindow():

    def __init__(self, canvas_width, canvas_height):
        #contianer_frame_main_window_offset
        self.container_frame_main_window_offset: double = 10.0

        self.canvas_width: float = canvas_width
        self.canvas_height: float = canvas_height
        self.main_window_height: float = self.canvas_width + (self.container_frame_main_window_offset*2)
        self.main_window_width: float = self.canvas_height + (self.container_frame_main_window_offset*2)

        #main_window_dimensions_geometry_object_formatted
        self.main_window_dimensions_geometry_formatted: string = str(int(self.main_window_width)) + "x" + str(int(self.main_window_height))
        #main_window_title
        self.main_window_title_text: str = "Dan's Fuckin' RTS"
        #canvas_color
        self.canvas_bg_color: str = "#00FF00"

        #init_window
        self.main_window = tk.Tk()
        self.main_window.geometry(self.main_window_dimensions_geometry_formatted)
        self.main_window.title(self.main_window_title_text)
        #init_frame
        self.container_frame = tk.Frame(self.main_window, width=self.canvas_width, height=self.canvas_height)
        self.container_frame.place(x=self.container_frame_main_window_offset, y=self.container_frame_main_window_offset)
        #self.container_frame.place(x=0,y=0)
        #init_canvas
        self.canvas = tk.Canvas(self.container_frame, bg=self.canvas_bg_color, width=self.canvas_width, height=self.canvas_height)
        self.canvas.place(x=0,y=0)

        self.player_entity: ce.Entity = ce.Entity(ud.Vec2d(50.0, 50.0), 1)
        self.game_entity_one: ce.Entity = ce.Entity(ud.Vec2d(100.0, 100.0), 2)
        self.game_entity_two: ce.Entity = ce.Entity(ud.Vec2d(200.0, 200.0), 3)
        self.game_entity_three: ce.Entity = ce.Entity(ud.Vec2d(300.0, 300.0), 4)
        self.game_entity_four: ce.Entity = ce.Entity(ud.Vec2d(400.0, 400.0), 5)
        self.game_entity_five: ce.Entity = ce.Entity(ud.Vec2d(200.0, 100.0), 6)

        #inits w/ player_entity and game_entity_one, game_entity_two
        self.all_entities: list = [self.player_entity, self.game_entity_one, self.game_entity_two, self.game_entity_three, self.game_entity_four]

        #default-target_vec_value
        self.target_vec: ud.Vec2d = ud.Vec2d(100.0, 100.0)

        #FOR-PRINT-TESTING-ONLY
        #self.example_entity: ce.Entity = self.game_entity_one
        self.x_differential: int = 0
        self.y_differential: int = 0

        #game_spaceNON_UI_ELEMENTS
        self.selected_entities = se.Selected_Entities()
        self.origin_x: float = 0.0
        self.origin_y: float = 0.0
        self.destination_x: float = 0.0
        self.destination_y: float = 0.0
        self.unit_selector_enabled: bool = False
        self.motion_selection_aabb: ut.AABB = ud.AABB(0,0,0,0)

        for entity in self.all_entities:
            self.display_entity(entity)
        self.set_window_bindings()
        self.tick()

    def get_mouse_x_location(self):
        x = self.main_window.winfo_pointerx()
        return (self.main_window.winfo_pointerx() - self.main_window.winfo_rootx()) - self.container_frame_main_window_offset
    def get_mouse_y_location(self):
        y = self.main_window.winfo_pointery()
        return (self.main_window.winfo_pointery() - self.main_window.winfo_rooty()) - self.container_frame_main_window_offset

    def set_target_movement_location(self):
        self.target_vec = ud.Vec2d(self.get_mouse_x_location(), self.get_mouse_y_location())

    def set_window_bindings(self):
        self.main_window.bind('<Button-3>', lambda event: self.set_target_movement_location())
        self.main_window.bind('<Button-1>', lambda event: self.set_unit_selector_origin())
        self.main_window.bind('<ButtonRelease-1>', lambda event: self.button_release_checks())

    def set_unit_selector_origin(self):
        origin_on_unit: bool = False
        selecting_entity: ce.Entity

        self.origin_x = self.get_mouse_x_location()
        self.origin_y = self.get_mouse_y_location()

        for entity in self.all_entities:
            if entity.aabb.check_xy_in_aabb(self.origin_x, self.origin_y):
                origin_on_unit = True
                selecting_entity = entity
                continue

        if origin_on_unit:
            self.select_entity(selecting_entity)
        else:
            self.enable_unit_selector()

    def select_entity(self, entity):
        self.selected_entities.add_to_selected_entities(entity)

    def enable_unit_selector(self):
        self.unit_selector_enabled = True
        self.motion_selection_aabb.x1 = self.origin_x
        self.motion_selection_aabb.x2 = self.origin_y

    def make_selection(self):
        #clear-selected-entities-first
        self.selected_entities.remove_all_selected_entities()
        for entity in self.all_entities:
            if self.motion_selection_aabb.check_aabb_in_aabb(entity.aabb):
                self.selected_entities.add_to_selected_entities(entity)

    def button_release_checks(self):
        if self.unit_selector_enabled:
            self.unit_selector_enabled = False
            self.destination_x = self.get_mouse_x_location()
            self.destination_y = self.get_mouse_y_location()

            self.motion_selection_aabb.x2 = self.destination_x
            self.motion_selection_aabb.y2 = self.destination_y

            self.make_selection()

    def draw_unit_selector(self):
        current_destination_x = self.get_mouse_x_location()
        current_destination_y = self.get_mouse_y_location()
        self.canvas.create_rectangle(self.origin_x, self.origin_y, current_destination_x, current_destination_y, outline='white')

    def run_main_window(self):
        self.main_window.mainloop()

    def highlight_selected_entities(self):
        for entity in self.selected_entities.selected:
            self.canvas.create_rectangle(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2, outline='red', width=2)

    def display_entity(self, entity: ce.Entity):
        self.canvas.create_image(entity.pos.x, entity.pos.y, image=entity.img, anchor=tk.NW)

    def display_all_elements(self):
        if self.unit_selector_enabled:
            self.draw_unit_selector()
        for entity in self.all_entities:
            self.display_entity(entity)
            if not self.selected_entities.is_empty():
                self.highlight_selected_entities()

    def tick(self):
        self.main_window.after(60, self.tick)
        self.canvas.delete('all')

        if not self.selected_entities.is_empty():
            self.selected_entities.move_entities(self.target_vec, self.all_entities)

        self.display_all_elements()