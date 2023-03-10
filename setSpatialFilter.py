from osgeo import gdal,ogr
import sys,os
from osgeo import osr
try:
    
    #opening the shapefile
    shapefile = r'C:\Users\msi\Desktop\Arcpy and Gdal\Lalitpurshp.shp'
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shapefile, 0)
    
    if dataSource is None:
        print ('Could not open ')
    else:
        print ('Opened ------------------>' ,shapefile)
        layer = dataSource.GetLayer()
        # if you want to filter BY COLUMN uncomment line beloe 
        # layer.SetAttributeFilter("TYPE = 'Gaunpalika'")
    
        featureCount = layer.GetFeatureCount()
        print ("Number of Local level   in Lalitpur"+ os.path.basename(shapefile),":  ",featureCount)
        print("They are listed below") 
        i = 1
        
        for feature in layer:
             print (i, feature.GetField("LOCAL"),"::",feature.GetField("TYPE"),)
             geom = feature.GetGeometryRef()
             
             #for finding centriod uncomment the line below
             #  print (feature.GetField("LOCAL"), "has its centroid in-->", geom.Centroid().ExportToWkt())
        # filter by point    #  
        
        kt = "POINT (85.3043 27.4977 )"
        ply=ogr.CreateGeometryFromWkt(kt)
        layer.SetSpatialFilter(ply)
        for feature in layer: 
             print ('Point lies in this Local level',feature.GetField("LOCAL"),',',feature.GetField("TYPE"))
             
except:
    sys.exit(1)
