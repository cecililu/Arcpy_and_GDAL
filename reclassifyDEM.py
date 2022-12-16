from osgeo import gdal

driver = gdal.GetDriverByName('GTiff')
raster = gdal.Open('raster.img')
band = raster.GetRasterBand(1)
print(band)
lista = band.ReadAsArray()


for j in  range(raster.RasterXSize):
    for i in  range(raster.RasterYSize):
        if lista[i,j] < 200:
            lista[i,j] = 1
        elif 200 < lista[i,j] < 400:
            lista[i,j] = 2
        elif 400 < lista[i,j] < 600:
            lista[i,j] = 3
        elif 600 < lista[i,j] < 800:
            lista[i,j] = 4
        else:
            lista[i,j] = 5

# create new raster
raster2 = driver.Create( 'raster2.tif', raster.RasterXSize , raster.RasterYSize , 1)
raster2.GetRasterBand(1).WriteArray(lista)

# spatial ref system
proj = raster.GetProjection()
georef = raster.GetGeoTransform()
raster2.SetProjection(proj)
raster2.SetGeoTransform(georef)
raster2.FlushCache()