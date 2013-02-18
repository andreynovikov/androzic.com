How to add custom online maps to Androzic and OziMapper
=======================================================

> This article is applicable both for Androzic and OziMapper.

Enabling custom online maps
---------------------------

Custom online maps can be added through special text file. The file has to be named `providers.dat` and be placed in the Application folder (configured in Settings).

File format
-----------

`providers.dat` is a text file, each line describes single provider. Each provider is described by a set of fields separated by commas. All fields are required, order is strict, no space allowed. If field is undefined for specific provider it must be empty.

*List and order of fields:*

 # title - map title
 # code - unique code, only letters and digits allowed, is used as a tile cache directory name
 # minzoom - minimum zoom, allowed by map
 # maxzoom - maximum zoom, allowed by map
 # tilesize - avarage tile size in bytes, can be left empty for default
 # url - tile provider url containing special placeholders (see bellow)
 # server1 - server substring, can be empty if not applicable
 # server2 - server substring, can be empty if not applicable
 # server3 - server substring, can be empty if not applicable
 # server4 - server substring, can be empty if not applicable
 # params - extra parameters: yinverse - inverse Y tile number, ellipsoid - use ellipsoid Mercator projection (default is spherical)

*URL placeholders:*

 * {$s} - server substring (cycles through variants)
 * {$l} - locale
 * {$z} - zoom
 * {$x} - X tile number
 * {$y} - Y tile number
 * {$q} - quad tree
 * {comma} - replaced by comma, should be used if url contains comma

Examples
--------

Fully functional example file can be found in [Downloads](../../downloads.html) section. Following examples are already included in application:

    OpenStreetMap Mapnik,osm,0,18,22000,http://{$s}.tile.openstreetmap.org/{$z}/{$x}/{$y}.png,a,b,c`
    MapQuest,mq,0,18,,http://otile{$s}.mqcdn.com/tiles/1.0.0/osm/{$z}/{$x}/{$y}.png,0,1,2,3`
    Charts VFR (US),aeromaps,5,12,,http://www.aeromaps.us/Z{$z}/{$y}/{$x}.png`
    Chartbundle US Area Charts,cbenra,4,13,,http://wms.chartbundle.com/tms/1.0.0/enra/{$z}/{$x}/{$y}.png,,,,,yinverse`

Special cases
-------------

1. If you want some online map to be included into distribution you can share its full description and it will be included in Androzic if it meets two criteria:

    1. Map license permits it's usage in third-party applications. (e.g. Google maps are not included due to license restrictions)
    2. Map is valuable for significant amount of users (country wide, community wide, etc).

2. If you want to add a provider but tile URL has unsupported format please send as much facts as you know about it so that support can be added in next Androzic updates.
