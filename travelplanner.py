distance_miles = 8
is_raining = False 
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_miles:
    print(False) 
elif distance_miles <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_miles > 1 and distance_miles <= 6:
    if has_bike and not is_raining:
        print(True) 
    else:
        print(False)
elif distance_miles > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)