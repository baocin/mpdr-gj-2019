# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.objects import Objects  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_createobjects(self):
        """Test case for createobjects

        Create a objects
        """
        body = Objects()
        response = self.client.open(
            '/objects',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createuser(self):
        """Test case for createuser

        Create a user
        """
        body = User()
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleteobjects(self):
        """Test case for deleteobjects

        Delete a objects
        """
        response = self.client.open(
            '/objects/{objectsId}'.format(objectsId='objectsId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleteuser(self):
        """Test case for deleteuser

        Delete a user
        """
        response = self.client.open(
            '/users/{userId}'.format(userId='userId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getobject(self):
        """Test case for getobject

        Get a objects
        """
        response = self.client.open(
            '/objects/{objectsId}'.format(objectsId='objectsId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getobjects(self):
        """Test case for getobjects

        List All objects
        """
        response = self.client.open(
            '/objects',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getuser(self):
        """Test case for getuser

        Get a user
        """
        response = self.client.open(
            '/users/{userId}'.format(userId='userId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getusers(self):
        """Test case for getusers

        List All users
        """
        response = self.client.open(
            '/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updateobjects(self):
        """Test case for updateobjects

        Update a objects
        """
        body = Objects()
        response = self.client.open(
            '/objects/{objectsId}'.format(objectsId='objectsId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updateuser(self):
        """Test case for updateuser

        Update a user
        """
        body = User()
        response = self.client.open(
            '/users/{userId}'.format(userId='userId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
