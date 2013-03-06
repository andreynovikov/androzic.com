Application change log
======================

1.7.3
-----

_not released yet_

 * Added double tap on map to switch following on/off
 * Added explanations on first run
 * Added support for local image references in waypoint descriptions
 * Added support for navigation to moving object
 * Added reduced icon set to be installed by default
 * Changed map dim so it does not alter device brightness anymore
 * Updated menu and action icons
 * Updated some interfaces to be more holo styled
 * Updated support links and credits
 * Fixed preloaded routes where not visible
 * Fixed saving waypoint descriptions with line feeds
 * Fixed notifications were not removed on crash
 * Fixed map objects where not cleared on exit
 * Fixed various crashes

1.7.2
-----

_13.02.2012_

 * Added double back exit confirmation option
 * Added Ukrainian localization
 * Fixed newly installed plugin initialization issue
 * Fixed crash on initialization on some devices
 * Fixed crash on opening HSI in landscape mode
 * Fixed crash on concurrent track update

1.7.1
-----

_24.01.2012_

 * Added support for national character encodings for text Ozi files
 * Added option to hide application action bar
 * Added support for View menu icons for plugins
 * Reorganized folder structure and settings
 * Added support for mock location providers
 * Returned back Remove button in waypoint information window
 * Made clicks on waypoints on modern devices easier
 * Removed non-working compass
 * Removed requirement for wake lock permission
 * Fixed displaying UTF-8 characters in waypoint description
 * Fixed blocking UI on maps folder preference change
 * Fixed various crashes

1.7
---

_13.01.2012_

 * `[NEW]` plugins support
 * `[NEW]` preload routes from files
 * `[NEW]` online maps of Finland
 * `[NEW]` OpenSeaMap online map (not very useful)
 * `[NEW]` Portuguese localization
 * `[NEW]` Swedish localization
 * `[ENH]` show filename in route list
 * `[FIX]` zero speed when first GPS fix is received in fast motion
 * `[FIX]` failure to index some maps
 * `[FIX]` failure to load some KML tracks and routes
 * `[FIX]` failure to download world map

1.6
---

_25.05.2012_

 * `[NEW]` adjacent maps
 * `[NEW]` crop map border
 * `[NEW]` continuous zoom
 * `[NEW]` Chinese localization
 * `[ENH]` show map border
 * `[ENH]` map scale indicator color setting
 * `[ENH]` optimized performance
 * `[ENH]` enhanced settings
 * `[FIX]` waiting indicator
 * `[FIX]` sensor data overflow
 * `[FIX]` various crashes

1.5
---

_12.03.2012_

 * `[NEW]` route details with navigation mode
 * `[NEW]` revised route management UI
 * `[NEW]` custom waypoint proximity in route (not compatible with OziExplorer)
 * `[NEW]` route ETE output
 * `[ENH]` map scale position change delay
 * `[ENH]` SMS listener moved to external plug-in
 * `[FIX]` support for devices without GPS
 * `[FIX]` route color loading
 * `[FIX]` crash on route waypoint edit in landscape mode
 * `[FIX]` various crashes

1.4.2
-----

_23.02.2012_

 * `[NEW]` route waypoint popup
 * `[ENH]` use popup instead of context menu for waypoints on map
 * `[FIX]` processing of map calibration specified by easting and northing
 * `[FIX]` continuous track on temporary signal loss
 * `[FIX]` magnetic course calculation
 * `[FIX]` waypoint proximity and altitude couldn't be cleared
 * `[FIX]` some crashes

1.4.1
-----

_16.02.2012_

 * `[NEW]` map scale bar
 * `[NEW]` support for armeabi-v7a and x86 platforms
 * `[NEW]` support for MSF map calibration parameter
 * `[ENH]` display zoom level in online map name
 * `[ENH]` display HDOP and VDOP in information view
 * `[ENH]` added Potsdam Rauenberg DHDN datum
 * `[FIX]` broken compass
 * `[FIX]` crash on loading corrupted waypoints file
 * `[FIX]` crash on trying to clean not existing current track

1.4
---

_5.02.2012_

 * `[NEW]` revised waypoint management UI
 * `[ENH]` new sliding panel handler
 * `[ENH]` new menu icons
 * `[ENH]` added more actions to sliding panel
 * `[ENH]` UI optimizations
 * `[ENH]` smaller minimum sharing update interval value
 * `[FIX]` all waypoint sets were saved into default set
 * `[FIX]` editing coordinates in DD MM.MM mode with 0 degrees
 * `[FIX]` crash on empty NMEA sentence

1.3
---

_30.01.2012_

 * `[NEW]` map view always shows location
 * `[NEW]` MSL altitude
 * `[NEW]` two-mode vector line
 * `[NEW]` waypoint altitude and proximity
 * `[NEW]` waypoint date (without editing)
 * `[NEW]` location sharing available for everyone
 * `[NEW]` custom map providers available for everyone
 * `[ENH]` GPS connection and tracking can be switched off
 * `[ENH]` configurable sliding panel actions
 * `[ENH]` "new waypoint" menu item
 * `[ENH]` map centers on newly created waypoints
 * `[ENH]` new notification icons
 * `[ENH]` location position indicator
 * `[ENH]` manual distance measurement mode
 * `[ENH]` color selection UI in properties
 * `[FIX]` core services redesign
 * `[FIX]` satellite panel hiding was broken
 * `[FIX]` crash on paste location from clipboard

1.2.3
-----

_13.01.2012_

 * `[NEW]` waypoint sets (files)
 * `[NEW]` custom waypoint marker icons
 * `[NEW]` donators can use custom online map sources
 * `[ENH]` application root fully configurable
 * `[ENH]` waypoint colors editable both globally and individually
 * `[ENH]` added NGO1948 datum
 * `[ENH]` color preference shows current color
 * `[ENH]` better Holo theme support on Honecomb+ devices
 * `[FIX]` waypoint position was incorrectly shared
 * `[FIX]` online map was not fully shown on low zooms
 * `[FIX]` sliding panel was flickering on close

1.2.2
-----

_20.12.2011_

 * `[ENH]` enabling online map does not need restart
 * `[FIX]` online map flicker
 * `[FIX]` various force closes on opening data files
 * `[FIX]` application not showing in Android Market for tablets and some other devices

1.2.1
-----

_17.12.2011_

 * `[ENH]` added more online map providers
 * `[FIX]` '(SUI) Swiss Grid' projection was broken
 * `[FIX]` crash on starting real-time location sharing

1.2
---

_15.12.2011_

 * `[NEW]` online maps support
 * `[NEW]` Turkish localization
 * `[ENH]` more popular datums
 * `[ENH]` reorganized settings
 * `[ENH]` updated web links
 * `[FIX]` move to zero coordinates in offline mode

1.1
---

_06.12.2011_

 * `[NEW]` real time location sharing in group
 * `[ENH]` information view shows location provider
 * `[ENH]` initialization view shows donation status
 * `[FIX]` slider based settings where broken
 * `[FIX]` unexpected move to zero coordinates

1.0.1
-----

_24.10.2011_

 * `[NEW]` German localization
 * `[NEW]` Hungarian localization
 * `[FIX]` occasional crash on first location acquisition
 * `[FIX]` occasional crash on map information view

1.0
---

_17.10.2011_

 * `[NEW]` Bulgarian localization
 * `[NEW]` Polish localization
 * `[NEW]` Dutch localization (partial)
 * `[FIX]` speed leaps
 * `[FIX]` compass view broken
 * `[FIX]` navigation to waypoint lost on device rotation

0.9.22b
-------

_24.09.2011_

 * `[NEW]` paste location coordinates from clipboard
 * `[NEW]` listen for coordinates in incoming SMS traffic
 * `[NEW]` Spanish localization
 * `[NEW]` Italian localization (partial)
 * `[NEW]` link for donation
 * `[ENH]` new status bar icons
 * `[FIX]` search menu item for modern phones and tables without hardware search button


0.9.21b
-------

_18.09.2011_

 * `[NEW]` map index can be reset
 * `[ENH]` minor optimizations for tablets (Honeycomb)

0.9.20b
-------

_15.09.2011_

 * `[NEW]` UTM coordinates
 * `[FIX]` route navigation cancel on screen rotation

0.9.19b
-------

_21.08.2011_

 * `[NEW]` share location
 * `[NEW]` copy location coordinates to clipboard
 * `[NEW]` share waypoint location

0.9.18b
-------

_20.02.2011_

 * `[NEW]` location from networks is used if GPS location not available
 * `[NEW]` location is saved on quiting application
 * `[ENH]` larger sliding panel handle on high DPI screens
 * `[FIX]` waypoint and track file compatibility with older versions of OziExplorer
 * `[FIX]` application crash on start while trying to load corrupted waypoints file

0.9.17b
-------

_08.02.2011_

 * `[NEW]` custom distance grid
 * `[NEW]` current track can be split by day/week
 * `[ENH]` faster map and zoom switch
 * `[ENH]` screen wake lock configurable
 * `[FIX]` parasitic drag detected at the end of pinch zoom 
 * `[FIX]` possibility to drag map without actually stopping following 	
 * `[FIX]` crash when opening problem map
 * `[FIX]` crash on trying to open map in non-ozf format

0.9.16b
-------

_30.01.2011_

 * `[NEW]` Finnish localization
 * `[ENH]` improvements in map image file processing
 * `[ENH]` format of map image file is determined based on file contents instead of file extension
 * `[FIX]` map image files with uppercase extensions where incorrectly processed
 * `[FIX]` move application to SD was not working

0.9.15b
-------

_25.01.2011_

 * `[NEW]` partial map grid support
 * `[ENH]` sliding drawler remembers its state
 * `[FIX]` colors where processed incorrectly in data files

0.9.14b
-------

_17.01.2011_

 * `[NEW]` application usable without maps
 * `[FIX]` crash on application start under Android 1.6

0.9.13.4b
---------

_15.01.2011_

 * `[FIX]` crash on loading data files with uppercase extensions
 * `[FIX]` best map was not loaded
 * `[FIX]` search for maps at location was broken in 0.9.13.3b

0.9.13.3b
---------

_12.01.2011_

 * `[NEW]` draw location accuracy circle
 * `[NEW]` request almanac update for faster cold start
 * `[ENH]` location accuracy displayed on information screen
 * `[ENH]` declination displayed on information screen
 * `[FIX]` crash on maps without corner markers
 * `[FIX]` added some missing datums
 * `[FIX]` incorrect parsing of map calibration points

0.9.13.2b
---------

_05.01.2011_

 * `[FIX]` location was incorrectly displayed on some maps with two calibration points
 * `[FIX]` wrong coordinate display in southern hemisphere in DDMM and DDMMSS formats
 * `[FIX]` UTM projection was incorrectly processed, once more

0.9.13.1b
---------

_03.01.2011_

 * `[ENH]` optimized zoom levels
 * `[FIX]` fixed crash on navigation start

0.9.13b
-------

_02.01.2011_

 * `[NEW]` cursor color configurable
 * `[NEW]` custom moving cursor
 * `[FIX]` tracking notification remained after crash
 * `[FIX]` application could not restart after crash
 * `[FIX]` waypoints where deleted on crash
 * `[FIX]` crash on preferences change on Android less than 2.2

0.9.12b
-------

_01.01.2011_

 * `[NEW]` start progress screen
 * `[ENH]` much faster drag of zoomed maps
 * `[FIX]` UTM projection was incorrectly processed, again

0.9.11b
-------

_30.12.2010_

 * `[NEW]` map index cached for faster application start
 * `[NEW]` magnetic declination support
 * `[FIX]` some datums where missing

0.9.10.1b
---------

_29.12.2010_

 * `[FIX]` UTM projection was incorrectly processed

0.9.10b
-------

_28.12.2010_

 * `[NEW]` backup preferences via native Android backup service (Froyo 2.2 and higher)
 * `[NEW]` oziexplorer datums.dat support
 * `[FIX]` some datums where missing
 * `[FIX]` map failed to index if .map contained empty strings

0.9.9b
------

_25.12.2010_

 * `[NEW]` sliding drawer
 * `[ENH]` application can be moved to SD card
 * `[ENH]` full screen mode (optional)

0.9.8.1b
--------

_24.12.2010_

 * `[NEW]` experimental: pinch zoom
 * `[FIX]` out of memory on large zooms
 * `[FIX]` waypoints, tracks and routes where not shown if 'hide on drag' was set
 * `[FIX]` distance measure broken

0.9.8b
------

_23.12.2010_

 * `[NEW]` map rendering rewritten
 * `[NEW]` projections and datums support rewritten

0.9.7b
------

_12.12.2010_

 * `[NEW]` experimental: convert track to route
 * `[NEW]` track edit (details)
 * `[ENH]` new route edit icons
 * `[ENH]` application path configurable
 * `[FIX]` map with two calibration points could not be used
 * `[FIX]` tracks without elevation where considered in wrong format

0.9.6.1b
--------

_05.11.2010_

 * `[FIX]` application crashed on exit
 * `[FIX]` infinite satellite search

0.9.6b
------

_03.11.2010_

 * `[NEW]` HSI screen
 * `[NEW]` compass screen
 * `[NEW]` information screen
 * `[ENH]` smooth look ahead
 * `[ENH]` performance improvements
 * `[FIX]` crash on loading bad data files

0.9.5b
------

_28.11.2010_

 * `[NEW]` French localization
 * `[NEW]` search coordinates in various formats
 * `[NEW]` search loaded waypoints, tracks and routes
 * `[ENH]` search has query history
 * `[ENH]` ETE calculation logic changed
 * `[ENH]` map buttons have state

0.9.4b
------

_25.11.2010_

 * `[NEW]` map and data folders configurable
 * `[NEW]` support for external SD card on Galaxy S family (not tested)
 * `[ENH]` waypoint properties usability improvement
 * `[ENH]` preferences reorganized

0.9.3b
------

_23.11.2010_

 * `[NEW]` load tracks in kml and gpx formats
 * `[NEW]` load routes in kml and gpx formats
 * `[ENH]` distance measure shows precise bearing
 * `[FIX]` application crashed on first run if no maps present

0.9.2b
------

_22.11.2010_

 * `[NEW]` project new waypoint
 * `[NEW]` show waypoint info
 * `[ENH]` waypoint description can contain HTML
 * `[ENH]` links to FAQ and feature request

0.9.1b
------

_21.11.2010_

 * `[NEW]` draw proximity circles
 * `[NEW]` distance measurement
 * `[NEW]` load waypoints in kml and gpx formats
 * `[NEW]` load unfinished route at next application start
 * `[NEW]` SHOW_RADAR hook for external applications
 * `[ENH]` better route navigation logic

0.9b
----

_19.11.2010_

 * `[NEW]` landscape orientation support
 * `[NEW]` orientation restriction in application
 * `[NEW]` credits page

0.8.6b
------

_17.11.2010_

 * `[NEW]` list maps for current position
 * `[NEW]` language can be selected in application
 * `[ENH]` better trackball processing
 * `[ENH]` memory optimizations
 * `[FIX]` coordinates input in locales with comma decimal separator
 * `[FIX]` Czech localization had incorrect language code

0.8.5b
------

_16.11.2010_

 * `[NEW]` use compass for current track if not moving
 * `[ENH]` wait indicator on some long operations
 * `[ENH]` sort waypoints by distance
 * `[ENH]` map list displays pixel scale

0.8.4b
------

_15.11.2010_

 * `[NEW]` Czech localization
 * `[NEW]` draw compass if not moving or no GPS fix
 * `[ENH]` Display preferences for waypoint and track
 * `[FIX]` current track was not drawn when maximum length reached

0.8.3b
------

_14.11.2010_

 * `[NEW]` fix time is written to current track log
 * `[ENH]` better waypoint tap processing
 * `[ENH]` map objects stay visible while dragging (configurable)
 * `[ENH]` great track draw improvement
 * `[ENH]` memory use optimization
 * `[ENH]` status icon and text now informative
 * `[FIX]` out of memory issue crashed application
 * `[FIX]` map overlays twitched on every location change
 * `[FIX]` permitted dragging to nonexistent coordinates
 * `[FIX]` current track log didn't honor minimum distance

0.8.2b
------

_12.11.2010_

 * `[NEW]` create new route
 * `[NEW]` edit route
 * `[NEW]` save route
 * `[ENH]` world map is now loaded from server
 * `[FIX]` best map was not honoring forcibly selected map
 * `[FIX]` look ahead with 0% drag ahead produced blank map margins
 * `[FIX]` dim was not reapplied on preference change

0.8.1b
------

_09.11.2010_

 * `[ENH]` dim disabled by default
 * `[ENH]` units honored everywhere
 * `[ENH]` performance optimizations

0.8b
----

_08.11.2010_

 * `[NEW]` route navigation
 * `[NEW]` route management (name, visibility, color)
 * `[ENH]` look ahead enhancements

0.7.1b
------
 
_07.11.2010_

 * `[NEW]` load route(s) from file
 * `[NEW]` show route(s)
 * `[NEW]` coordinate format in waypoint properties
 * `[ENH]` map update interval configurable
 * `[ENH]` dim configurable
 * `[ENH]` coordinate display format configurable
 * `[FIX]` waypoint could not be tapped

0.7b
----

_04.11.2010_

 * `[NEW]` track management (name, visibility, color)
 * `[NEW]` save track to file
 * `[NEW]` remove track
 * `[ENH]` current track honors GPS fix loss
 * `[ENH]` performance optimization of waypoint drawing
 * `[ENH]` great memory optimization of look ahead feature
 * `[ENH]` dim screen at night
 * `[ENH]` 'drag ahead' preloads map to show on dragging
 * `[ENH]` core library performance optimization
 * `[FIX]` removed crash reports - was buggy
 * `[FIX]` map corner markers support, again

0.6.9b
------

_02.11.2010_

 * `[NEW]` load arbitrary map
 * `[NEW]` map corner markers support
 * `[FIX]` crashed on close and restart while navigating

0.6.8b
------

_01.11.2010_

 * `[NEW]` D-pad support (follow/not follow, move map)
 * `[ENH]` load best scale map can be disabled and time period configurable
 * `[FIX]` no trackball issue fixed (no way to disable auto follow)

0.6.7b
------

_01.11.2010_

 * `[NEW]` look ahead
 * `[NEW]` search locations via Google geocoder
 * `[NEW]` crash reports are automatically sent to developer
 * `[ENH]` current waypoints are saved after each modification
 * `[ENH]` 'Ensure visible' in waypoint menu
 * `[ENH]` better various screen density support
 * `[FIX]` corrupt zoom after map change

0.6.6b
------

_30.10.2010_

 * `[NEW]` strict following/not following (by default, configurable)
 * `[NEW]` current log is written in batches
 * `[NEW]` trackball support (follow/not follow, move map)
 * `[NEW]` stop navigation and clear track tail menu
 * `[ENH]` different cursor color in not following mode and on no satellite fix
 * `[ENH]` selecting Navigate in waypoint list now returns to main map window
 * `[ENH]` GPS status indicator again
 * `[FIX]` best scale map was reseting zoom if map not changed
 * `[FIX]` app crashed if SD card not present

0.6.5b
------

_28.10.2010_

 * `[NEW]` distance unit preference
 * `[NEW]` elevation unit preference
 * `[NEW]` current track color preference
 * `[NEW]` try to load best scale map each 5 seconds
 * `[ENH]` GPS status indicator

0.6.4b
------

_27.10.2010_

 * `[NEW]` speed unit preference
 * `[ENH]` load best scale map at startup
 * `[FIX]` speed display was showing debug info

0.6.3b
------

_25.10.2010_

 * `[NEW]` load waypoints from file
 * `[NEW]` save waypoints to file
 * `[ENH]` if exists obtain location from cellular network at startup
 * `[ENH]` new application icon
 * `[FIX]` tracking notification now returns to old map window but not starts a new one

0.6.2b
------

_25.10.2010_

 * `[NEW]` indexed maps list
 * `[ENH]` added twitter link in properties
 * `[ENH]` single speed leaps are filtered
 * `[ENH]` VMG is now lightly smoothed
 * `[FIX]` fixed ETE display at zero speed
 * `[FIX]` fixed VMG and ETE display layout

0.6.1b
------

_23.10.2010_

 * `[ENH]` display navigation waypoint name, VMG and ETE
 * `[FIX]` fixed Russian localization
 * `[FIX]` fixed localized decimal point written to ozi files

0.6b
----

_23.10.2010_

 * `[NEW]` navigation to waypoint
 * `[ENH]` parameter displays now have titles
 * `[BUG]` landscape mode disabled for a time being

0.5.1b
------

_23.10.2010_

 * `[NEW]` waypoint management (name, description, coordinates)

0.5b
----

_19.10.2010_

 * `[NEW]` basic waypoint management
 * `[NEW]` built-in world map for dummies

0.4b
----

_16.10.2010_

 * `[NEW]` load track(s) from file
 * `[NEW]` notify if maps folder missing at startup
 * `[FIX]` fixed track visualization

0.3b
----

_15.10.2010_

 * `[NEW]` store current track into file
 * `[NEW]` track log preferences
 * `[FIX]` fixed speed display

0.2b
----

_14.10.2010_

 * `[NEW]` current track display
 * `[NEW]` basic information displays: speed, bearing, elevation

0.1a
----

_09.10.2010_

 * `[NEW]` map index
 * `[NEW]` switch between maps
 * `[NEW]` zoom maps
 * `[NEW]` drag maps
 * `[NEW]` show current position and movement direction
