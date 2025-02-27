<img src="https://raw.githubusercontent.com/DHI/fmskill/main/images/logo/mike-fm-skill-rgb.svg" width="300">

# FMskill: Compare MIKE FM results with observations.
 ![Python version](https://img.shields.io/pypi/pyversions/fmskill.svg) 
![Python package](https://github.com/DHI/fmskill/actions/workflows/full_test.yml/badge.svg) [![PyPI version](https://badge.fury.io/py/fmskill.svg)](https://badge.fury.io/py/fmskill)

[FMskill](https://github.com/DHI/fmskill) is a python package for scoring [MIKE FM](https://www.mikepoweredbydhi.com/products/mike-21-3) models. 

Read more about the [vision and scope](https://dhi.github.io/fmskill/vision.html). Contribute with new ideas in the [discussion](https://github.com/DHI/fmskill/discussions), report an [issue](https://github.com/DHI/fmskill/issues) or browse the [API documentation](https://dhi.github.io/fmskill/api.html).


## Use cases

[FMskill](https://github.com/DHI/fmskill) would like to be your companion during the different phases of a MIKE FM modelling workflow.

* Model setup - exploratory phase   
* Model calibration
* Model validation and reporting - communicate your final results

## Installation

From [pypi](https://pypi.org/project/fmskill/):

`> pip install fmskill`

Or the development version:

`> pip install https://github.com/DHI/fmskill/archive/main.zip`


## Example notebooks

* [Quick_and_dirty_compare.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Quick_and_dirty_compare.ipynb)
* [SW_DutchCoast.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/SW_DutchCoast.ipynb)
* [Multi_model_comparison.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Multi_model_comparison.ipynb)
* [Multi_variable_comparison.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Multi_variable_comparison.ipynb)
* [Track_comparison.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Track_comparison.ipynb) (including global wave model example)
* [Spatial_skill.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Spatial_skill.ipynb) (satellite tracks, skill aggregated on spatial bins)
* [NetCDF_ModelResult.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/NetCDF_ModelResult.ipynb)
* [Combine_comparers.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Combine_comparers.ipynb)
* [DMI_observations.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/DMI_observations.ipynb) (download data from REST api)
* [Altimetry_data.ipynb](https://nbviewer.jupyter.org/github/DHI/fmskill/blob/main/notebooks/Altimetry_data.ipynb) (download data from altimetry api)

## Workflow

1. Define **ModelResults**
2. Define **Observations**
3. **Connect** Observations and ModelResults
4. **Extract** ModelResults at Observation positions
5. Do plotting, statistics, reporting using a **Comparer**

Read more about the workflow in the [getting started guide](https://dhi.github.io/fmskill/getting_started.html).


## Example of use

Start by defining model results and observations:

```python
>>> from fmskill.model import ModelResult
>>> from fmskill.observation import PointObservation, TrackObservation
>>> mr = ModelResult("HKZN_local_2017_DutchCoast.dfsu", name="HKZN_local", item=0)
>>> HKNA = PointObservation("HKNA_Hm0.dfs0", item=0, x=4.2420, y=52.6887, name="HKNA")
>>> EPL = PointObservation("eur_Hm0.dfs0", item=0, x=3.2760, y=51.9990, name="EPL")
>>> c2 = TrackObservation("Alti_c2_Dutch.dfs0", item=3, name="c2")
```

Then, connect observations and model results, and extract data at observation points:

```python
>>> from fmskill import Connector
>>> con = Connector([HKNA, EPL, c2], mr)
>>> comparer = con.extract()
```

With the comparer, all sorts of skill assessments and plots can be made:

```python
>>> comparer.skill().round(2)
               n  bias  rmse  urmse   mae    cc    si    r2
observation                                                
HKNA         385 -0.20  0.35   0.29  0.25  0.97  0.09  0.99
EPL           66 -0.08  0.22   0.20  0.18  0.97  0.07  0.99
c2           113 -0.00  0.35   0.35  0.29  0.97  0.12  0.99
```

### Overview of observation locations

```python
con.plot_observation_positions(figsize=(7,7))
```

![map](https://raw.githubusercontent.com/DHI/fmskill/main/images/map.png)



### Scatter plot

```python
comparer.scatter()
```

![scatter](https://raw.githubusercontent.com/DHI/fmskill/main/images/scatter.png)

### Timeseries plot

Timeseries plots can either be static and report-friendly ([matplotlib](https://matplotlib.org/)) or interactive with zoom functionality ([plotly](https://plotly.com/python/)).

```python
comparer["HKNA"].plot_timeseries(width=1000, backend="plotly")
```

![timeseries](https://raw.githubusercontent.com/DHI/fmskill/main/images/plotly_timeseries.png)


## Automated reporting

With a few lines of code, it will be possible to generate an automated report.

```python
from fmskill.report import Reporter

rep = Reporter(mr)
rep.to_markdown()
```

[Very basic first example report](https://github.com/DHI/fmskill/blob/main/notebooks/HKZN_local/HKZN_local.md)
