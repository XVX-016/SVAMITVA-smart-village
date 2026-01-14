import geopandas as gpd
import os

def export_for_web(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    # Load GeoJSON (currently in UTM or mixed)
    gdf = gpd.read_file(input_path)
    
    # Reproject to WGS84 (required for Leaflet)
    print(f"Reprojecting from {gdf.crs} to EPSG:4326...")
    gdf_web = gdf.to_crs(epsg=4326)
    
    # Optional: Filter or sort to ensure the best features are shown
    # Let's keep the best 100 as we did for stats, or keep all above a threshold
    gdf_web['area_m2'] = gdf_web.geometry.area # This is degrees now, so we compute area in UTM first if needed
    # But we already computed stats in m2 in compute_stats.py
    
    # For simplicity, we just save the full reprojected set or a calibrated subset
    # Let's use the threshold logic from compute_stats
    # (Re-calculating area in meters before reprojection to be safe)
    gdf_utm = gdf.to_crs(epsg=32614)
    gdf_utm['area_m2'] = gdf_utm.geometry.area
    gdf_filtered = gdf_utm[gdf_utm['area_m2'] > 0.01].copy() # Using a lower filter for the map to show more
    
    # Now reproject filtered to WGS84
    gdf_web_filtered = gdf_filtered.to_crs(epsg=4326)
    
    # Ensure output dir exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to GeoJSON
    gdf_web_filtered.to_file(output_path, driver='GeoJSON')
    print(f"Exported {len(gdf_web_filtered)} features to {output_path}")

if __name__ == "__main__":
    export_for_web('outputs/building_footprints.geojson', 'web_demo/data/building_footprints.geojson')
