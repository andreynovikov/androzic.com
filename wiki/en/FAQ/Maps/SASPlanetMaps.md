Support for SAS.Planet Map Cache
================================

Androzic supports maps in [SAS.Planet](http://sasgis.org/sasplaneta/) cache format. It is as simple as copying map folder from SAS.Planet `'cache'`
folder to Androzic `'sas'` folder. You can then rename map folder as you wish, its name will be used as a map name in Androzic. This lets you have
multiple maps from one map provider for different regions.

Map cache folder can have multiple zooms, they will be used accordingly. The only limitation of Androzic is that the zooms have to be serial, like z5,z6,z7.
There should be no gaps in zooms sequence, like z5,z7,z8.

If original online map has Ellipsoid projection (see SAS.planet help for details), then you must additionally put empty file with the name `ellipsoid` in
map root folder (beside zoom level folders).

Unlike built-in online map, SAS cache maps behave as ordinary maps in Androzic: they can be zoomed to arbitrary zoom levels, they have margins, participate in
adjacent maps selection, etc. But unlike native ozf maps they are a little bit slow because they consist of regular images which are not optimized for quick
rendering.
