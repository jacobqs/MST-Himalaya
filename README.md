# Assessing the Shyft Modelling Framework in Nepal: Impact of Snow Routines and Terrain Representation on Simulated Water Balance Components
[![DOI](https://zenodo.org/badge/472295880.svg)](https://zenodo.org/badge/latestdoi/472295880)


## Introduction:

The region encompassing the Himalayan and Tibetan Plateau is of immense significance as it provides water resources for millions of people residing in the surrounding areas (Bookhagen and Burbank 2010). The water from this region provides drinking water, supports agricultural activities, is used for generating hydro power, and catering to other agro-economic requirements (Ménégoz et al. 2013). The area holds tremendous potential for developing hydro power and thus making the transition towards a greener economy more feasible.

The Budhi Gandaki catchment, located in Nepal's Gorkha district, receives a high mean annual precipitation of 1495 mm and has an extremely diverse topography, with elevations varying from 479 to 8163 meters above sea level  (Devkota et al. 2017). Its unique characteristics make it an attractive location for hydro power development, with an installed capacity of 1200 megawatts (MW) and an average energy generation of 3383 gigawatt-hours (GWh). However, the hydro power potential is subject to the prevailing climatic conditions in precipitation, evaporation, temperature, and snow/ice within the catchment, as noted in (Edenhofer et al. 2011) Climate change can have serious implications to the hydro power production (Edenhofer et al. 2011). 
Changing rainfall pattern and increased temperatures will affect power generation. The retreat of glaciers, expansion of glacial lakes, and alterations in the seasonality and intensity of precipitation are some of the factors that will impact power generation in the future (Dandekhya et al. 2017). In addition, the region is also susceptible to Glacial Lake Outburst Floods (GLOFs), which can cause devastating floods downstream (Dandekhya et al. 2017).

The complex hydrology of the High Mountain Asia poses challenges to hydrological modelling due to highly variable distribution of hydro-meteorological variables, steep elevation gradients and pronounced seasonality by the Indian Monsoon, as well as differing moisture regimes between the Tibetan Plateau and the Indian Ocean region (Bhattarai et al. 2020; Fan et al. 2019).}. Additionally, climate change can likely alter the regional water balance components  (Koch et al. 2011). Accurate measurement of meteorological variables is challenging due to the region's heterogeneous topography (Pellicciotti et al. 2012). It is nearly impossible to make observations at all elevations, especially for snow. Insufficient data can lead to errors in discharge predictions, making satellite observations and reanalysis data sets vital for the decision-making processes. Furthermore, the input data and choice of models can have a considerable impact the accuracy of the outcome  (Kauffeldt et al. 2016). 
In the past, several hydrological models have been developed for various applications. Some of these models include SRM (Martinec et al. 1983), HEC-HMS (Halwatura and Najim 2013), J2000  (Nepal et al. 2014 and Shyft  (Burkhart et al. 2021). Unlike other many other models, Shyft offers the advantage of integrating various well-known hydrological routines (each defined for processes such as evapotranspiration, snow accumulation and melt) into multiple models. This allows for testing multiple different scientific hypotheses using only this framework. Furthermore, it is important that a model can accurately represent terrain features since the terrain in High Mountain Asia is complex. Most distributed models discretize the catchment and derive terrain features from Digital Elevation Models (DEMs) (Bhattarai, Silantyeva, et al. 2020). Shyft is able to use several different catchment discretization methods, such as regular grid and Triangular Irregular Networks (TINs). TIN-based models have a better accuracy in representing complex terrain than grids, while also being computationally efficient. Few studies have used TINs in Himalayan catchments, but  Bhattarai, Silantyeva, et al. 2020 have shown that TINs can improve simulation results compared with grids. Shyft is therefore considered a particularly valuable tool for its ability to evaluate different models, and to consider terrain heterogeneity and generate distributed output variables. Shyft also aims to become a FAIR framework for learning and research activities promoting open-science efforts (Wilkinson et al. 2016), which makes it ideal for scientific purposes. 

Bhattarai, B. C. (2020). Hydrologic model forcing over the Himalaya. 2267. Faculty of
Mathematics and Natural Sciences, University of Oslo. isbn: 1501-7710.

Bhattarai, B. C., J. F. Burkhart, F. Stordal, et al. (July 5, 2019). “Aerosol Optical Depth Over the Nepalese Cryosphere Derived From an Empirical Model.” In: Frontiers in Earth Science 7, p. 178. issn: 2296-6463. doi: 10.3389/feart.2019.00178. url: https://www.frontiersin.org/article/10.3389/feart.2019.00178/full (visited on 10/17/2022).

Bhattarai, B. C., J. F. Burkhart, L. M. Tallaksen, et al. (Apr. 1, 2020). “Evaluation
of global forcing datasets for hydropower inflow simulation in Nepal.” In: Hydrology Research 51.2, pp. 202–225. issn: 0029-1277, 2224-7955. doi: 10.2166/nh.2020.079. url: https://iwaponline.com/hr/article/51/2/202/72386/Evaluation-of-global- forcing-datasets-for (visited on 10/17/2022).

Bhattarai, B. C., O. Silantyeva, et al. (Aug. 20, 2020). “Impact of Catchment Discretization and Imputed Radiation on Model Response: A Case Study from Central Himalayan Catchment.” In: Water 12.9, p. 2339. issn: 2073-4441. doi: 10. 3390/w12092339. url: https://www.mdpi.com/2073-4441/12/9/2339 (visited on 09/29/2022).

Burkhart, J. F. et al. (Feb. 5, 2021). “Shyft v4.8: a framework for uncertainty assessment and distributed hydrologic modeling for operational hydrology.” In: Geoscientific Model Development 14.2, pp. 821–842. issn: 1991-9603. doi: 10.5194/gmd-14- 821-2021. url: https://gmd.copernicus.org/articles/14/821/2021/ (visited on
09/29/2022).

Dandekhya, S. et al. (2017). The Gandaki Basin- Maintaining Livelihoods in the Face of Landslides,Floods, and Drought; HI-AWARE Working Paper 9. Himalayan Adaptation, Water and Resilience (HI-AWARE).

Devkota, R. P. et al. (Jan. 2017). “Climate change and adaptation strategies in Budhi Gandaki River Basin, Nepal: a perception-based analysis.” In: Climatic Change 140.2, pp. 195–208. issn: 0165-0009, 1573-1480. doi: 10.1007/s10584-016-1836-5. url: http://link.springer.com/10.1007/s10584-016-1836-5 (visited on 10/03/2022).

Edenhofer, O. et al. (2011). Renewable energy sources and climate change mitigation: Special report of the intergovernmental panel on climate change. Cambridge University Press.

Fan, Y. et al. (Feb. 2019). “Hillslope Hydrology in Global Change Research and Earth System Modeling.” In: Water Resources Research 55.2, pp. 1737–1772. issn: 0043-1481397, 1944-7973. doi: 10.1029/2018WR023903. url: https://onlinelibrary.wiley.
com/doi/10.1029/2018WR023903 (visited on 04/23/2023).

Halwatura, D. and M.M.M. Najim (Aug. 2013). “Application of the HEC-HMS model for runoff simulation in a tropical catchment.” In: Environmental Modelling & Software 46, pp. 155–162. issn: 13648152. doi: 10.1016/j.envsoft.2013.03.006. url: https: //linkinghub.elsevier.com/retrieve/pii/S1364815213000698 (visited on 05/11/2023).

JPL, NASA (2013). NASA Shuttle Radar Topography Mission Global 1 arc second. doi: 10.5067/MEASURES/SRTM/SRTMGL1.003. url: https://lpdaac.usgs.gov/ products/srtmgl1v003/ (visited on 10/13/2022).

Kauffeldt, A. et al. (Jan. 2016). “Technical review of large-scale hydrological models for implementation in operational flood forecasting schemes on continental level.” In: Environmental Modelling & Software 75, pp. 68–76. issn: 13648152. doi: 10. 1016/j.envsoft.2015.09.009. url: https://linkinghub.elsevier.com/retrieve/pii/ S1364815215300529 (visited on 04/11/2023).

Ménégoz, M., H. Gallée, and H. W. Jacobi (Oct. 15, 2013). “Precipitation and snow cover in the Himalaya: from reanalysis to regional climate simulations.” In: Hydrology and Earth System Sciences 17.10, pp. 3921–3936. issn: 1607-7938. doi: 10.5194/hess-17-3921-2013. url: https://hess.copernicus.org/articles/17/3921/2013/ (visited on 10/13/2022).

Pellicciotti, F. et al. (Feb. 2012). “Challenges and Uncertainties in Hydrological Modeling of Remote Hindu Kush–Karakoram–Himalayan (HKH) Basins: Suggestions for Calibration Strategies.” In: Mountain Research and Development 32.1, pp. 39–50. issn: 0276-4741, 1994-7151. doi: 10.1659/MRD-JOURNAL-D-11-00092.1. url: http://www.bioone.org/doi/10.1659/MRD-JOURNAL-D-11-00092.1 (visited on 10/13/2022).

Nepal, S. et al. (Jan. 30, 2014). “Understanding the hydrological system dynamics of a glaciated alpine catchment in the Himalayan region using the J2000 hydrological model: Hydrological System Dynamics of Himalaya Rivers.” In: Hydrological Processes 28.3, pp. 1329–1344. issn: 08856087. doi: 10.1002/hyp.9627. url: https: //onlinelibrary.wiley.com/doi/10.1002/hyp.9627 (visited on 05/11/2023).

Wilkinson, M. D. et al. (Mar. 15, 2016). “The FAIR Guiding Principles for scientific data management and stewardship.” In: Scientific Data 3.1, p. 160018. issn: 2052-4463. doi: 10.1038/sdata.2016.18. url: https://www.nature.com/articles/sdata201618 (visited on 04/23/2023).



## Scientific questions:


The primary aim of this study to evaluate the Shyft modelling framework in its ability to simulate primary water balance components in the Budhi Gandaki catchment, with its complex terrain and limited availability of data. To achieve this goal the study will be divided into the several objectives.

The first objective will be to investigate spatial and temporal variation in the forcing data (temperature, precipitation, global radiation, relative humidity and wind speed). The recently added bias-adjusted ERA5 reanalysis data is chosen for this study because it has shown to have a lower mean absolute error and higher correlation with observed precipitation than the WDFEI reanalysis. The analysis of temporal variation is done to see if there are any trends or seasonality that might affect the hydrology of the High Mountain Asia and the Budhi Gandaki catchment. This is important because potential changes in the climate may affect the model performance. The spatial variation will be investigated through seasonal maps of the forcing variables and by statistical methods. The analysis of spatial variation may help explain if the forcing data is able to capture leeward and windward precipitation patterns that might affect the model performance. Furthermore, two different interpolation methods in Shyft (Bayesian Temperature Kriging and Inverse Distance Weighting) will be discussed.

The second objective is to evaluate the effect of different terrain representations and snow routines on model calibration and performance using observed river discharge as target. To achieve this, the catchment is discretized using two different discretization methods. A regular grid representation will be compared with four different Triangular Irregular Networks (TINs) of different resolutions. The two snow routines used include the Gamma Snow routine (simplified surface energy balance model for snow melt) and the recently introduced Snow Tiles routine. The Gamma Snow routine is a simplified surface energy balance model that has been tested in the region before with satisfactory results. The Snow Tiles routine is a temperature-index based model which has never been tested in the region. The Snow Tiles routine is chosen because it has considerably fewer parameters than the Gamma Snow routine, potentially making calibration faster and thus lower uncertainty stemming from equifinality. The model performance will be evaluated by comparing simulated and observed discharge using visualisation and evaluation criteria such as the Nash-Sutcliffe Efficiency (NSE), Kling-Gupta Efficiency (KGE) and Root Mean Square Error (RMSE).

The third objective is to evaluate the impact of the different terrain representations and snow routines on simulated snow-covered area, snow water equivalent, snow cover duration and glacier melt. Snow melt can be a significant contributor to runoff, and it is therefore important that the accuracy of modelled snow is assessed. Simulated snow-covered area (SCA) is compared with observed snow-covered area and snow-cover duration (SCD) derived using observed SCA by MODIS. This method provides an additional way of evaluating model performance. The evaluation criteria used for this comparison is the Critical Success Index (CSI).

## Methods:

Shyft — Statkraft’s Hydrological Forecasting Toolbox (Burkhart et al. 2021), is a modelling framework aimed for hydrological simulations in operational environments, but also for being a flexible and easy-to-use tool for testing scientific hypothesizes. Shyft-platform, being under development, has a goal towards being a FAIR framework for learning and research activities facilitating open-science shift (GO FAIR 2021).

For more information abou Shyft please see:

[Shyft source code](https://gitlab.com/shyft-os/shyft)

[Shyft v4.8: a framework for uncertainty assessment and distributed hydrologic modeling for operational hydrology](https://gmd.copernicus.org/articles/14/821/2021/)

## Data

The study use the WFDE5 global bias-adjusted ERA-5 as forcing data (Cucchi et al. 2020), and snow-covered area by MODIS (Hall, D. K. & G. A. Riggs, 2016) and observed river discharge data from the [Department of Hydrology and Meteorology in Nepal](https://www.dhm.gov.np) as evaluation. The FAIR principles will be a part of the of data handling (GO FAIR 2021). The data can be found at the [Zenodo repository](https://zenodo.org/deposit/7992374).

Cucchi, M., G. P. Weedon, A. Amici, N. Bellouin, S. Lange, H. Müller Schmied, H. Hersbach, and C. Buontempo (Sept. 8, 2020). “WFDE5: bias-adjusted ERA5 reanalysis data for impact studies.” In: Earth System Science Data 12.3, pp. 2097– 2120. issn: 1866-3516. doi: 10.5194/essd-12-2097-2020. url: https://essd.copernicus. org/articles/12/2097/2020/ (visited on 09/29/2022).

Hall, D. K. and G. A. Riggs. (2016). MODIS/Terra Snow Cover Daily L3 Global 500m SIN Grid, Version 6 [Data Set]. Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD10A1.006. Date Accessed 06-06-2023.


