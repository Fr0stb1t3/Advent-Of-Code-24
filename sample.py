import time
from tqdm import tqdm

with tqdm(total=3, desc='level_1', position=0, leave=False) as pbar:
    for i in tqdm(range(3)):
        for j in tqdm(range(5), desc='level_2', position=0, leave=True):
            time.sleep(0.1)
        pbar.update()