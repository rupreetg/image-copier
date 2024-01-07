import base64
import subprocess

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def run_node_subprocess(node_script, arg):
    command = ["node", node_script] + [arg]
    subprocess.run(command)
