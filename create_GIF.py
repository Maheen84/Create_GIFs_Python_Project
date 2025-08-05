from PIL import Image
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, "frame")

frame_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg'))])

frames = [Image.open(os.path.join(folder_path, f)) for f in frame_files]

frames[0].save("output2.gif",
              save_all=True,
              append_images=frames[1:],
              duration=200,
              loop=0)

print("GIF saved as output2.gif")
