import os
import pprint

file = "/home/simon/.steam/debian-installation/steamapps/common/ProjectZomboid/media/scripts/mannequins.txt"


with open(file, "r") as f:
    for line in f:
        if "mannequin " in line:
            parts = line.strip().split()
            if parts:
                print("*<code>" + parts[-1] + "</code>")


print("\n\n")

folder = "/home/simon/.steam/debian-installation/steamapps/common/ProjectZomboid/media/textures/Body"

contains = [
    "F_",
    "M_",
    "Female",
    "Male",
    "Mannequin",
]

files = []

for filename in os.listdir(folder):
    if any(substr in filename for substr in contains):
        files.append(filename)

files.append("Skeleton.png")
files.append("SkeletonBurned.png")
files.append("SkeletonMuscle.png")

files.sort()

for filename in files:
    print("*<code>" + filename.replace(".png", "") + "</code>")