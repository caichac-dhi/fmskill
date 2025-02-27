.. _getting_started:

Getting started
###############

This page describes the typical FMskill workflow for comparing 
model results and observations. If you just need a simple one-to-one 
time series comparison, see the `simple time series comparison <simple_compare.html>`_.

Workflow
********

The typical FMskill workflow consists of these five steps:

#. Define **ModelResults**
#. Define **Observations**
#. **Connect** observations and ModelResults
#. **Extract** ModelResults at observation positions
#. Do analysis, plotting, etc with a **Comparer**


1. Define ModelResults
======================

The result of a MIKE 21/3 simulation is stored in one or more dfs files. 
The most common formats are .dfsu for distributed data and .dfs0 for 
time series point data. A FMskill `ModelResult <api.html#fmskill.model.ModelResult>`_ is defined by the 
result file path and a name:

.. code-block:: python

   from fmskill import ModelResult
   mr = ModelResult("HKZN_local_2017.dfsu", name="HKZN_local")

Currently, ModelResult supports .dfs0 and .dfsu files and pandas DataFrame.  
Only the file header is read when the ModelResult object is created. 
The data will be read later. 

The ModelResult can be constructed without specifying a specific item as shown here. 
But the the item must be specified later (e.g. when connecting to an observation) 
by mr[0] or similar.



2. Define Observations
======================

The next step is to define the measurements to be used for the skill assessment. 
Two types of observation are available: 

* `PointObservation <api.html#fmskill.observation.PointObservation>`_
* `TrackObservation <api.html#fmskill.observation.TrackObservation>`_

Let's assume that we have one PointObservation and one TrackObservation: 

.. code-block:: python

   from fmskill import PointObservation, TrackObservation
   HKNA = PointObservation("HKNA_Hm0.dfs0", item=0, x=4.2420, y=52.6887, name="HKNA")
   c2 = TrackObservation("Alti_c2_Dutch.dfs0", item=3, name="c2")

In this case both observations are provided as .dfs0 files but pandas 
dataframes are also supported in case data are stored in another file format. 

Both PointObservation and TrackObservation need the path of the data file, 
the item number (or item name) and a name. A PointObservation further needs to be initialized with it's x-, y-position. 




3. Connect observations and ModelResults
========================================

The observations are connected with a model result using the 
`Connector <api.html#fmskill.connection.Connector>`_ like this:


.. code-block:: python

   from fmskill import Connector
   con = Connector([HKNA, c2], mr[0])

Note
----
Only ModelResults with a single item can be added to the Connector.
From a multi-item ModelResult 'mr' an item must selected e.g. with
'mr[0]' before adding.



4. Extract ModelResults at observation positions
================================================

Once the observations and the model results have been connected, 
its very simple to do the extraction which interpolates the model results 
in space and time to the observation points using the `extract() <api.html#fmskill.connection.Connector.extract>`_ method: 

.. code-block:: python

   cc = con.extract()

The extract method returns a `ComparerCollection <api.html#fmskill.comparison.ComparerCollection>`_ for further analysis and plotting. 


5. Do analysis, plotting, etc with a Comparer
=============================================

The object returned by the ``extract()`` method is a *comparer*. 
It holds the matched observation and model data and has methods 
for plotting and skill assessment. 

The primary comparer methods are:

* `skill() <api.html#fmskill.comparison.ComparerCollection.skill>`_ which returns a pandas dataframe with the skill scores
* `scatter() <api.html#fmskill.comparison.ComparerCollection.scatter>`_ which shows a scatter density plot of the data


Filtering
---------

Both methods allow filtering of the data in several ways:

* on ``observation`` by specifying name or id of one or more observations
* on ``model`` (if more than one is compared) by giving name or id 
* temporal using the ``start`` and ``end`` arguments
* spatial using the ``area`` argument given as a bounding box or a polygon