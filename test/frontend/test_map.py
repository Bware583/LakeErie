import unittest
from leaflet_map import map_main, map_main_with_custom_buoys

class TestMapMainFunction(unittest.TestCase):

    def test_valid_buoy(self):
        # Test with a valid buoy
        selected_buoy = "Buoy 3"
        # This test should not raise any exceptions
        map_html = map_main(selected_buoy)
        self.assertIsInstance(map_html, str)

    def test_invalid_buoy(self):
        # Test with an invalid buoy
        selected_buoy = "Invalid Buoy"
        # Expecting a ValueError to be raised since the buoy is not in the predefined list
        with self.assertRaises(ValueError):
            map_main(selected_buoy)

    def test_non_numeric_coordinates(self):
        # Test with non-numeric coordinates for a buoy
        buoy_locations = [
            {"name": "Invalid Buoy", "latitude": "invalid", "longitude": 2.3522},
        ]
        # Expecting a ValueError to be raised since latitude is not numeric
        with self.assertRaises(ValueError):
            map_main_with_custom_buoys("Invalid Buoy", buoy_locations)

    def test_invalid_coordinates_type(self):
        # Test with coordinates of invalid type
        buoy_locations = [
            {"name": "Invalid Buoy", "latitude": "invalid", "longitude": 2.3522},
        ]
        # Expecting a ValueError to be raised since latitude is not numeric
        with self.assertRaises(ValueError):
            map_main_with_custom_buoys("Invalid Buoy", buoy_locations)