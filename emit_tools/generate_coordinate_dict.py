from typing import Dict
import xarray as xr

from .get_pixel_center_coords import get_pixel_center_coords

def generate_coordinate_dict(swath_ds: xr.Dataset) -> Dict:
    # Calculate Lat and Lon Vectors
    lon, lat = get_pixel_center_coords(swath_ds)  # Reorder this function to make sense in case of multiple variables
    
    # Create Coordinate Dictionary
    coords = {
        "latitude": (["latitude"], lat),
        "longitude": (["longitude"], lon),
        **swath_ds.coords,
    }  # unpack to add appropriate coordinates

    return coords
