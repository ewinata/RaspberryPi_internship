

def ddm_dd_convert(coord, direction):
    """Converts GPS reading from DDM to DD
       str coord - the ddm coordinate from $GPGGA
       str direction - the direction of the coord (N,S,W,E)
       returns - string representation of dd coordinate
    """
    value = ''
    if (direction == 'S' or direction == 'W'):
        value += '-'
    value += coord[0:-7] 
    minute = float(coord[-7:])
    decimal = round(minute / 60, 8)
    result = str(decimal)[1:]
    value += result
    return value

def gprmc_convert(line):
    """Translates $GPRMC line into documented array
       str line - the GPRMC line
       returns - the data documented into array
    """
    gps = line.strip().split(',')
    #check data
    if gps[2] == 'V':
        return
    raw_date = gps[9]
    time = ''
    date = raw_date[0:2]
    month = raw_date[2:4]
    year = raw_date[4:]
    #modify year if reaches year 2100
    time += date + '/' + month + '/20' + year
    return [time]


def gpvtg_convert(line):
    """Translates $GPVTG line into documented array
       Data only used for measuring ground speed
       str line - the GPVTG line
       returns - the data documented into array
    """
    gps = line.strip().split(',')
    #check data
    if gps[1] == '0.00': 
        return
    #jsondata = {'Horizontal speed': gps[7] + ' kmph or ' + gps[5] + 'knots'}
    return []


def gpgga_convert(line):
    """Translates $GPGGPA line into documented array
       str line - the GPGGA line
       returns - the data documented into array
    """
    gps = line.strip().split(',')
    #check data
    if gps[6] == '0' :
        return
    fix = ''
    if gps[6] == '1':
        fix = 'GPS fix'
    elif gps[6] == '2':
        fix = 'DGPS fix'
    elif gps[6] == '4':
        fix = 'RTK Fix coordinate (centimeter precision)'
    elif gps[6] == '5':
        fix = 'RTK Float (decimeter precision)'
    #utc = gps[1][0:2] + ':' + gps[1][2:4] + ':' + gps[1][4:6]
    lat = ddm_dd_convert(gps[2], gps[3])
    long = ddm_dd_convert(gps[4], gps[5])   
    return [lat, long, fix]

              
def gpgsa_convert(line):
    """Translates $GPGSA line into documented array
       str line - the GPGSA line
       returns - the data documented into array
    """
    gps = line.strip().split(',')
    #check data
    if gps[2] == '1':
        return
    if gps[2] == '2':
        fix = '2D fix'
    else:
        fix = '3D fix'
    return [fix]