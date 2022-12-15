from osgeo import gdal,ogr
import sys,os

try:
    shapefile = r'C:\Users\msi\Desktop\Arcpy and Gdal\Lalitpurshp.shp'
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shapefile, 0)
    # layer = dataSource.GetLayer()
    
    if dataSource is None:
        print ('Could not open ')
    
    else:
        print ('Opened ' ,shapefile)
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()
        print ("Number of features in"+ os.path.basename(shapefile),":  ",featureCount)

    
except:
    sys.exit(1)
