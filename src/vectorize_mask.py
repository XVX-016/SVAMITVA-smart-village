import rasterio
from rasterio.features import shapes
import geopandas as gpd
from shapely.geometry import shape
import os

def vectorize(mask_path, output_path):
    if not os.path.exists(mask_path):
        print(f"Error: {mask_path} not found.")
        return

    with rasterio.open(mask_path) as src:
        image = src.read(1) # mask is band 1
        mask = (image > 0)
        
        # Generator for shapes
        results = (
            {'properties': {'raster_val': v}, 'geometry': s}
            for i, (s, v) in enumerate(
                shapes(image, mask=mask, transform=src.transform)
            )
        )
        
        # Convert to list of shapely geometries
        geoms = list(results)
        if not geoms:
            print("No polygons found in mask.")
            return

        # Create GeoDataFrame
        df = gpd.GeoDataFrame.from_features(geoms, crs=src.crs)
        
        # Optional: Simplify polygons slightly or filter by area if needed
        # df['geometry'] = df.geometry.simplify(0.1)
        
        # Save to GeoJSON
        df.to_file(output_path, driver='GeoJSON')
        print(f"Vectorized {len(df)} features to {output_path}")

if __name__ == "__main__":
    vectorize('building_mask.tif', 'building_footprints.geojson')
