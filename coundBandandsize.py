#program to count the number of bands in raster file and show theie stats
from osgeo import gdal
import sys
rasterPath=r'C:\Users\msi\Desktop\srtm_cgiar_nepal_boundary.img'

raster=gdal.Open(rasterPath)
if raster is None:
    sys.exit("cant read the Raster ffile make sure the path is correct")
print(raster.GetMetadata())

print("Number of Bands",raster.RasterCount)
print("Demesions  :",raster.RasterXSize,"x ",raster.RasterYSize)
for i in range(raster.RasterCount):
     i+=1
     band=raster.GetRasterBand(i)
     stats=band.GetStatistics(True,True)
     print ("[ STATS for band %d] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
i, stats[0], stats[1], stats[2], stats[3] ))
     
