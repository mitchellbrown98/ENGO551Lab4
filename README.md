application.py:
There is only 1 route needed for this lab

1. `@app.route("/")` 
	- This route passes the username, style_ids, and access token for the Mapbox tile layers, and renders the index.html page.
	

`Index.html:`

- This page contains an edited mapbox tile layer without the traffic dataset, which is initially seen when you load the page. ![](https://github.com/mitchellbrown98/ENGO551Lab3/blob/main/screenshots/2021-03-05_14h30_31.png)

- You have the ability to toggle between the tile layer without the dataset, or the one with the dataset with this popup:

  ![](https://github.com/mitchellbrown98/ENGO551Lab3/blob/main/screenshots/2021-03-05_14h30_41.png) 

  Both were created in mapbox studio. You can also enter full screen mode with this button:

  ![](https://github.com/mitchellbrown98/ENGO551Lab3/blob/main/screenshots/2021-03-05_14h07_02.png)

- For this lab, the focus is on the traffic points and roadways they occur on, so the map background has been darkened, along with the green features, water ports, airports, pedestrian roadways, etc as they are not as relevant. The labels have been updated as well for ease of viewing with the dark background.

- Orange greatly contrasts with green, so I have made the traffic points orange, on top of the various green roadways to ensure they easily stand out.![](https://github.com/mitchellbrown98/ENGO551Lab3/blob/main/screenshots/2021-03-05_14h06_52.png)

- I chose a radius of 4px for the traffic points, as that size will fit inside the roadway when you are zoomed into the map. The points will also adjust their size based on the zoom layer, so it is easy to see where they are grouped together when you zoom out, but can be easily identified and differentiated when you zoom in. I chose to use no blur, and full opacity so the points appear sharp and easily stand out.

- I chose to include the natural features, place labels, point of interest labels, road networks, terrain, transit, and walking & cycling components as these can aid in the visualization and correlation of the traffic incident dataset. 
