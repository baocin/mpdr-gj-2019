import connexion
import json
import six
import sqlite3
from flask import jsonify

from swagger_server.models.objects import Objects  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

db = sqlite3.connect('game.db', check_same_thread=False)
cursor = db.cursor()
try:
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, role TEXT, long DECIMAL, lat DECIMAL, lastOnline TEXT, health DECIMAL, deviceId TEXT)''')
    cursor.execute('''CREATE TABLE objects(id INTEGER PRIMARY KEY, dmg BOOL, endLat DECIMAL, endLong DECIMAL, hp BOOL, lat DECIMAL, long DECIMAL, name TEXT, radius DECIMAL, speed DECIMAL, startLat DECIMAL, startLong DECIMAL)''')
    db.commit()
except Exception:
    pass

def createobjects(body):  # noqa: E501
    """Create a objects

    Creates a new instance of a &#x60;objects&#x60;. # noqa: E501

    :param body: A new &#x60;objects&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Objects.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        cursor.execute('''INSERT INTO users( dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?)''', (body.dmg,body.end_lat, body.end_long, body.hp, body.lat, body.long, body.name, body.radius, body.speed, body.start_lat, body.start_long))
        db.commit()
    return cursor.lastrowid


def createuser(body):  # noqa: E501
    """Create a user

    Creates a new instance of a &#x60;user&#x60;. # noqa: E501

    :param body: A new &#x60;user&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        cursor.execute('''INSERT INTO users(name, role, long, lat, health, lastOnline, deviceId)
                  VALUES(?,?,?,?,?,?,?)''', (body.name, body.role, body.long, body.lat, body.health, body.last_online, body.device_id))
        db.commit()
    return cursor.lastrowid


def deleteobjects(objectsId):  # noqa: E501
    """Delete a objects

    Deletes an existing &#x60;objects&#x60;. # noqa: E501

    :param objectsId: A unique identifier for a &#x60;objects&#x60;.
    :type objectsId: str

    :rtype: None
    """
    return 'do some magic!'


def deleteuser(userId):  # noqa: E501
    """Delete a user

    Deletes an existing &#x60;user&#x60;. # noqa: E501

    :param userId: A unique identifier for a &#x60;user&#x60;.
    :type userId: str

    :rtype: None
    """
    return 'do some magic!'


def getobject(objectsId):  # noqa: E501
    """Get a objects

    Gets the details of a single instance of a &#x60;objects&#x60;. # noqa: E501

    :param objectsId: A unique identifier for a &#x60;objects&#x60;.
    :type objectsId: str

    :rtype: Objects
    """
    
    cursor.execute('''SELECT dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong from objects WHERE id=?''', (objectsId))
    row = cursor.fetchone()
    jsonObject = {}
    jsonObject['dmg'] = row[0]
    jsonObject['endLat'] = row[1]
    jsonObject['endLong'] = row[2]
    jsonObject['hp'] = row[3]
    jsonObject['lat'] = row[4]
    jsonObject['long'] = row[5]
    jsonObject['name'] = row[6]
    jsonObject['radius'] = row[7]
    jsonObject['speed'] = row[8]
    jsonObject['startLat'] = row[9]
    jsonObject['startLong'] = row[10]
    return jsonify(jsonObject)


def getobjects():  # noqa: E501
    """List All objects

    Gets a list of all &#x60;objects&#x60; entities. # noqa: E501


    :rtype: List[Objects]
    """
    cursor.execute('''SELECT dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong from objects''')
    all_rows = cursor.fetchall()
    jsonUserList = []
    for row in all_rows:
        jsonObject = {}
        # name, role, long, lat, health, lastOnline, deviceId
        jsonObject['dmg'] = row[0]
        jsonObject['endLat'] = row[1]
        jsonObject['endLong'] = row[2]
        jsonObject['hp'] = row[3]
        jsonObject['lat'] = row[4]
        jsonObject['long'] = row[5]
        jsonObject['name'] = row[6]
        jsonObject['radius'] = row[7]
        jsonObject['speed'] = row[8]
        jsonObject['startLat'] = row[9]
        jsonObject['startLong'] = row[10]
        jsonUserList.append(jsonObject)
    return jsonify(jsonUserList)

def getuser(userId):  # noqa: E501
    """Get a user

    Gets the details of a single instance of a &#x60;user&#x60;. # noqa: E501

    :param userId: A unique identifier for a &#x60;user&#x60;.
    :type userId: str

    :rtype: User
    """
    cursor.execute('''SELECT name,role,lat,long,health,lastOnline,deviceId FROM users WHERE id=?''', (userId,))
    row = cursor.fetchone()
    jsonObject = {}
    jsonObject['name'] = row[0]
    jsonObject['role'] = row[1]
    jsonObject['lat'] = row[2]
    jsonObject['long'] = row[3]
    jsonObject['health'] = row[4]
    jsonObject['lastOnline'] = row[5]
    jsonObject['deviceId'] = row[6]
    return jsonify(jsonObject)


def getusers():  # noqa: E501
    """List All users

    Gets a list of all &#x60;user&#x60; entities. # noqa: E501


    :rtype: List[User]
    """
    cursor.execute('''SELECT name,role,lat,long,health,lastOnline,deviceId  FROM users''')
    all_rows = cursor.fetchall()
    jsonUserList = []
    for row in all_rows:
        jsonObject = {}
        # name, role, long, lat, health, lastOnline, deviceId
        jsonObject['name'] = row[0]
        jsonObject['role'] = row[1]
        jsonObject['lat'] = row[2]
        jsonObject['long'] = row[3]
        jsonObject['health'] = row[4]
        jsonObject['lastOnline'] = row[5]
        jsonObject['deviceId'] = row[6]
        jsonUserList.append(jsonObject)
    print(all_rows)
    return jsonify(jsonUserList)


def updateobjects(objectsId, body):  # noqa: E501
    """Update a objects

    Updates an existing &#x60;objects&#x60;. # noqa: E501

    :param objectsId: A unique identifier for a &#x60;objects&#x60;.
    :type objectsId: str
    :param body: Updated &#x60;objects&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong
        json = connexion.request.get_json()
        body = Objects.from_dict(json) 
        if ('dmg' in json):
            cursor.execute('''UPDATE objects SET name = ? WHERE id = ? ''', (body.dmg, objectsId))
        if ('endLat' in json):
            cursor.execute('''UPDATE objects SET role = ? WHERE id = ? ''', (body.end_lat, objectsId))
        if ('endLong' in json):
            cursor.execute('''UPDATE objects SET lat = ? WHERE id = ? ''', (body.end_long, objectsId))
        if ('hp' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.hp, objectsId))
        if ('lat' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.lat, objectsId))
        if ('long' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.long, objectsId))
        if ('name' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.name, objectsId))
        if ('radius' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.radius, objectsId))
        if ('speed' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.speed, objectsId))
        if ('startLat' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.startLat, objectsId))
        if ('startLong' in json):
            cursor.execute('''UPDATE objects SET long = ? WHERE id = ? ''', (body.startLong, objectsId))
        db.commit()
    return getobject(objectsId)


def updateuser(userId, body):  # noqa: E501
    """Update a user

    Updates an existing &#x60;user&#x60;. # noqa: E501

    :param userId: A unique identifier for a &#x60;user&#x60;.
    :type userId: str
    :param body: Updated &#x60;user&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        json = connexion.request.get_json()
        body = User.from_dict(json)  # noqa: E501
        if ('name' in json):
            cursor.execute('''UPDATE users SET name = ? WHERE id = ? ''', (body.name, userId))
        if ('role' in json):
            cursor.execute('''UPDATE users SET role = ? WHERE id = ? ''', (body.role, userId))
        if ('lat' in json):
            cursor.execute('''UPDATE users SET lat = ? WHERE id = ? ''', (body.lat, userId))
        if ('long' in json):
            cursor.execute('''UPDATE users SET long = ? WHERE id = ? ''', (body.long, userId))
        if ('health' in json):
            cursor.execute('''UPDATE users SET health = ? WHERE id = ? ''', (body.health, userId))
        if ('last_online' in json):
            cursor.execute('''UPDATE users SET lastOnline = ? WHERE id = ? ''', (body.last_online, userId))
        if ('device_id' in json):
            cursor.execute('''UPDATE users SET deviceId = ? WHERE id = ? ''', (body.device_id, userId))
        db.commit()
    return getuser(userId)
