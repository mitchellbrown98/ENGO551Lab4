import os, csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# set database url
DATABASE_URL='postgres://nchktprwfkcsft:cfb2627d3c6fa6c9ba947539605df51858775532eae09fb65fa61dbaf36d02a9@ec2-54-198-252-9.compute-1.amazonaws.com:5432/d8lojdc2ophhqj'

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

school = open ("hospitals.csv")
reader = csv.reader(school)
for name, address, longitude, latitude in reader:
    db.execute("INSERT INTO hospitals (name, address, lng, lat) VALUES (:name, :address, :lng, :lat)",
    {"name": name, "address": address, "lng": longitude, "lat": latitude})
print("import success")

db.commit()
