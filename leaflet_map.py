import folium 

def map_main():
    st.title("Simple Map with Leaflet")

    # Create a map object using Folium
    m = folium.Map(location=[latitude, longitude], zoom_start=13)

    # Add markers or other map elements using Folium
    folium.Marker([marker_latitude, marker_longitude], popup="Marker 1").add_to(m)

    # Display the map using Streamlit
    folium_static(m)

if __name__ == "__main__":
    main()