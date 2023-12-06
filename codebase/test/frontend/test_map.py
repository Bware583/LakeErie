import unittest
import folium
import sys

sys.path.append("../../src/frontend")
import leaflet_map

class TestMapMainFunction(unittest.TestCase):

    def test_valid_selected_buoy(self):
        # Test with a valid selected buoy
        selected_buoy = "Buoy 3"
        result = leaflet_map.map_main(selected_buoy)
        self.assertIsInstance(result, folium.Map)

    def test_invalid_selected_buoy(self):
        # Test with an invalid selected buoy
        selected_buoy = "Invalid Buoy"
        with self.assertRaises(ValueError) as context:
            leaflet_map.map_main(selected_buoy)
        self.assertEqual(str(context.exception), "Invalid selected buoy 'Invalid Buoy'. Please select a valid buoy from the list.")

    def test_invalid_coordinates(self):
        # Test with invalid coordinates (non-numeric)
        buoy_locations = [
            {"name": "Invalid Buoy", "latitude": "invalid", "longitude": "invalid"}
        ]
        with self.assertRaises(ValueError) as context:
            leaflet_map.map_main("Buoy 3")
        self.assertEqual(str(context.exception), "Invalid coordinates for buoy 'Invalid Buoy'. Latitude and longitude must be numeric.")

    def test_valid_coordinates(self):
        # Test with valid coordinates (numeric)
        selected_buoy = "Buoy 3"
        result = leaflet_map.map_main(selected_buoy)
        self.assertIsInstance(result, folium.Map)

if __name__ == '__main__':
    unittest.main()
