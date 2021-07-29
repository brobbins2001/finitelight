import math
def lightspeed_time(distance_to_object, full_angle=0, distance_to_second_observer=-1):
    if distance_to_second_observer < 0:
        distance_to_second_observer = distance_to_object
        full_angle=0
    hyp_squared = (distance_to_second_observer ** 2 + distance_to_object ** 2) - (2 * distance_to_second_observer * distance_to_object * math.cos(full_angle))
    hyp_left = math.sqrt((hyp_squared))

    c = 299792.458

    right_time = distance_to_object / c
    left_time = hyp_left/c

    time_diff = right_time-left_time

    time_diff = math.fabs(time_diff)
    return time_diff
