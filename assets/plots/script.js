document.addEventListener('DOMContentLoaded', function() {
    const yearSelect = document.getElementById('year');
    const categorySelect = document.getElementById('category');
    const mapDiv = document.getElementById('mapDiv');

    function updateMap() {
        const selectedYear = yearSelect.value;
        const selectedCategory = categorySelect.value;

        if (!selectedYear || !selectedCategory) {
            // Clear the map if no year or category is selected
            Plotly.purge(mapDiv);
            return;
        }

        // Filter data
        let filteredData = crimeData.filter(item => item.Year == selectedYear && item.Category == selectedCategory);

        // Prepare data for heatmap
        let latitudes = filteredData.map(item => item.Latitude);
        let longitudes = filteredData.map(item => item.Longitude);
        let counts = filteredData.map(item => item.Count);

        // Find max count for colorscale
        let maxCount = Math.max(...counts);

        // Create heatmap trace
        let trace = {
            type: 'densitymapbox',
            lat: latitudes,
            lon: longitudes,
            z: counts,
            radius: 10,
            colorscale: 'Viridis',
            zmax: maxCount,
            colorbar: {
                title: 'Crime Count'
            },
            hovertemplate: "Count: %{z}<extra></extra>"
        };

        let layout = {
            mapbox: {
                style: 'open-street-map',
                center: {
                    lat: 37.7749,
                    lon: -122.4194
                },
                zoom: 11
            },
            margin: {
                r: 0,
                t: 0,
                b: 0,
                l: 0
            }
        };

        Plotly.newPlot(mapDiv, [trace], layout);
    }

    yearSelect.addEventListener('change', updateMap);
    categorySelect.addEventListener('change', updateMap);
});
