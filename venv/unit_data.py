from PIL import Image
from PIL import ImageTk
from pathlib import Path

class ImgInfo():
    def __init__(self):
        self.img_height: int = 20
        self.img_width: int = 20

        self.img_folder_path: str = "imgs"
        self.main_character_img_name: str = "happy_guy.png"
        self.img_file_location = Path(__file__).parent/self.img_folder_path

        self.main_character_img: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(self.img_file_location/self.main_character_img_name))

class Vec2d():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class AABB():
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def check_xy_in_aabb(self, x: float, y: float):
        return x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2

    def check_aabb_in_aabb(self, aabb_check):
        if self.check_xy_in_aabb(aabb_check.x1, aabb_check.y1):
            return True
        elif self.check_xy_in_aabb(aabb_check.x2, aabb_check.y2):
            return True
        elif self.check_xy_in_aabb(aabb_check.x1, aabb_check.y2):
            return True
        elif self.check_xy_in_aabb(aabb_check.x2, aabb_check.y1):
            return True
        else:
            return False