import rasterio
from rasterio.enums import Resampling
from PIL import Image
import numpy as np
import os

def generate_web_png(input_path, output_path, max_dim=2048):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with rasterio.open(input_path) as src:
        # Calculate scaling factor
        scale = max_dim / max(src.width, src.height)
        new_width = int(src.width * scale)
        new_height = int(src.height * scale)
        
        print(f"Downsampling to {new_width}x{new_height}...")
        
        # Read and resample
        # Assuming RGB (first 3 bands)
        data = src.read(
            [1, 2, 3],
            out_shape=(3, new_height, new_width),
            resampling=Resampling.bilinear
        )
        
        # Convert to HWC format (Height, Width, Channel)
        img_np = np.transpose(data, (1, 2, 0))
        
        # Save as PNG
        img = Image.fromarray(img_np.astype('uint8'), 'RGB')
        img.save(output_path)
        
        print(f"Saved web-friendly PNG to: {output_path}")
        
        # Also return the bounds for Leaflet ImageOverlay
        bounds = [[src.bounds.bottom, src.bounds.left], [src.bounds.top, src.bounds.right]]
        # Convert to 4326 if needed, but for ImageOverlay we usually need the same CRS as the map or 4326
        # Let's get the bounds in 4326
        from pyproj import Transformer
        transformer = Transformer.from_crs(src.crs, "EPSG:4326", always_xy=True)
        bl = transformer.transform(src.bounds.left, src.bounds.bottom)
        tr = transformer.transform(src.bounds.right, src.bounds.top)
        
        print(f"Leaflet Bounds (EPSG:4326): [[{bl[1]}, {bl[0]}], [{tr[1]}, {tr[0]}]]")

if __name__ == "__main__":
    # Ensure dir exists
    os.makedirs('web_demo/data', exist_ok=True)
    generate_web_png('data/processed/orthophoto_rgb.tif', 'web_demo/data/orthophoto_web.png')
