import rasterio
from rasterio.windows import Window
import os

src_path = "data/processed/orthophoto_rgb.tif"
out_dir = "tiles"
tile_size = 512

os.makedirs(out_dir, exist_ok=True)

with rasterio.open(src_path) as src:
    meta = src.meta.copy()
    width, height = src.width, src.height

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            window = Window(x, y, tile_size, tile_size)
            transform = src.window_transform(window)
            tile = src.read(window=window)

            if tile.shape[1] < tile_size or tile.shape[2] < tile_size:
                continue  # skip partial tiles

            meta.update({
                "height": tile_size,
                "width": tile_size,
                "transform": transform
            })

            out_path = f"{out_dir}/tile_{x}_{y}.tif"
            with rasterio.open(out_path, "w", **meta) as dst:
                dst.write(tile)

print("Tiling complete.")
