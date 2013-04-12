#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, os.path, time, math
import simplejson as json
import MySQLdb
from webob import Request, Response

import wsgiref.handlers

def application(environ, start_response):
    request = Request(environ)
    response = Response(content_type='text/plain', charset='utf-8')
    response.cache_expires(0)
    response.cache_control.private = True

    session = request.params.get('session', None)
    user = request.params.get('user', None)
    debug = request.params.get('debug', None)
    silent = request.params.get('silent', None)

    data = {}

    if session is not None:
        conf = dbconf()
        db = MySQLdb.connect(user=conf['user'], passwd=conf['passwd'], db=conf['db'], use_unicode=conf['use_unicode'],
                             charset=conf['charset'])
        cursor = db.cursor(MySQLdb.cursors.DictCursor)

        if user is not None:
            params = toDict(request.params.items())
            # initialize optional parameters
            params.setdefault('elevation', None)
            params.setdefault('accuracy', None)

            cursor.execute('''INSERT INTO location(session, user, lat, lon, speed, track, elevation, accuracy, ftime)
                              VALUES (%(session)s, %(user)s, %(lat)s, %(lon)s, %(speed)s, %(track)s, %(elevation)s,
                              %(accuracy)s, %(ftime)s)''', params)
            db.commit()

        if silent is not None:
            cursor.close()
            response.text = ''
            return response(environ, start_response)

        data['session-key'] = session
        data['users'] = []

        cursor.execute('''SELECT location.id, user, lat, lon, speed, track, elevation, accuracy, ftime FROM location
                          INNER JOIN (SELECT MAX(id) AS id FROM location WHERE session = %s GROUP BY user) last
                          ON location.id = last.id''', (session))

        for user in cursor:
            # remove optional unset parameters
            if user['elevation'] == None:
                del user['elevation']
            if user['accuracy'] == None:
                del user['accuracy']
            data['users'].append(user)

        cursor.close()

        if session == 'test':
            ftime = time.time()
            distance = 100000 # 100 km
            plane = fakerotator(u'Москва', 55.7517, 37.6178, distance, ftime)
            data['users'].append(plane)
            plane = fakerotator(u'Melbourne', -37.7833, 144.9667, distance, ftime)
            data['users'].append(plane)
            plane = fakerotator(u'Montréal', 45.5081, -73.5550, distance, ftime)
            data['users'].append(plane)

    params = {'ensure_ascii': False}
    if debug is not None:
        params['indent'] = 4;
    response.text = json.dumps(data, **params)
    return response(environ, start_response)

def fakerotator(name, lat, lon, distance, ftime):
    seconds = int(ftime) % 3600
    degree = seconds * 0.1
    coords = project(lat, lon, distance, degree)
    plane = {}
    plane['user'] = name
    plane['speed'] = 0.001745317 * distance # 360 deg / hour
    plane['track'] = (degree + 90) % 360 # clockwise rotation
    plane['lat'] = coords[0]
    plane['lon'] = coords[1]
    plane['elevation'] = 900 # TODO: make it fluctuating
    plane['accuracy'] = 3
    plane['ftime'] = int(ftime * 1000)
    return plane

def project(lat, lon, distance, bearing):
    # WGS-84 ellipsoid
    a = 6378137
    b = 6356752.3142
    f = 1 / 298.257223563

    s = distance
    alpha1 = math.radians(bearing)
    sinAlpha1 = math.sin(alpha1)
    cosAlpha1 = math.cos(alpha1)

    tanU1 = (1 - f) * math.tan(math.radians(lat))
    cosU1 = 1 / math.sqrt((1 + tanU1*tanU1))
    sinU1 = tanU1 * cosU1
    sigma1 = math.atan2(tanU1, cosAlpha1)
    sinAlpha = cosU1 * sinAlpha1
    cosSqAlpha = 1 - sinAlpha * sinAlpha
    uSq = cosSqAlpha * (a * a - b * b) / (b * b)
    A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
    B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))

    sigma = s / (b * A)
    sigmaP = 2 * math.pi

    iterLimit = 100

    while True:
        cos2SigmaM = math.cos(2 * sigma1 + sigma)
        sinSigma = math.sin(sigma)
        cosSigma = math.cos(sigma)
        deltaSigma = B * sinSigma * (cos2SigmaM + B / 4 * (cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM) - \
                     B / 6 * cos2SigmaM * (-3 + 4 * sinSigma * sinSigma) * (-3 + 4 * cos2SigmaM * cos2SigmaM)))
        sigmaP = sigma
        sigma = s / (b*A) + deltaSigma
        iterLimit -= 1
        if math.fabs(sigma - sigmaP) <= 1e-12 or iterLimit == 0:
            break

    tmp = sinU1 * sinSigma - cosU1 * cosSigma * cosAlpha1
    lat2 = math.atan2(sinU1 * cosSigma + cosU1 * sinSigma * cosAlpha1, \
           (1 - f) * math.sqrt(sinAlpha * sinAlpha + tmp * tmp))
    lmbda = math.atan2(sinSigma * sinAlpha1, cosU1 * cosSigma - sinU1 * sinSigma * cosAlpha1)
    C = f / 16 * cosSqAlpha * (4 + f * (4 - 3 * cosSqAlpha))
    L = lmbda - (1 - C) * f * sinAlpha * \
        (sigma + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM)))

    result = [math.degrees(lat2), lon + math.degrees(L)]
    return result

def toDict(L):
    r = {}
    for i in L:
        k, v = i[0], i[1]
        r[i[0]] = i[1]
    return r

def dbconf():
    path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(path, 'db.json'), 'r') as data_file:
        data = json.load(data_file)
    return data

if __name__ == '__main__':
    wsgiref.handlers.CGIHandler().run(application)
