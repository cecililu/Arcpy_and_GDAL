from osgeo import gdal

driver = gdal.GetDriverByName('GTiff')
file = gdal.Open('raster.img')
band = file.GetRasterBand(1)
print(band)
lista = band.ReadAsArray()


for j in  range(file.RasterXSize):
    for i in  range(file.RasterYSize):
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

# create new file
file2 = driver.Create( 'raster2.tif', file.RasterXSize , file.RasterYSize , 1)
file2.GetRasterBand(1).WriteArray(lista)

# spatial ref system
proj = file.GetProjection()
georef = file.GetGeoTransform()
file2.SetProjection(proj)
file2.SetGeoTransform(georef)
file2.FlushCache()