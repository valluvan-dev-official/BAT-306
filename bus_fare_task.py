

import dis


def Calculate_fare(distance_km,time_min):

    base_fare = 5

    # Distance fare :

    if distance_km <= 5:

        distance_fare = distance_km * 2

    else:

        distance_fare = (5 * 2) + ((distance_km - 5) * 1.5)

    # Time fare :

    if time_min <= 10:

        time_fare = time_min * 0.50

    else:
        time_fare = (10 * 0.50) + ((time_min - 10) * 0.30)


    # Long Distance :

    sur_charge = 10 if distance_km > 20 else 0 


    total_fare = base_fare + distance_fare + time_fare + sur_charge

    print("======== Fare Breakdown : ==========")
    
    print(f"Base Fare : ${base_fare}")
    print(f"Distance Fare : ${distance_fare}")
    print(f"Time Fare : ${time_fare}")
    print(f"Long Distance Surcharge : ${sur_charge}")
    
    print("===================================")

    print("Total Fare : $",round(total_fare,2))


   
distance = float(input("Enter distance traveled (in km): "))
time = float(input("Enter time taken (in minutes): "))

Calculate_fare(distance,time)