import numpy as np 

def años():
    años = np.array([
        a2008 , a2009 , a2010 , a2011 , a2012 , a2013 , a2014 , a2015 , a2016 , a2017
        ])
    return años




utilidad2008 = 27834
utilidad2009 = 23789
utilidad2010 = 30189
utilidad2011 = 30967
utilidad2012 = 32501
utilidad2013 = 32701
utilidad2014 = 32701
utilidad2015 = 17155
utilidad2016 = 4614
utilidad2017 = 834

a2008 = utilidad2008
a2009 = utilidad2009
a2010 = utilidad2010
a2011 = utilidad2011
a2012 = utilidad2012
a2013 = utilidad2013
a2014 = utilidad2014
a2015 = utilidad2015
a2016 = utilidad2016
a2017 = utilidad2017


utilidadtotal = (utilidad2008 , utilidad2009 , utilidad2010 , utilidad2011 , utilidad2012 ,
utilidad2013 , utilidad2014 , utilidad2015 , utilidad2016 , utilidad2017 )

print(años, utilidadtotal)


sum = (utilidad2008 + utilidad2009 + utilidad2010 + utilidad2011 +utilidad2012 + utilidad2013 + utilidad2014 + utilidad2015 + utilidad2016 + utilidad2017)
avg = sum/10

print ("El promedio o media de la utilidad con el paso de los años es: ", avg)


DifMayorYMenorUtilidad =(a2013 - a2017)

print ("La diferencia del año con mayor utilidad y el de menor utilidad es: ", DifMayorYMenorUtilidad)


medianap1 = (a2008 + a2010)
medianap2 = medianap1 /2

print ("La mediana de la utilidad con el paso de los años es: ", medianap2)

aporte2008 = a2008
print("El aporte acumulado en el año 2008 es", aporte2008)

aporte2009 = aporte2008 + a2009
print("El aporte acumulado en el año 2009 es", aporte2009)

aporte2010 = aporte2009 + a2010
print("El aporte acumulado en el año 2010 es", aporte2010)

aporte2011 = aporte2010 + a2011
print("El aporte acumulado en el año 2011 es", aporte2011)

aporte2012 = aporte2011 + a2012
print("El aporte acumulado en el año 2012 es", aporte2012)

aporte2013 = aporte2012 + a2013
print("El aporte acumulado en el año 2013 es", aporte2013)

aporte2014 = aporte2013 + a2014
print("El aporte acumulado en el año 2014 es", aporte2014)

aporte2015 = aporte2014 + a2015
print("El aporte acumulado en el año 2015 es", aporte2015)

aporte2016 = aporte2015 + a2016
print("El aporte acumulado en el año 2016 es", aporte2016)

aporte2017 = aporte2016 + a2017
print("El aporte acumulado en el año 2017 es", aporte2017)