import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import logging
import requests
import datetime
from datetime import datetime

class Vector2:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

def get_line(factor):
    line_intervals = {
        (0, 5): Vector2(x=8.222, y=9.801),
        (5, 10): Vector2(x=8.122, y=9.727),
        (10, 15): Vector2(x=8.111, y=9.652),
        (15, 20): Vector2(x=8.100, y=9.577),
        (20, 25): Vector2(x=8.090, y=9.502),
        (25, 30): Vector2(x=8.080, y=9.427),
        (30, 35): Vector2(x=8.070, y=9.352),
        (35, 40): Vector2(x=8.060, y=9.277),
        (40, 45): Vector2(x=8.050, y=9.202),
        (45, 50): Vector2(x=8.040, y=9.127),
        (50, 55): Vector2(x=8.030, y=9.052),
        (55, 60): Vector2(x=8.020, y=8.977),
        (60, 65): Vector2(x=8.010, y=8.902),
        (65, 70): Vector2(x=8.000, y=8.827),
        (70, 75): Vector2(x=7.990, y=8.752),
        (75, 80): Vector2(x=7.980, y=8.677),
        (80, 85): Vector2(x=7.970, y=8.602),
        (85, 90): Vector2(x=7.960, y=8.527),
        (90, 95): Vector2(x=7.950, y=8.452),
        (95, 100): Vector2(x=7.940, y=8.377),
        (100, 105): Vector2(x=7.930, y=8.302),
        (105, 110): Vector2(x=7.920, y=8.227),
        (110, 115): Vector2(x=7.910, y=8.152),
        (115, 120): Vector2(x=7.900, y=8.077),
        (120, 125): Vector2(x=7.890, y=8.002),
        (125, 130): Vector2(x=7.880, y=7.927),
        (130, 135): Vector2(x=7.870, y=7.852),
        (135, 140): Vector2(x=7.860, y=7.777),
        (140, 145): Vector2(x=7.850, y=7.702),
        (145, 150): Vector2(x=7.840, y=7.627),
        (150, 155): Vector2(x=7.820, y=7.552),
        (155, 160): Vector2(x=7.800, y=7.477),
        (160, 165): Vector2(x=7.790, y=7.402),
        (165, 170): Vector2(x=7.780, y=7.327),
        (170, 175): Vector2(x=7.770, y=7.252),
        (175, 180): Vector2(x=7.760, y=7.177),
        (180, 185): Vector2(x=7.730, y=7.102),
        (185, 190): Vector2(x=7.710, y=7.027),
        (190, 195): Vector2(x=7.690, y=6.952),
        (195, 200): Vector2(x=7.670, y=6.877),
        (200, 205): Vector2(x=7.650, y=6.802),
        (205, 210): Vector2(x=7.640, y=6.727),
        (210, 215): Vector2(x=7.630, y=6.652),
        (215, 220): Vector2(x=7.620, y=6.577),
        (220, 225): Vector2(x=7.610, y=6.502),
        (225, 230): Vector2(x=7.600, y=6.427),
        (230, 235): Vector2(x=7.590, y=6.352),
        (235, 240): Vector2(x=7.580, y=6.277),
        (240, 245): Vector2(x=7.570, y=6.202),
        (245, 250): Vector2(x=7.560, y=6.127),
        (250, 255): Vector2(x=7.550, y=6.052),
        (255, 260): Vector2(x=7.540, y=5.977),
        (260, 265): Vector2(x=7.530, y=5.902),
        (265, 270): Vector2(x=7.520, y=5.827),
        (270, 275): Vector2(x=7.510, y=5.752),
        (275, 280): Vector2(x=7.500, y=5.677),
        (280, 285): Vector2(x=7.490, y=5.602),
        (285, 290): Vector2(x=7.480, y=5.527),
        (290, 295): Vector2(x=7.470, y=5.452),
        (295, 300): Vector2(x=7.460, y=5.377),
        (300, 305): Vector2(x=7.460, y=-0.018),
        (305, 310): Vector2(x=7.450, y=-0.288),
        (310, 315): Vector2(x=7.440, y=-0.558),
        (315, 320): Vector2(x=7.430, y=-0.828),
        (320, 325): Vector2(x=7.420, y=-1.098),
        (325, 330): Vector2(x=7.410, y=-1.368),
        (330, 335): Vector2(x=7.400, y=-1.638),
        (335, 340): Vector2(x=7.390, y=-1.908),
        (340, 345): Vector2(x=7.380, y=-2.178),
        (345, 350): Vector2(x=7.370, y=-2.448),
        (350, 355): Vector2(x=7.360, y=-2.718),
        (355, 360): Vector2(x=7.350, y=-2.988),
        (360, 365): Vector2(x=7.340, y=-3.258),
        (365, 370): Vector2(x=7.330, y=-3.528),
        (370, 375): Vector2(x=7.320, y=-3.798),
        (375, 380): Vector2(x=7.310, y=-4.068),
        (380, 385): Vector2(x=7.300, y=-4.338),
        (385, 390): Vector2(x=7.290, y=-4.608),
        (390, 395): Vector2(x=7.280, y=-4.878),
        (395, 400): Vector2(x=7.270, y=-5.148),
        (400, 405): Vector2(x=7.260, y=-5.418),
        (405, 410): Vector2(x=7.250, y=-5.688),
        (410, 415): Vector2(x=7.240, y=-5.958),
        (415, 420): Vector2(x=7.230, y=-6.228),
        (420, 425): Vector2(x=7.220, y=-6.498),
        (425, 430): Vector2(x=7.210, y=-6.768),
        (430, 435): Vector2(x=7.200, y=-7.038),
        (435, 440): Vector2(x=7.190, y=-7.308),
        (440, 445): Vector2(x=7.180, y=-7.578),
        (445, 450): Vector2(x=7.170, y=-7.848),
        (450, 455): Vector2(x=7.160, y=-8.118),
        (455, 460): Vector2(x=7.150, y=-8.388),
        (460, 465): Vector2(x=7.140, y=-8.658),
        (465, 470): Vector2(x=7.130, y=-8.928),
        (470, 475): Vector2(x=7.120, y=-9.198),
        (475, 480): Vector2(x=7.110, y=-9.468),
        (480, 485): Vector2(x=7.100, y=-9.738),
        (485, 490): Vector2(x=7.090, y=-10.008),
        (490, 495): Vector2(x=7.080, y=-10.278),
        (495, 500): Vector2(x=7.070, y=-10.548)
    }

    for (lower, upper), value in line_intervals.items():
        if lower < factor <= upper:
            return value

def getPred_Multiply(factor):
    ping_ranges = {
        (20, 30): 0.1010,
        (30, 40): 0.1110,
        (40, 50): 0.1185,
        (50, 60): 0.1225,
        (60, 70): 0.1260,
        (70, 80): 0.1292,
        (80, 90): 0.1302,
        (90, 100): 0.1312,
        (100, 110): 0.1330,
        (110, 120): 0.1352,
        (120, 130): 0.1405,
        (130, 140): 0.1495,
        (140, 150): 0.1550,
        (150, 160): 0.1580,
        (160, 170): 0.1660,
        (170, 180): 0.1685,
        (180, 190): 0.1855,
        (190, 200): 0.1875,
        (200, 210): 0.1925,
        (210, 220): 0.1950,
        (220, 230): 0.2015,
        (230, 240): 0.2038,
        (240, 250): 0.2048,
        (250, 260): 0.2065,
        (260, 270): 0.2090,
        (270, 280): 0.2115,
        (280, 290): 0.2185,
        (290, 300): 0.2235,
        (300, 310): 0.2255,
        (310, 320): 0.2315,
        (320, 330): 0.2350,
        (330, 340): 0.2405,
        (340, 350): 0.2430,
        (350, 360): 0.2475,
        (360, 370): 0.2500,
        (370, 380): 0.2535,
        (380, 390): 0.2560,
        (390, 400): 0.2590,
        (400, 410): 0.2615,
        (410, 420): 0.2638,
        (420, 430): 0.2665,
        (430, 440): 0.2690,
        (440, 450): 0.2715,
        (450, 460): 0.2738,
        (460, 470): 0.2765,
        (470, 480): 0.2788,
        (480, 490): 0.2810,
        (490, 500): 0.2835
    }

    for (lower, upper), value in ping_ranges.items():
        if lower < factor <= upper:
            return value

class ConfigGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bleeds gen!!:3")
        # Styling
        self.root.configure(bg="#FFFFFF")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#FFFFFF")
        self.style.configure("TLabel", background="#FFFFFF", foreground="#333")
        self.style.configure("TButton", background="#4CAF50", foreground="#FFF", font=('Helvetica', 10, 'bold'))
        self.style.map("TButton", background=[('active', '#43A047')])

        # Main frame to contain all widgets
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        # Add padding around the main frame
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(4, weight=1)

        # Variables to store widget values
        self.ping_var = tk.StringVar()
        self.type_var = tk.StringVar()
        self.prediction_var = tk.StringVar()
        self.external_var = tk.StringVar()

        # Other widgets for the Config Generator
        ttk.Label(self.main_frame, text="Ping:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, sticky="w")
        ttk.Entry(self.main_frame, textvariable=self.ping_var, font=('Helvetica', 12)).grid(row=0, column=1, sticky="we", pady=5)

        ttk.Label(self.main_frame, text="Type:", font=('Helvetica', 12, 'bold')).grid(row=1, column=0, sticky="w")
        ttk.Combobox(self.main_frame, values=['Rage', 'Blatant', 'Semi Legit', 'Legit'], textvariable=self.type_var, font=('Helvetica', 12)).grid(row=1, column=1, sticky="we", pady=5)

        ttk.Label(self.main_frame, text="Prediction:", font=('Helvetica', 12, 'bold')).grid(row=2, column=0, sticky="w")
        ttk.Combobox(self.main_frame, values=['Division', 'Multiplication'], textvariable=self.prediction_var, font=('Helvetica', 12)).grid(row=2, column=1, sticky="we", pady=5)

        ttk.Label(self.main_frame, text="External:", font=('Helvetica', 12, 'bold')).grid(row=3, column=0, sticky="w")
        ttk.Combobox(self.main_frame, values=['Celex', 'Severe', 'Ethic', 'Horizon', 'Santoware', 'Silence'], textvariable=self.external_var, font=('Helvetica', 12)).grid(row=3, column=1, sticky="we", pady=5)

        ttk.Button(self.main_frame, text="Generate", command=self.generate_config).grid(row=4, column=1, pady=10)

        # Bind events for window dragging
        root.bind("<ButtonPress-1>", self.on_drag_start)
        root.bind("<B1-Motion>", self.on_drag_motion)

        # Title bar frame
        self.title_bar = tk.Frame(root, bg="#202225", relief=tk.SUNKEN, bd=0)

        # Title label
        self.title_label = tk.Label(self.title_bar, text="Config!!:3", bg="#202225", fg="white", font=("Helvetica", 10))

    def send_webhook_message(self, config_filename):
        webhook_url = ""

        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

        message = f"## **A New Config!!!**, **Time:** **{current_time}**, **Configuration Name:** **{config_filename}**"
        data = {
            "content": message
        }

        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print("Webhook message sent successfully.")
        else:
            print(f"Failed to send webhook message. Status code: {response.status_code}")

    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def on_drag_motion(self, event):
        x = self.root.winfo_x() - self.drag_start_x + event.x
        y = self.root.winfo_y() - self.drag_start_y + event.y
        self.root.geometry(f"+{x}+{y}")

    def generate_config(self):
        ping = int(self.ping_var.get())
        type_selected = self.type_var.get()
        prediction_selected = self.prediction_var.get()
        external_selected = self.external_var.get()

        if ping < 0 or ping > 500:
            messagebox.showerror("Error", "Your Ping Must Be Between 1 - 500")
            return

        if not prediction_selected:
            messagebox.showerror("Error", "Please select a prediction type.")
            return

        if not type_selected:
            messagebox.showerror("Error", "Please select a blatancy type.")
            return
        
        if not external_selected:
            messagebox.showerror("Error", "Please select an external.")
            return

        solution = get_line(ping)

        # Prepare the configuration based on the prediction and blatancy type selected

        config =  {}
        if prediction_selected == 'Division':
            if type_selected == 'Blatant':
                config = {"type": "blatant", "prediction": "division", "aimbot_smoothing": "1.5", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "1"}
            elif type_selected == 'Legit':
                config = {"type": "legit", "prediction": "division", "aimbot_smoothing": "7.25", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "0.35"}
            elif type_selected == 'Semi Legit':
                config = {"type": "semi-legit", "prediction": "division", "aimbot_smoothing": "4", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "0.65"}
            elif type_selected == 'Rage':
                config = {"type": "rage", "prediction": "division", "aimbot_smoothing": "1", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "1.5"}
        elif prediction_selected == 'Multiplication':
            if type_selected == 'Blatant':
                config = {"type": "blatant", "prediction": "multiplication", "aimbot_smoothing": "1.5", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "1"}
            elif type_selected == 'Legit':
                config = {"type": "legit", "prediction": "multiplication", "aimbot_smoothing": "7.25", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "0.35"}
            elif type_selected == 'Semi Legit':
                config = {"type": "semi-legit", "prediction": "multiplication", "aimbot_smoothing": "4", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "0.65"}
            elif type_selected == 'Rage':
                config = {"type": "rage", "prediction": "multiplication", "aimbot_smoothing": "1", "aimbot_bind": "5", "aimbot_bind_mode": "1", "aimbot_sensitivity": "1.5"}

        if prediction_selected == 'Division':
            prediction_value = 1
            pred_type_line = ""  # Empty string, as pred_type should not be included for Division
        else:
            prediction_value = getPred_Multiply(ping)
            pred_type_line = 'pred_type = "1";\n'  # Include pred_type line for Multiplication

        config_templates = {
    'Celex': f"""aimbot-enabled = "1";
aimbot-smoothing = "{config['aimbot_smoothing']}";
camera-smoothing = "1";
aimbot-sensitivity = "{config['aimbot_sensitivity']}";
aimbot-bind = "{config['aimbot_bind']}";
aimbot-bind-mode = "{config['aimbot_bind_mode']}";
aimbot-part = "2";
streamproof = "0";
v-sync = "1";
show_name = "0";
show_boxes = "0";
show_fov = "0";
show_deadzone = "0";
show_tracers = "0";
prediction = "1";
stickyaim = "1";
teamcheck = "0";
knockcheck = "0";
aimbot-fov = "1000";
filled_fov = "0";
aimbot-deadzone = "0";
filled_deadzone = "0";
pred_x = "{solution.x}";
pred_y = "{solution.y}";
pred = "{prediction_value}";
x_offset = "0";
y_offset = "0";
deadzone_flag = "0";
fov_flag = "0";
prediction_dot = "0";
pred_dot_type = "0";
tracer_type = "0";
shake = "0";
shake_x = "0";
shake_y = "0";
box_type = "0";
aimbot_type = "1";
no_jump = "1";
noclip = "0";
{pred_type_line}""",  # Config template for External1
    'Severe': f"""1-waypoint = "PlaceHolder:[position]-(0.000000,0.000000,0.000000)";
prediction_type = "Static";
transform = "WorldToScreenPoint";
type = "2D_AABB";
tname = "Username";
box = "Box";
bot = "Mouse";
apart = "HumanoidRootPart";
a_type = "Exponential";
s_type = "Bodyshot";
cbased = "internal";
aim_key_name = "SIDE_MOUSE";
font = "proxyma";
vallign = "Buttom_Left";
cursor_url = "none";
background_url = "none";
macro_pov = "third_person";
macrokey = "E";
shape = "Sphere";
tp_part = "Head";
tp_method = "behind";
flightkey = "F";
walkspeedkey = "G";
ragekey = "Q";
setkey = "V";
back_allign_x = "0";
back_allign_y = "0";
tip_allign = "30";
fov = "360";
predict_x = {solution.x};
predict_y = {solution.y};
drop = "0";
speed = "0.08";
stablization = "0.3";
distance = "500";
adistance = "1953.09";
vdistance = "100";
clsplr_d = "100";
cdistance = "150";
view = "10";
thickness = "1";
restrictor = "1";
noise = "0";
intensity = "20";
dfov = "0";
chealth = "3";
radius = "150";
hair_size = "10";
zoom = "0.5";
ping_delay = "2";
csmoothness = "5";
smoothness = "{config['aimbot_smoothing']}";
strength = "{config['aimbot_sensitivity']}";
multipiler = "0";
flight_speed = "5";
transport_speed = "1";
decreaser = "0";
increaser = "1";
sensitivity = "0.5";
avatar_allign = "608";
vert_dec = "15";
unlock_on_death = "0";
bounce = "0";
show_avatar = "1";
lock_indicator = "1";
speed_stab = "0";
enb_stab = "0";
sensitive = "0";
sound = "0";
abs_v = "0";
hide_cursor = "0";
anti_ground = "0";
keybind_logger = "0";
server_transparent = "0";
display_server = "0";
waypoints = "0";
visualize_waypoint = "0";
high_transport = "0";
rage_fov = "0";
radar_value = "0";
rage_snaplines = "0";
hold_rage = "0";
look_at_plr = "0";
rage_teleport = "0";
unlock_reload = "0";
manipulate_loop = "0";
manipulate_char = "0";
gun_check = "0";
character_fly = "0";
client_lag = "1";
show_prediction = "0";
mouse_tp = "0";
material_esp = "0";
m_toggle = "0";
auto_macro = "0";
auto_scroll = "1";
unlock_knockout = "0";
smart_fov = "1";
rdirections = "1";
radar = "0";
crosshair = "0";
offscreen = "0";
certain_health = "0";
toggle = "1";
disable_images = "0";
fov_zone = "0";
vdotted = "0";
c_allign = "0";
dmg_indicator = "0";
vtransprent = "0";
ping_interpolation = "0";
snaplines_a = "0";
snaplines_v = "0";
chams = "0";
cfilled = "0";
cflat = "0";
limit = "0";
center = "0";
allign = "1";
loutline = "1";
background = "1";
indicator = "1";
stats = "0";
name = "0";
lhealth = "0";
override = "0";
team_check = "0";
invisible_check = "0";
ffield_check = "0";
close_ind = "0";
close_camera = "1";
sticky_aim = "1";
ohealth = "0";
esp_box = "0";
esp_ground = "0";
esp_bone = "0";
forientation = "0";
ooutline = "1";
arc_bar = "0";
sfont = "1";
oname = "1";
aimbot = "1";
amplify = "0";
vision = "0";
CAPS = "1";
circle_filled = "0";
cfilled_hcolor = "0";
box_filled = "0";
bfilled_hcolor = "0";
chams_filled = "0";
hfilled_hcolor = "0";
fov_circle = "0";
dotted = "0";
perlin_noise = "0";
auto_reload = "0";
arsenal_hitbox = "0";
fly_hold = "0";
gun_chams = "0";
aim_delay = "0";
delay = "70";
walkspeed = "80";
jumppower = "80";
aim_key = "5";
flight = "70";
macro = "69";
rage = "81";
walkspeedk = "71";
m_delay = "25";
range = "10";
rage_size = "30";
tp_height = "600";
wtp_height = "0";
rset = "86";""",
    'Ethic': f"""{{"aimbot":true,"aimkey":6,"aimkeymethod":0,"aimpart":2,"box":false,"esp":false,"fov":360,"fovcircle":false,"healthcheck":false,"knockcheck":true,"name":false,"prediction":true,"prediction_x":{solution.x},"prediction_y":{solution.y},"sensitivity":1,"smoothness_x":{config['aimbot_smoothing']},"smoothness_y":{config['aimbot_smoothing']},"sticky":true,"streamproof":false,"teamcheck":false,"tracers":false,"vsync":true}}""",
    'Horizon': f"""{{"aimbot":true,"aimkey":69,"aimkeymethod":0,"aimpart":0,"box":false,"esp":false,"fov":360,"fovcircle":false,"healthcheck":false,"knockcheck":false,"name":false,"prediction":true,"prediction_x":{solution.x},"prediction_y":{solution.y},"sensitivity":1,"smoothness_x":{config['aimbot_smoothing']},"smoothness_y":{config['aimbot_smoothing']},"sticky":true,"streamproof":false,"teamcheck":false,"tracers":false,"vsync":true}}""",
    'Santoware': f"""{{"aimbot":true,"aimkey":6,"aimkeymethod":0,"aimpart":2,"autopred":false,"autoresolve":false,"box":false,"datentime":false,"deadzone":false,"deadzone_fov_filled":false,"distance_esp":false,"esp":false,"fillboxtype":0,"filledbox":false,"fov":99,"fov_filled":false,"fovcircle":false,"healthbar":false,"healthcheck":false,"healthinfo":false,"knockcheck":false,"local_box":false,"max_dist":10000,"name":false,"outline":false,"prediction":true,"prediction_x":{solution.x},"prediction_y":{solution.y},"rainbowbox":false,"rainbowfov":false,"rainbowfovfilled":false,"rainbowmode":false,"range":0.0,"range_mult":0.0,"resolver":true,"sensitivity":2.35,"shake_value":0.0,"shake_x":0.0,"shake_y":0.0,"shaketype":0,"show_deadzone":false,"smoothness_x":{config['aimbot_smoothing']},"smoothness_y":{config['aimbot_smoothing']},"streamproof":false,"team_check_esp":false,"teamcheck":false,"tracers":false,"velocity_threshold":39.0,"visualisetarget":true,"vsync":false,"watermark":false,"x_offset":0,"y_offset":0}}""",
    'Silence': f"""{{"aimbot":true,"aimkey":6,"aimkeymethod":0,"aimpart":2,"box":false,"esp":false,"fov":360,"fovcircle":false,"healthcheck":false,"knockcheck":true,"name":false,"prediction":true,"prediction_x":{solution.x},"prediction_y":{solution.y},"sensitivity":1,"smoothness_x":{config['aimbot_smoothing']},"smoothness_y":{config['aimbot_smoothing']},"sticky":true,"streamproof":false,"teamcheck":false,"tracers":false,"vsync":true}}"""
}
        
        config_template = config_templates.get(external_selected)

        if config_template is None:
         messagebox.showerror("Error", "No config template found for the selected external.")
         return

        # Save the configuration to a file
        config_filename = f"Bleed-{ping}-'ping'-{config['prediction']}-{config['type']}.cfg"

        with open(config_filename, 'w') as file:
            file.write(config_template)

            logging.info(f"Config generated: {config_filename}")
            self.send_webhook_message(config_filename)

        messagebox.showinfo("Here you go!!:3", f"Config has been generated!!:3 '{config_filename}'.")

# Create the main application window
root = tk.Tk()
app = ConfigGeneratorApp(root)

# Set initial size of the window and center it on the screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()