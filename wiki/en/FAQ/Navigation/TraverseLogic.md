Traverse logic
==============

Sometimes there is no way or no need to reach waypoint proximity distance. This is where traverse logic helps. Look at the illustration:

![Illustration](traverse.png)

Let’s assume you are going from Turin to Strasbourg, it means that Strasbourg is an active route waypoint and Turin-Strasbourg is an active route leg. Passing Bern you decided to skip Strasbourg and go directly to Berlin. In this case you will never reach Strasbourg proximity and navigation will not switch to new route leg (Strasbourg-Berlin). This leg has a traverse - a line perpendicular to the leg and crossing source waypoint, it is drawn in red on illustration. As soon as you cross the traverse Androzic assumes that you wish to navigate along that leg and switches to the next route waypoint (Berlin in our case). This behavior can be turned off in Settings.
