# Judge Q&A Simulation: Drone-to-Panchayat

Be prepared for these common questions during your presentation.

---

### **Q1: Why did you tile the imagery instead of processing it all at once?**
**Answer:** "The original orthophoto is a high-resolution 7000x8000 pixel raster. Processing this in one shot would exceed the VRAM of most GPUs. Tiling into 512x512 patches allows our pipeline to remain memory-efficient and scalable to much larger survey areas, like entire districts."

### **Q2: Your model is pretrained on satellite data. How does it handle higher resolution drone imagery?**
**Answer:** "That’s a great observation. Satellite data is typically 30cm to 1m per pixel, while our drone data is 2cm per pixel. To handle this, we used a spatial calibration step and a noise filter. While a pretrained model provides a robust baseline, our pipeline is designed such that adding just a few hundred local labels would allow for rapid fine-tuning to specific regional architectures."

### **Q3: How do you handle building occlusions like trees or shadows?**
**Answer:** "Currently, we rely on the spectral signatures in the RGB bands. While heavy tree cover can be a challenge for RGB-only models, our pipeline is 'modality-ready'. In the next phase, we would integrate the DSM (Digital Surface Model) from the drone capture, using height discontinuities to 'see' buildings under canopy."

### **Q4: Is this system ready for real-world government use?**
**Answer:** "Yes. The output is a standard GeoJSON with verified UTM projections. This can be directly imported into QGIS, ArcGIS, or government land record portals. We’ve focused on a pure-Python stack precisely so it can be deployed as an automated backend service without requiring manual desktop GIS work."

### **Q5: How are you managing the performance of such high-resolution imagery in the web demo?**
**Answer:** "That’s a critical challenge for web-GIS. For the demo, we’ve implemented a 'downsampled proxy' technique. We generate a web-friendly PNG (2048px) that preserves the geospatial bounds for visualization, while the heavy AI inference still runs on the full-resolution (8000px+) GeoTIFF in the backend. This gives you the speed of the web with the precision of AI."

---

## **Final Tip: The "Pivot" Technique**
If you don't know the answer to a deep technical question, pivot to the impact:
*"That's a great technical nuance. While our current focus was on building the automated end-to-end extraction for Panchayats, our architecture is modular enough to integrate [X feature] in the next development cycle."*
