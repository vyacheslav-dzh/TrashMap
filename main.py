import os
from PIL import Image
import torch

LIMIT = 0.7

# Здесь модель работает не локально, а с репозитория, но веса использует, те которые мы обучили
model = torch.hub.load("ultralytics/yolov5", "custom", "custom_weights.pt")

images = []

for i in os.listdir("test"):
    path = os.path.join("test", i)
    img = Image.open(path)
    images.append(img)

results = model(images)

all_count = len(results.pandas().xyxy[0]["Class"])
full_count = len([i for i in results.pandas().xyxy[0]["Class"] if i])

if all_count != 0:
    pollution = full_count/all_count
    if pollution > LIMIT:
        print("Post c_mode = 1")
    else:
        print("Post c_mode = 0")
else:
    print("Objects didn't detected")

# results.pandas().xyxy[0]
