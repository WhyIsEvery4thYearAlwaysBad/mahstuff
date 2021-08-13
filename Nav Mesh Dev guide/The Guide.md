(This guide is under development.)

Just a heads up: **This guide uses pictures to illustrate some sections.** It is thus recommend to enable picture elements on your browser. If you can't do that, then download the assets so you can follow long easier (and also save bandwidth).

# TF2 Navmesh Development Guide

This is a guide dedicated to Mapmakers or Navmesh Developers. It is recommend to read the VDC Wiki entries on the [Navigation Mesh](https://developer.valvesoftware.com/wiki/Navigation_Meshes) and [`tf_bot`s](https://developer.valvesoftware.com/wiki/Tf_bot) as this guide assumes that you have some background knowledge and experience with Nav Meshes.

## Useful Commands
<hr>
</hr>

* `tf_show_blocked_areas` - Shows areas blocked by a demographic (Purple for both teams, red for RED team, blue for BLU team). This is handy for debugging TF attribute logic.

## Techniques

### Airstrafe Paths
<hr>

You can get bots to airstrafe to a spot by organizing nav ares into a layout that I call the "Airstrafe Path".

![](assets/airstrafe_pic.gif)
(Nav Areas are marked by green squares, bidirectional connections are light blue, and monoconnections are blue.)

Bots at the starting point will presumably jump to the turning point, then turn towards the the destination once they hit the turning point nav area and will reach the destination.

Airstrafe paths don't have to be in this *particular* layout. For instance you can reverse the starting point and destination, add two destinations, use monodirectional connections instead of bidirectional connections, etc.

### Stacked Areas

There will be moments where you'll need multiple TFAttributes to get bots to work with some map logic, or a specific path of nav areas to setup bots for a jump. Since TFAttributes actually *override* each others blocked status, and you often want to preserve the original nav area for full movement, it is often a good idea to stack nav areas on top of nav areas.

Tip: `nav_splice`, `nav_shift`, `nav_corner_raise`, and `nav_corner_lower` will help you shift nav areas onto each other.

## Testing a Nav mesh
<hr>

Navmeshes need testing so that you can fix bugs in them and ensure they actually function, before releasing them or implementing the nav mesh into your map.

### Test a specific path

Traditionally specific paths are tested through `bot_moveto` with a puppet bot. Unfortunately though, `bot_moveto` currently does not work in Team Fortress 2, so the next best alternative is to tnstead you will have to use flags to get bots to move to a nav area.

<!-- The FAQ

## FAQ

### "What's the point of improving/making nav meshes when I can just use nav_generate?"

There's a reason you're reading this. `nav_generate` does an okish job at creating a nav mesh, but it is definitely not perfect; it often generates biconnections where they shouldn't be, fails to account for all possible areas that players can reach, etc. These sorts of details can influence how well bots play TF2, and may in fact turn off a player from them.

At the very least if you don't want to take some time to fix up a navmesh, then please set-->

Checksum: <!-- Insert checksum here. -->