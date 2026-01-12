# Drone-to-Panchayat: Automated Rural Property Mapping

> **Problem**: Manual property surveys for local Panchayats are slow, expensive, and error-prone.
> **Solution**: An automated GeoAI pipeline that converts raw drone imagery into GIS-ready building intelligence in minutes.

---

## The Edge
- **Zero Manual Digitization**: Replaces hours of manual tagging with a U-Net AI pipeline.
- **Geospatial-Native**: Preserves absolute precision (UTM Zone 14N) for immediate GIS integration.
- **Actionable Stats**: Automatically computes building counts and footprint areas (m²).

## Tech Stack
- **AI**: PyTorch, Segmentation Models (U-Net + ResNet34)
- **GIS Engine**: Rasterio, GeoPandas (Pure Python, no heavy software needed)
- **Data**: High-resolution (2cm/pixel) drone-captured orthophotos.

## Impact (Sample Panchayat Survey)
- **Input Area**: ~2.3 Hectares (7403 x 8428 pixels)
- **Validated Footprints**: 100 significant structures
- **Total Built-up Area**: 3,062.21 m²
- **Output Format**: Industry-standard GeoJSON

---

## Submission Contents
- `building_footprints.geojson`: Vectorized building layers.
- `building_mask.tif`: High-resolution probability mask.
- `src/`: Reusable Python automation scripts.
- **[Walkthrough](C:\Users\tanmm\.gemini\antigravity\brain\b01ce016-5ec0-4c94-a3b1-ad23499570f1\walkthrough.md)**: Full architecture + **Judge Script**.

---
*“Mapping the future, one footprint at a time.”*
