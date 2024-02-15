import tk_simple_canvas
import unit_data
import canvas_entities as ce

class RTSMain:
    def __init__(self):
        self.canvas_width: float = 500.0
        self.canvas_height: float = 500.0

        self.game_area: tk_simple_canvas.TkWindow = tk_simple_canvas.TkWindow(canvas_width=self.canvas_width, canvas_height=self.canvas_height)
        self.img_info: unit_data.ImgInfo = unit_data.ImgInfo()

rtsmain = RTSMain()
rtsmain.game_area.run_main_window()