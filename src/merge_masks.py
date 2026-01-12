import os
import rasterio
from rasterio.merge import merge
import glob

def merge_masks(input_dir, output_path):
    files = glob.glob(os.path.join(input_dir, "*.tif"))
    if not files:
        print("No files found to merge.")
        return

    src_files_to_mosaic = []
    for f in files:
        src = rasterio.open(f)
        src_files_to_mosaic.append(src)

    # Use rasterio.merge to handle tiling and geotransform correctly
    mosaic, out_trans = merge(src_files_to_mosaic)

    out_meta = src_files_to_mosaic[0].meta.copy()
    out_meta.update({
        "driver": "GTiff",
        "height": mosaic.shape[1],
        "width": mosaic.shape[2],
        "transform": out_trans,
        "count": 1,
        "compress": "deflate",
        "dtype": "uint8"
    })

    with rasterio.open(output_path, "w", **out_meta) as dest:
        dest.write(mosaic)

    # Clean up
    for src in src_files_to_mosaic:
        src.close()

    print(f"Saved merged mask to: {output_path}")

if __name__ == "__main__":
    merge_masks('outputs', 'building_mask.tif')
