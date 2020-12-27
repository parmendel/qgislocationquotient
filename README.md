# qgislocationquotient
Location Quotient plugin for QGIS

Location Quotient (LQ) is a widely used index in Spatial Analysis\n.
LQ compares the percentage of two variables in a region with the percentage of the same variables in a larget geographic unit (e.g. the whole country). \n
For example, LQ can be used to compare the unemployment rate of each city (unemployment / population) with the average unemployment rate in the country.
Location Quoetient formula: LQ = (xi/yi) / (Xi/Yi) where xi, yi are the variables and Xi, Yi is the summary of xi,yi in the wider area \n
LQ Algorithm requires a vector layer (any geometry) and two fields as x, y variables. It calculates the LQ index and adds the index for each feature in the attribute table.

For further explanation in LQ, you can check:
https://www.geoib.com/location-quotients.html
