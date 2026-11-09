import psycopg2 
conn = psycopg2.connect( host="localhost", port=5432, dbname="lab10", user="postgres", password="lab123") 
print("Connection Successfull!!!")
cur = conn.cursor()

#Question 1
print("\nQuestion 1") 
cur.execute("""SELECT DISTINCT s.satellite_name FROM Satellites s JOIN Downlinks d ON s.satellite_id = d.satellite_id
JOIN Ground_Stations g ON d.station_id = g.station_id WHERE d.status = 'Completed' AND g.region = 'North' ORDER BY s.satellite_name;""") 
for row in cur.fetchall(): 
    print(row) 

#Question 2    
print("\nQuestion 2") 
cur.execute("""SELECT g.station_name, SUM(d.data_gb) AS total_data_gb FROM Ground_Stations g JOIN Downlinks d ON g.station_id =
d.station_id WHERE d.status = 'Completed' GROUP BY g.station_id, g.station_name HAVING SUM(d.data_gb)>30 ORDER BY total_data_gb DESC;""") 
for row in cur.fetchall(): 
    print(row) 

#Question 3  
print("\nQuestion 3") 
cur.execute("""SELECT s.satellite_id, s.satellite_name, COUNT(DISTINCT d.station_id) AS station_count, SUM(d.data_gb) AS 
total_completed_data_gb FROM Satellites s JOIN Downlinks d ON s.satellite_id = d.satellite_id WHERE d.status = 'Completed' GROUP BY 
s.satellite_id, s.satellite_name HAVING COUNT(DISTINCT d.station_id) >= 2 ORDER BY station_count DESC, s.satellite_name;""") 
for row in cur.fetchall(): 
    print(row) 

#closing the connection   
cur.close() 
conn.close() 