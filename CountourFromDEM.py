from osgeo import gdal
driver = gdal.GetDriverByName('GTiff')
raster = gdal.Open(r'C:\Users\msi\Desktop\srtm_cgiar_nepal_boundary.img')
band = raster.GetRasterBand(1)

elevArray = band.ReadAsArray()
