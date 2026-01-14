// Initialize map (Centered on survey area)
const bounds = [[30.170426958123574, -98.08991734411521], [30.17224765685004, -98.089476468]];
const map = L.map('map').fitBounds(bounds);

// Add Base Map Layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 22,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Add the Orthophoto Image Overlay (PNG)
const imageUrl = 'data/orthophoto_web.png';
const imageOverlay = L.imageOverlay(imageUrl, bounds, {
    opacity: 0.85,
    interactive: true,
    attribution: "Drone Survey Data"
}).addTo(map);

// Load Building Footprints
fetch('data/building_footprints.geojson')
    .then(response => response.json())
    .then(data => {
        const geojson = L.geoJSON(data, {
            style: function (feature) {
                return {
                    color: '#ef4444',
                    weight: 2,
                    opacity: 0.9,
                    fillColor: '#ef4444',
                    fillOpacity: 0.4,
                };
            },
            onEachFeature: function (feature, layer) {
                if (feature.properties && feature.properties.area_m2) {
                    layer.bindPopup(`<b>Infrastructure Feature</b><br>Detected Area: ${feature.properties.area_m2.toFixed(2)} m²`);
                }
            }
        }).addTo(map);
        console.log("Loaded building footprints.");
    })
    .catch(error => {
        console.error('Error loading GeoJSON:', error);
    });

// Add Legend
const legend = L.control({ position: 'bottomright' });
legend.onAdd = function (map) {
    const div = L.DomUtil.create('div', 'legend');
    div.innerHTML = '<i style="background: #ef4444; border: 2px solid #ef4444; width: 12px; height: 12px; display: inline-block; margin-right: 5px;"></i> Detected Building';
    return div;
};
legend.addTo(map);
