import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

BASE = "https://github.com/Tommy-Burns/easy-eo/releases/download/sample-data-v1/"

with rasterio.open(BASE + "sentinel2_small_cog.tif") as src:
    aoi = gpd.read_file(BASE + "roi.gpkg").to_crs(src.crs)
    clipped, transform = mask(src, aoi.geometry.values, crop=True)
    bands = {name: i for i, name in enumerate(src.descriptions)}
    nodata = src.nodata
    profile = src.profile

red = clipped[bands["red"]].astype("float32")
nir = clipped[bands["nir"]].astype("float32")

valid = (red != nodata) & (nir != nodata)
total = nir + red
ndvi = np.where(valid & (total != 0), (nir - red) / np.where(total == 0, 1, total), 0.0)
ndvi = np.where(valid, ndvi, np.nan).astype("float32")

profile.update(
    count=1, dtype="float32", nodata=np.nan,
    height=ndvi.shape[0], width=ndvi.shape[1], transform=transform,
)
with rasterio.open("ndvi_rio.tif", "w", **profile) as dst:
    dst.write(ndvi, 1)
