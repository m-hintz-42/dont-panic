import requests

andy = 'http://127.0.0.1:5000/api/andy/'
matt = 'http://127.0.0.1:5000/api/matt/'
michael = 'http://127.0.0.1:5000/api/michael/'
get_headers = {'Accept': 'application/json'}
post_headers = {'Content-type': 'application/json'}


def andy_endpoint(seed_data, uuid, expected_response):
    url = andy + uuid
    response = requests.post(url=url, json=seed_data, headers=post_headers)
    if response.status_code != 201:
        assert False, "ERROR: Server responded with a " + response.status_code + ". Expected a 201"
    string_response = response.json()['Success']
    if string_response != expected_response:
        assert False, "ERROR: Expected response did not match the server response." + "\n" + "Expected: \n" \
                      + expected_response + "\n Actual: \n" + string_response
    print "Andy is good"


def matt_endpoint(uuid, payload, expected_response):
    url = matt + uuid
    response = requests.post(url=url, json=payload, headers=post_headers)
    if response.status_code == 404:
        assert False, "ERROR: No record with uuid " + uuid + " was found."
    elif response.status_code != 200:
        assert False, "ERROR: Server responded with a " + response.status_code + ". Expected a 200"
    if response.json() != expected_response:
        assert False, "ERROR: Expected response did not match the server response." + "\n" + "Expected: \n" \
                      + expected_response + "\n Actual: \n" + response.json()
    print "Matt is good"


def michael_endpoint(uuid, expected_response):
    url = michael + uuid
    response = requests.get(url=url, headers=get_headers)
    if response.status_code == 404:
        assert False, "ERROR: No record with uuid " + uuid + " was found."
    elif response.status_code != 200:
        assert False, "ERROR: Server responded with a " + response.status_code + ". Expected a 200"
    if response.json() != expected_response:
        assert False, "ERROR: Expected response did not match the server response." + "\n" + "Expected: \n" \
                      + expected_response + "\n Actual: \n" + response.json()
    print "Michael is good"

#############
expected = 'Yo ' + str(42) + ' worked!'
andy_endpoint('test andy', str(42), expected)
matt_endpoint(str(42), 'test matt', 'test andy')
michael_endpoint(str(42), 'test matt')
