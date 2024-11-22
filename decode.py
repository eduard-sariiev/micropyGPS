from datetime import datetime

def decodeGPS(gps_string):
    # DD = d + (min/60) + (sec/3600)
    lat_d = int(gps_string[:2], 16)
    lat_min = int(gps_string[2:7], 16)/10000
    long_d = int(gps_string[7:9], 16)
    long_min = int(gps_string[9:14], 16)/10000
    direction = int(gps_string[14:15], 16)
    speed = int(gps_string[15:17], 16)
    alt = int(gps_string[17:20], 16)
    dop = int(gps_string[20:22], 16)/16/3
    lat = lat_d + (lat_min/60) * (1 if direction > 2 else -1)
    long = long_d + (long_min/60) * (1 if direction & 0b01 else -1)
    #logfile.write(f'{round(datetime.now().timestamp(), 2)},{lat:.9},{long:.9},{speed},{alt},{dop:.4}')
    #print(f'Lat:{lat:.9}\nLong:{long:.9}')
    print(f'[{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}] {speed}km/s {alt}m {dop:.4}q https://www.google.com/maps/search/?api=1&query={lat:.9}%2C{long:.9}')