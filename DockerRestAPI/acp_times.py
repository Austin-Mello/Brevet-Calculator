"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import time

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    """

    control = control_dist_km
    calc = 0.0
    start_time = brevet_start_time
    total_dist = brevet_dist_km

    #Proto-table
    two_hun = 200/34
    four_hun = 200/32 + two_hun
    six_hun = 200/30 + four_hun

    """ START TIME """
    #Empty set
    if start_time == "":
        return "Bad input"


    """ CONTROL POINTS """
    #Case 0: The empty set
    if control == "":
        return "Bad input"

    #Case 1: control < 0
    elif control < 0:
        return "Bad input"

    #Case 2: control > 20% of brevet distance
    elif control > total_dist + (total_dist/5):
        return "Bad input"

    #Case 3: Control is <= Brevit
    else:
        if total_dist <= 200:
            calc = control / 34
        elif total_dist <= 400:
            calc = two_hun + ((control - 200) / 32)
        elif total_dist <= 600:
            calc = four_hun + ((control - 400) / 30)
        else:
            calc = six_hun + ((control - 600) / 28)


        #Time conversion
        #Take the floor of the calc variable
        hrs = calc // 1
        #Multiply the remainder by 60, then round up/down
        mins = (calc - hrs) * 60
        mins = round(mins)

        #shift the start time
        open_time = start_time.shift(hours = hrs, minutes = mins)
    

    """
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    return open_time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    """ 
    control = control_dist_km
    calc = 0.0
    start_time = brevet_start_time
    total_dist = brevet_dist_km
    close_time = 0.0

    #Proto-table
    two_hun = 200/15
    four_hun = 200/15 + two_hun
    six_hun = 200/15 + four_hun

    """ START TIME """
    #Empty set
    if start_time == "":
        return "Bad input"


    """ CONTROL POINTS """
    #Case 0: The empty set
    if control == "":
        return "Bad input"

    #Case 1: control < 0
    elif control < 0:
        return "Bad input"

    #Case 2: Control is >= Brevet
    elif control >= total_dist:
        #Subcase 1: control > 20% of brevet distance
        if control > total_dist + (total_dist/5):
            return "Bad input"
        #Subcase 2: All good, assign the set time.
        else:
            if total_dist == 200:
                close_time = start_time.shift(hours = 13, minutes = 30)
            elif total_dist == 300:
                close_time = start_time.shift(hours = 20)
            elif total_dist == 400:
                close_time = start_time.shift(hours = 27)
            elif total_dist == 600:
                close_time = start_time.shift(hours = 40)
            else:
                close_time = start_time.shift(hours = 75)

    #Case 3: Control is < Brevit
    else:
        #Subcase 1: Control is less than 60
        if control < 60:
            #dist/20 + 1 hour
            calc = (control / 20) + 1 
        #Subcase 2: All good, calculate time based on the brevet.
        elif total_dist <= 200:
            calc = control / 15
        elif total_dist <= 400:
            calc = two_hun + ((control - 200) / 15)
        elif total_dist <= 600:
            calc = four_hun + ((control - 400) / 15)
        else:
            calc = six_hun + ((control - 600) / 11.428)


        #Time conversion
        #Take the floor of the calc variable
        hrs = calc // 1
        #Multiply the remainder by 60, then round up/down
        mins = (calc - hrs) * 60
        mins = round(mins)

        #shift the start time
        close_time = start_time.shift(hours = hrs, minutes = mins)
    
    """
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return close_time
    
