import os
import re
import glob
import shutil

root = "/home/hadi/Documents/ai/action_recognition/dataset/UCF101"
vidoes_paths = os.listdir(root)
actions = []
for i, path in enumerate(vidoes_paths):
    try:
        match = re.findall(r'v_(.*)_g.*', path)[0]
    except IndexError as e:
        pass
    else:
        actions.append(match)

for i, act in enumerate(actions):
    new_folder = os.path.join(root, act)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

for i, act in enumerate(actions):
    act_vids = [v for v in vidoes_paths if act in v]
    for vid in act_vids:
        src_path = os.path.join(root, vid)
        tgt_path = os.path.join(root, act, vid)
        print(src_path, tgt_path)
        if os.path.exists(src_path):
            shutil.move(src_path, tgt_path)
