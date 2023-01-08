# Forecasting discharge for hydropower production in Central Himalaya, Nepal
[![DOI](https://zenodo.org/badge/472295880.svg)](https://zenodo.org/badge/latestdoi/472295880)


## Introduction:

The water supply from the Himalayan and Tibetan Plateau is of great importance for millions of people (Bookhagen & Burbank 2010). The water from this region provides drinking water, supports agricultural demands, is used for hydropower generation and other agro-economic activities (Ménégoz et al. 2013). The countries in the High Mountain Asia (HMA) region have a huge potential for developing hydropower making the shift towards a greener economy more feasible.

The Bundhi-Gandaki catchment is located in the Gorkha district of Nepal. The catch- ment has a high mean annual precipitation of 1495 mm and extremely high spatial vari- ation in elevation (Devkota et al. 2017). For example, the lowest point is at 479 meters above sea level (m.a.s.l.) at Arughat hydrological station and the highest at Manaslu mountain 8163 m.a.s.l. The combination of high precipitation rate and steep gradients in elevation makes the region of superior interest for hydropower. The installed capacity is 1200 megawatt (MW) with an average energy generation of 3383 gigawatt-hours (GWh).

However, the hydropower potential is dependent on the climatic conditions in precipi- tation, evaporation, temperature and snow/ice in the catchment (Edenhofer et al. 2011). Climate change has serious implications fro hydropower production (Dandekhya et al. 2017). Changing rainfall pattern and increased temperatures will affect power genera- tion. The retreat of glaciers, expansion of glacial lakes and changes in the seasonality and intensity of rainfall is identifies as factors that will affect the power generation in the future (Dandekhya et al. 2017). The region is also threatened by Glacial Lake Out- burst Floods (GLOFs), that can cause devastating floods downstream (Dandekhya et al. 2017). In addition, the extremely heterogeneous topography of the catchment makes it challenging to get accurate measurements of meteorological variables (Pellicciotti et al. 2012). The scarcity of data makes the discharge predictions, which lies the foundation for hydropower, prone to errors. It is impossible to make observations at all high levels, especially for snow over and depth. For this reason, satellite observations and reanalysis data sets important for decision-making processes. Furthermore, different precipitation patterns on the leeward and windward sides of the catchment needs to taken into account in simulations.

Hydrological modelling in the region is challenging due to the steep gradients in eleva- tion, the highly heterogeneous distribuiton of hydrometeorological variables the marked seasonality driven by the Indian Monsoon and contrasting moisture regimes between the Tibetan Plateau and regions near the Indian Ocean (Bhattarai et al. 2020). Climate change will also likely lead to changes in the regional water balance components (Bhat- tarai et al. 2020). The quality of the discharge simulations for the region remains a challenge (Rochester 2010, Engeland et al. 2016, Kauffeldt et al. 2016), because the input data and choice of model will greatly affect the outcome (Kauffeldt et al. 2016).


## Scientific questions:


The main objective of this study is to evaluate the Shyft modelling framework in its ability to simulate main water balance components, especially discharge, in the specific conditions of the Budhi-Gandaki catchment with scarce data and extreme topography.

* Is the model able to capture precipitation variations on the leeward and windward sides of the catchment, and predict discharge adequately?
* How sensitive the model is to the forcings, spatial representation (grid or triangular- irregular networks) and scales?
* Can we calibrate the model using remote sensing data?
* How will changes in snow cover fraction and glacier melt affect the discharge in the
future?

## Methods:

Shyft — Statkraft’s Hydrological Forecasting Toolbox (Burkhart et al. 2021), is a mod- elling framework aimed for hydrological simulations in operational environments, but also for being a flexible and easy-to-use tool for testing scientific hypothesizes. Shyft-platform, being under development, has a goal towards being a FAIR framework for learning and research activities facilitating open-science shift (GO FAIR 2021).

For more information abou Shyft please see:

[Shyft source code](https://gitlab.com/shyft-os/shyft)
[Shyft v4.8: a framework for uncertainty assessment and distributed hydrologic modeling for operational hydrology](https://gmd.copernicus.org/articles/14/821/2021/)

## Data

The project will require work with several re-analysis datasets (WFDE5 global bias- adjusted ERA-5 (Cucchi et al. 2020), Hi-Aware regional dataset (ICIMOD 2021) and downscaling procedure (TopoScale/TopoClim), planning and executing modelling experi- ments, analyzing results. The FAIR principles will be a part of the of data handling (GO FAIR 2021).



## References:

Bhattarai, B. C., Burkhart, J. F., Tallaksen, L. M., Xu, C.-Y. & Matt, F. N. (2020), ‘Evaluation of global forcing datasets for hydropower inflow simulation in nepal’, Hydrology Research 51(2), 202–225.

Burkhart, J. F., Matt, F. N., Helset, S., Sultan Abdella, Y., Skavhaug, O. & Silantyeva, O. (2021), ‘Shyft v4. 8: a framework for uncertainty assessment and distributed hydrologic modeling for operational hydrology’, Geoscientific Model Development 14(2), 821–842.

Cucchi, M., Weedon, G. P., Amici, A., Bellouin, N., Lange, S., Muller Schmied, H., Hersbach, H. & Buontempo, C. (2020), ‘Wfde5: bias-adjusted era5 reanalysis data for impact studies’, Earth System Science Data 12(3), 2097–2120.

Devkota, R. P., Pandey, V. P., Bhattarai, U., Shrestha, H., Adhikari, S. & Dulal, K. N. (2017), ‘Climate change and adaptation strategies in budhi gandaki river basin, nepal: a perception-based analysis’, Climatic Change 140(2), 195–208.


Edenhofer, O., Pichs-Madruga, R., Sokona, Y., Seyboth, K., Kadner, S., Zwickel, T., Eickemeier, P., Hansen, G., Schl ̈omer, S., von Stechow, C. et al. (2011), Renewable energy sources and climate change mitigation: Special report of the intergovernmental panel on climate change, Cambridge University Press.

Engeland, K., Steinsland, I., Johansen, S. S., Petersen-Øverleir, A. & Kolberg, S. (2016), ‘Effects of uncertainties in hydrological modelling. a case study of a mountainous catch- ment in southern norway’, Journal of Hydrology 536, 147–160.

GO FAIR (2021), ‘Fair principles’. Downloaded 2021-11-18.
URL: https://www.go-fair.org/fair-principles/ 

ICIMOD (2021), ‘Hi-aware’. Downloaded 2021-11-18.
URL: https://www.icimod.org/initiative/hi-aware

Kauffeldt, A., Wetterhall, F., Pappenberger, F., Salamon, P. & Thielen, J. (2016), ‘Tech- nical review of large-scale hydrological models for implementation in operational flood forecasting schemes on continental level’, Environmental Modelling & Software 75, 68– 76.

Ménégoz, M., Gallée, H. & Jacobi, H. (2013), ‘Precipitation and snow cover in the hi- malaya: from reanalysis to regional climate simulations’, Hydrology and Earth System Sciences 17(10), 3921–3936.

Pellicciotti, F., Buergi, C., Immerzeel, W. W., Konz, M. & Shrestha, A. B. (2012), ‘Chal- lenges and uncertainties in hydrological modeling of remote hindu kush–karakoram– himalayan (hkh) basins: suggestions for calibration strategies’, Mountain Research and Development 32(1), 39–50.


Rochester, R. E. L. (2010), Uncertainty in hydrological modelling: a case study in the Tern catchment, Shropshire, UK, PhD thesis, UCL (University College London).


## Contact

This repository is made by Jacob Qvam Skavang. Reach out to jacobqs@uio.no. 

