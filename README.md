In this project, I am using Turf.js to add spatial analysis to a web mapping application. I have made a a map of Calgary Schools and Calgary Health Clinics and Hospitals. When a user clicks on a school, the map will show which clinic or hospital is nearest.

**application.py:**
There is only 1 route needed for this project

1. `@app.route("/")` 
	- This route queries the database for all of the schools and all of the hospitals and clinics, and passes them to the index.html page
	
	-     schools = db.execute("SELECT * FROM schools").fetchall()
	      
	      hospitals = db.execute("SELECT * FROM hospitals").fetchall()
	

**import.py:**

- This file was used to import hospitals.csv and schools.csv into my database. 



**Index.html:**

- This page contains the Mapbox light-v10 style map, and is centered on Calgary. All schools and hospitals/clinics are loaded in (as 2 separate layers). Schools are represented by a graduation cap icon, and the hospitals and clinics are represented by a cross:

  ![](https://github.com/mitchellbrown98/ENGO551Lab4/blob/main/screenshots/2021-03-09_13h09_24.png)

- When you hover your mouse over an icon, the feature's name and address will be displayed in a styled popup:

  ![](https://github.com/mitchellbrown98/ENGO551Lab4/blob/main/screenshots/2021-03-09_13h09_39.png) ![](https://github.com/mitchellbrown98/ENGO551Lab4/blob/main/screenshots/2021-03-09_13h09_50.png) 

  When you move your mouse off of the icon, the popup will close by itself.

- When you click on a hospital/clinic icon, nothing will happen. When you click on a school icon, `turf.nearest()` is used to find the closest hospital feature, and `turf.distance()` is used to find the distance (in km) between the school and the nearest hospital. The nearest hospital will be marked with a green circle behind the icon. Additionally, a modal popup will appear that displays the 'From' school name and address, the 'To' hospital/clinic name and address, and the distance between the two features. The modal can be closed by clicking the 'x' in the top right corner, or by clicking anywhere off the modal:

  ![](https://github.com/mitchellbrown98/ENGO551Lab4/blob/main/screenshots/2021-03-09_13h10_00.png)

- Clicking on another school will remove the green mark from the old hospital, place it on the new nearest hospital, and re-open the modal with the newly updated information:

  ![](https://github.com/mitchellbrown98/ENGO551Lab4/blob/main/screenshots/2021-03-09_13h10_20.png)
