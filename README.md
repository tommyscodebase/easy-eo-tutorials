# Easy-EO Tutorials

Code, notebooks and data for the **Easy-EO** video series.

<p align="center">
  <a href="https://www.youtube.com/@tommys_codebase">
    <img src="https://img.shields.io/badge/YouTube-Watch%20the%20series-FF0000?logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
  <a href="https://pypi.org/project/easy-eo/"><img src="https://img.shields.io/pypi/v/easy-eo.svg" alt="PyPI"></a>
  <a href="https://easy-eo.readthedocs.io"><img src="https://readthedocs.org/projects/easy-eo/badge/?version=latest" alt="Docs"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT"></a>
</p>


**Library:** [Tommy-Burns/easy-eo](https://github.com/Tommy-Burns/easy-eo) ·
**Docs:** [easy-eo.readthedocs.io](https://easy-eo.readthedocs.io) ·
**Channel:** [@Tommy's Codebase](https://www.youtube.com/@tommys_codebase)

---

## Start here

If you have never touched a GeoTIFF, watch Episode 1 and run this:

```python
import eeo
from eeo.datasets import load_sample_dataset

sd = load_sample_dataset()  # downloads + caches a hosted Sentinel-2 subset

scene = eeo.load_raster(sd.sentinel2_cog_stacked)   # red, green, blue, nir
scene.ndvi(red="red", nir="nir").plot_raster(cmap="RdYlGn")
```

That is a real NDVI map of a real Sentinel-2 scene, in five lines, with no GDAL
setup and no downloads to manage by hand.

---

## Setup

Pick one package manager and stay with it. Mixing pip and conda in the same
environment can break geospatial stacks.
I recommend installing it into an environment created with conda `conda create -n eeo-env python=3.12` (easy-eo requires Python 3.10+) instead of using a regular Python environment `python -m venv .venv`.  
After creating the conda environment, proceed to install easy-eo

**conda (recommended for GDAL-based stacks):**

```bash
conda activate eeo-env
conda install -c conda-forge easy-eo jupyterlab

# easy-eo provides a stack extra, install it via:
conda install -c conda-forge pystac-client planetary-computer
# easy-eo provides an xarray extra, install it via:
conda install -c conda-forge easy-eo xarray rioxarray
```

**pip:**  
Using pip in a conda environment
```bash
conda activate eeo-env
pip install easy-eo jupyterlab

# easy-eo provides a stack extra, install it via:
pip install "easy-eo[stac]"
# easy-eo provides an xarray extra, install it via:
pip install "easy-eo[xarray]"

# or install both extras with
pip install "easy-eo[stac,xarray]"
```

easy-eo requires Python 3.10+. Verify installation with:

```python
import eeo; eeo.show_versions()
```

---

## Following along

- **Pause on the code cells.** Every cell in the notebook is the cell in the
  video, in the same order, so you can catch up without scrubbing.
- **Stuck?** Open an issue here with the episode number and the full traceback.
- **Bug in the library itself?** That belongs on
  [easy-eo/issues](https://github.com/Tommy-Burns/easy-eo/issues). I read both.
- **Want an episode on something?** Open a Discussion.

---

## About Easy-EO

Easy-EO is a lightweight, extensible Python library for raster Earth Observation:
chainable processing, band algebra, spectral indices and visualization, without
the GDAL boilerplate. It applies one written-down nodata and dtype contract to
every operation, ships type hints (`py.typed`), and is tested on Python 3.10–3.14
across Linux, macOS and Windows.

If the series is useful, ⭐ the
[library repo](https://github.com/Tommy-Burns/easy-eo).

---

## License

- Notebooks and code in this repo: MIT (see [LICENSE](LICENSE)).  
- Satellite imagery belongs to its providers:
  - Sentinel-2 data is © Copernicus / ESA, and
  - Copernicus DEM is © ESA / Airbus. 

Attribution notes are in each notebook.
