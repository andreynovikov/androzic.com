# Añadir datums del usuario

Androzic es compatible con el fichero datums.dat de OziExplorer. Este fichero debe estar situado en la Carpeta de la Aplicación (configurada en las preferencias). Se puede encontrar un fichero de ejemplo en la sección de [Descargas][1]. A continuación se muestra la reimpresión del artículo de ayuda de OziExplorer original (con la diferencia de que Androzic admite cualquier número de referencias del usuario):

 [1]: ../../downloads.html

## Agregar datums del usuario

OziExplorer puede utilizar hasta 10 datums definidos por el usuario.

Para añadir datums del usuario a OziExplorer debe hacer lo siguiente.

Si no existe ya Crear un archivo de texto llamado datums.dat en el directorio de OziExplorer. OziExplorer leerá este fichero la próxima vez que sea ejecutado. Los Datums del usuario serán añadidos siempre al final de la lista.

Añade dentro de este fichero la siguiente línea (o líneas, si hay que añadir más de un datum).

El formato de la línea es como sigue:

    Nombre del Datum, Número Elipsoidal, dx, dy, dz
    

*Datum name* - Cualquier nombre que quieras introducir

*Ellipsoid number* - Todos los datums tienen un elipsoide de referencia, elige el número de la lista de abajo. Si el elipsoide no está en esta lista, entonces no puedes agregar el datum, necesitas contactar con el autor de OziExplorer y conseguir que añada el elipsoide.

*dx, dy, dz* - deben ser conocidos para el datum particular que estás introduciendo.

Debe usarse una coma entre todos los campos.

Ejemplo - Una línea en el archivo puede ser algo así

    NAD 27 usuario, 4 -8, 160, 176
     

## Lista de elipsoides

1.  'Airy 1830'; a: 6377563.396; invf: 299.3249646
2.  'Modified Airy'; a: 6377340.189; invf: 299.3249646
3.  'Australian National'; a: 6378160.0; invf: 298.25 
4.  'Bessel 1841'; a: 6377397.155; invf: 299.1528128
5.  'Clarke 1866'; a: 6378206.4; invf: 294.9786982
6.  'Clarke 1880'; a: 6378249.145; invf: 293.465
7.  'Everest (India 1830)'; a: 6377276.345; invf: 300.8017
8.  'Everest (1948)'; a: 6377304.063; invf: 300.8017
9.  'Modified Fischer 1960'; a: 6378155.0; invf: 298.3
10. 'Everest (Pakistan)'; a: 6377309.613; invf: 300.8017
11. 'Indonesian 1974'; a: 6378160.0; invf: 298.247
12. 'GRS 80'; a: 6378137.0; invf: 298.257222101
13. 'Helmert 1906'; a: 6378200.0; invf: 298.3
14. 'Hough 1960'; a: 6378270.0; invf: 297.0
15. 'International 1924'; a: 6378388.0; invf: 297.0
16. 'Krassovsky 1940'; a: 6378245.0; invf: 298.3
17. 'South American 1969'; a: 6378160.0; invf: 298.25
18. 'Everest (Malaysia 1969)'; a: 6377295.664; invf: 300.8017
19. 'Everest (Sabah Sarawak)'; a: 6377298.556; invf: 300.8017
20. 'WGS 72'; a: 6378135.0; invf: 298.26
21. 'WGS 84'; a: 6378137.0; invf: 298.257223563
22. 'Bessel 1841 (Namibia)'; a: 6377483.865; invf: 299.1528128
23. 'Everest (India 1956)'; a: 6377301.243; invf: 300.8017
24. 'Clarke 1880 Palestine'; a: 6378300.789; invf: 293.466 
25. 'Clarke 1880 IGN'; a: 6378249.2; invf: 293.466021
26. 'Hayford 1909'; a: 6378388.0; invf: 296.959263
27. 'Clarke 1858'; a: 6378350.87;invf: 294.26
28. 'Bessel 1841 (Norway)' ; a: 6377492.0176;invf: 299.1528
29. 'Plessis 1817 (France)'; a: 6376523.0 ; invf: 308.6409971
30. 'Hayford 1924'; a: 6378388.0; invf: 297.0
