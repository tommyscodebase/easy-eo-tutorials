import eeo
from eeo.datasets import load_sample_dataset

sd = load_sample_dataset()

(
    eeo.load_raster(sd.sentinel2_cog_stacked)
    .clip_raster_with_vector(sd.boundary)
    .ndvi(red="red", nir="nir")
    .save_raster("ndvi_eeo.tif")
)
