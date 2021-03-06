# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LocationQuotient
                                 A QGIS plugin
 LocationQuotient
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-12-21
        copyright            : (C) 2020 by Parmenion Delialis
        email                : parmeniondelialis@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Parmenion Delialis'
__date__ = '2020-12-21'
__copyright__ = '(C) 2020 by Parmenion Delialis'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LocationQuotient class from file LocationQuotient.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LocationQuotient import LocationQuotientPlugin
    return LocationQuotientPlugin()
