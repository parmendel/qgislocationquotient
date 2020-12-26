# qgislocationquotient
Location Quotient plugin for QGIS

Location Quotient (LQ) is a widely used index in Spatial Analysis. 
LQ compares the percentage of two variables in a study area with the percentage of the same variables in a wider area.

Location Quoetient formula: LQ = (xi/yi) / (Xi/Yi)
                            where xi, yi are the variables
                            Xi, Yi is the summary of xi,yi in the wider area

LQ Algorithm requires a vector layer (any geometry) and two fields as x, y variables. It calculates the LQ index and 
adds the index for each feature in the attribute table.
