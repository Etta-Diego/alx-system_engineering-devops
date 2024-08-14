#!/usr/bin/python3

"""Retrieving Todo list progress info of a given employee ID"""

import requests
import sys

if '__name__" == __main__:
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/"
    url = baseUrl + employeeId
    response
