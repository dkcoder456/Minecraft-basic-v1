from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from PIL import Image
import os
import random

# Create assets directory if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

# Generate textures
def create_texture(name, color):
    img = Image.new('RGB', (128, 128), color)
    # Add some noise for texture
    for x in range(128):
        for y in range(128):
            if random.random() > 0.8:
                img.putpixel((x, y), (max(0, color[0]-20), max(0, color[1]-20), max(0, color[2]-20)))
    img.save(f'assets/{name}.png')

# Generate block textures
create_texture('grass_block', (34, 139, 34))  # Green
create_texture('stone_block', (128, 128, 128))  # Gray
create_texture('brick_block', (139, 69, 19))  # Brown
create_texture('skybox', (135, 206, 235))  # Sky blue
create_texture('wood_block', (139, 69, 19))  # Brown (Wood)
create_texture('leaves_block', (34, 139, 34))  # Green (Leaves)
create_texture('sand_block', (194, 178, 128))  # Sand
create_texture('water_block', (64, 164, 223))  # Water

app = Ursina()

# Load the generated textures
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
sky_texture = load_texture('assets/skybox.png')
wood_texture = load_texture('assets/wood_block.png')
leaves_texture = load_texture('assets/leaves_block.png')
sand_texture = load_texture('assets/sand_block.png')
water_texture = load_texture('assets/water_block.png')

# Rest of your game code remains the same
current_texture = grass_texture

def update():
    global current_texture
    if held_keys['1']: current_texture = grass_texture
    if held_keys['2']: current_texture = stone_texture
    if held_keys['3']: current_texture = brick_texture
    if held_keys['4']: current_texture = wood_texture
    if held_keys['5']: current_texture = leaves_texture
    if held_keys['6']: current_texture = sand_texture
    if held_keys['7']: current_texture = water_texture

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=1
        )
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal, texture=current_texture)
            if key == 'right mouse down':
                destroy(self)

# Generate terrain with different textures
for z in range(25): 
    for x in range(25):
        if (x + z) % 5 == 0:
            voxel = Voxel(position=(x,0,z), texture=grass_texture)
        elif (x + z) % 5 == 1:
            voxel = Voxel(position=(x,0,z), texture=stone_texture)
        elif (x + z) % 5 == 2:
            voxel = Voxel(position=(x,0,z), texture=wood_texture)
        elif (x + z) % 5 == 3:
            voxel = Voxel(position=(x,0,z), texture=sand_texture)
        else:
            voxel = Voxel(position=(x,0,z), texture=water_texture)

player = FirstPersonController()
Sky(texture=sky_texture)

app.run()
