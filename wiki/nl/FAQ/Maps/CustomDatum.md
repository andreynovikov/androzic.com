# Aangepaste gegevens toevoegen

Androzic ondersteunt OziExplorer datums.dat file. Dit bestand moet worden opgeslagen in de Applicatie map (instelbaar in Preferences). Een voorbeeld is te vinden in de rubriek[downloads][1]. Hieronder een copie van het originele OziExplorer help artikel (met als verschil dat Androzic ieder aantal aangepaste kaartgegevens ondersteunt):

 [1]: ../../downloads.html

## Kaartgegevens van gebruikers toevoegen

OziExplorer kan tot 10, door de gebruiker beschreven, kaartgegevens gebruiken.

Om persoonlijke kaartgegevens toe te voegen aan OziExplorer gaat u alsvolgt te werk.

Maak een tekstbestand genaamd datums.dat in de OziExplorer directory, als dit bestand nog niet bestaat. OziExplorer leest dit bestand de eerst volgende keer dat het wordt gebruikt, de kaartgegevens van de gebruiker zullen altijd onderaan de lijst worden geplaatst.

voeg de volgende regel of regels (als er meer dan 1 moet worden toegevoegd) toe aan het bestand.

De regel wordt als volgt ingevoerd:

    Gegevens name, Ellipsoid nummer, dx, dy, dz
    

*Datum name* - iedere willekeurige naam

*Ellipsoid number* - Alle kaartgegevens hebben een referentie ellips, kies het nummer uit de onderstaande lijst. Als de ellips niet in deze lijst voor komt kan het niet worden toegevoegd. Neem kontakt op met de auteur van OziExplorer om de ellips te laten toevoegen in de code lijst.

*dx, dy, dz* - deze moeten bekend zijn voor de specifieke kaartgegevens die u invoert.

Tussen alle velden dient een komma te staan.

Voorbeeld - een regel in het bestand zou er zo uit kunnen zien

    NAD 27 User, 4 -8, 160, 176
     

## Ellips lijst

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