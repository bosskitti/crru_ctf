import shutil
import os

src = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/gaming_diagram_labeled_1784041660564.png"
dst_static = "/home/kali/crru_ctf/CTFd/CTFd/themes/core/static/img/gaming_diagram_labeled.png"
dst_assets = "/home/kali/crru_ctf/CTFd/CTFd/themes/core/assets/img/gaming_diagram_labeled.png"

# Create directories if they don't exist
os.makedirs(os.path.dirname(dst_static), exist_ok=True)
os.makedirs(os.path.dirname(dst_assets), exist_ok=True)

# Copy the file
shutil.copy(src, dst_static)
shutil.copy(src, dst_assets)
print("Copied successfully!")
