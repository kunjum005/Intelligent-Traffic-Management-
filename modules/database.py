"""
database.py

Handles MySQL operations.
"""

import mysql.connector


def connect_database():
    """
    Create MySQL connection.
    """

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="traffic_management"
    )

    return connection


def save_report(
    location,
    video_name,
    counts,
    total,
    density,
    signal_time
):
    """
    Save traffic report to database.
    """

    try:

        connection = connect_database()

        cursor = connection.cursor()

    except Exception as e:

        print(e)

        return

    query = """
    INSERT INTO traffic_reports
    (
        location,
        video_name,
        cars,
        motorcycles,
        buses,
        trucks,
        total_vehicles,
        traffic_density,
        signal_time
    )

    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (

        location,

        video_name,

        float(counts["Car"]),

        float(counts["Motorcycle"]),

        float(counts["Bus"]),

        float(counts["Truck"]),

        float(total),

        density,

        signal_time

    )

    cursor.execute(query, values)

    try:

        connection.commit()

        print("✅ Report saved successfully.")

    except Exception as e:

        print(e)

    finally:

        cursor.close()

        connection.close()
    
def get_all_reports():
    """
    Fetch all traffic reports from database.
    """

    connection = connect_database()

    cursor = connection.cursor()

    query = """
    SELECT
        id,
        location,
        video_name,
        cars,
        motorcycles,
        buses,
        trucks,
        total_vehicles,
        traffic_density,
        signal_time
    FROM traffic_reports
    ORDER BY id ASC
    """

    cursor.execute(query)

    reports = cursor.fetchall()

    cursor.close()

    connection.close()

    return reports