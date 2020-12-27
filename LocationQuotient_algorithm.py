"""
***************************************************************************
    LocationQuotient.py
    ---------------------
    Author                      : Parmenion Delialis
    Date                         : December 2020
    Contact                     : parmeniondelialis@gmail.com
***************************************************************************
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterField
from qgis.core import QgsProcessingParameterFeatureSink
from qgis.core import QgsProcessingParameterString
from qgis.core import QgsField
from PyQt5.QtCore import QVariant
from qgis.core import QgsMessageLog
from qgis.core import Qgis
import processing

class LocationQuotientAlgorithm(QgsProcessingAlgorithm):
    LAYER = 'LAYER'
    VARIABLEX = 'VARIABLEX'
    VARIABLEY = 'VARIABLEY'
    LQFIELD = 'LQFIELD'
    LQLAYER = 'LQLAYER'
    
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.LAYER, 'Layer', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterField(self.VARIABLEX, 'Variable X', type=QgsProcessingParameterField.Numeric, parentLayerParameterName=self.LAYER))
        self.addParameter(QgsProcessingParameterField(self.VARIABLEY, 'Variable Y', type=QgsProcessingParameterField.Numeric, parentLayerParameterName=self.LAYER))
        self.addParameter(QgsProcessingParameterString(self.LQFIELD, 'Name for LQ Field ', defaultValue = 'LQ'))
        self.addParameter(QgsProcessingParameterFeatureSink(self.LQLAYER, 'Output', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        results = {}
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
    
        # Convert parameters
        layer = self.parameterAsVectorLayer(parameters, self.LAYER, context)
        variableX = self.parameterAsString(parameters, self.VARIABLEX, context)
        variableY = self.parameterAsString(parameters, self.VARIABLEY, context)
        lqField = self.parameterAsString(parameters, self.LQFIELD, context)

        # Add ID
        try:
            layer = processing.run("native:fieldcalculator", {'INPUT': layer, 'FIELD_NAME': 'LQ_FID','FIELD_TYPE': 1, 'FIELD_LENGTH': 10, 'FIELD_PRECISION': 0, 'FORMULA': '$id+1', 'OUTPUT': 'memory:'})['OUTPUT']
        except:
            layer = processing.run("qgis:fieldcalculator", {'INPUT': layer, 'FIELD_NAME': 'LQ_FID','FIELD_TYPE': 1, 'FIELD_LENGTH': 10, 'FIELD_PRECISION': 0, 'FORMULA': '$id+1', 'OUTPUT': 'memory:'})['OUTPUT']

        # Creating new field for LQ
        flds = layer.fields()
        pr = layer.dataProvider()
        
        # Checking if LQField exists
        if lqField not in flds.names():
            pr.addAttributes([QgsField(lqField, QVariant.Double, len=10, prec=5)])
            layer.updateFields()
            flds = layer.fields()

        # Getting field index from name
        idx1 = flds.indexOf(variableX)
        idx2 = flds.indexOf(variableY)
        LQFieldIdx = flds.indexOf(lqField)
        # Calculating bottom part of fraction (Xi/Yi)
        X = 0   #Sum of xi
        Y = 0   #Sum of yi
        for ftr in layer.getFeatures():
            X += ftr[idx1]
            Y += ftr[idx2]
        XoverY = X/Y
        
        # Calculating LQ
        for ftr in layer.getFeatures():
            xovery = ftr[idx1] / ftr[idx2]
            LQ = xovery / XoverY
            toAdd = {LQFieldIdx:LQ}
            pr.changeAttributeValues({ftr['LQ_FID']:toAdd})
        layer.updateFields()
        layerOut = processing.run("qgis:deletecolumn", {'INPUT':layer,'COLUMN':['LQ_FID'],'OUTPUT':parameters['LQLAYER']},context=context, feedback=feedback, is_child_algorithm=True )['OUTPUT']
        
        return results

    def name(self):
        return 'locationquotient'

    def displayName(self):
        return 'Location Quotient'

    def group(self):
        return 'Spatial Analysis'

    def groupId(self):
        return 'spatialanalysis'
        
    def shortHelpString(self):
        return ("Location Quotient")
    

    def createInstance(self):
        return LocationQuotientAlgorithm()
