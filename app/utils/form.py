import requests
import json

def get_coords():
    r = requests.get("https://ipinfo.io/loc")
    coords = r.content[:-1]
    x = coords[:7].decode("utf-8")
    y = coords[8:].decode("utf-8")
    return [x,y]


def submit_form():

    coords = get_coords()
    lat = coords[0]
    long = coords[1]
    print(lat)
    print(long)

    firstname = "John"
    lastname = "Doe"

    s = requests.session()
    s.cookies.clear()

    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B350 Safari/8536.25'}

    postlocation = "http://a841-dotvweb01.nyc.gov/Potholeform/ViewController/CreateComplaint.aspx"

    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE":  "/wEPDwUKMjAwNDE4OTYzOA9kFgICAQ9kFgQCAQ9kFgICAw8WAh4EVGV4dAWYATxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iL1BvdGhvbGVmb3JtL1ZpZXdDb250cm9sbGVyL1N0eWxlcy9JbnB1dC5hc3AiPjxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iL1BvdGhvbGVmb3JtL1ZpZXdDb250cm9sbGVyL1N0eWxlcy9HZW5lcmFsLmNzcyI+ZAIFD2QWBAIBDw8WAh8ABRYmbmJzcCBIZWxwIEluc3RydWN0aW9uZGQCAw8PFgIfAAWjATxicj48Yj4tPC9iPglBbGwgZmllbGRzIHdpdGggPGZvbnQgY29sb3IgPXJlZD4qKjwvZm9udD4gYXJlIHJlcXVpcmVkLjxicj48YnI+PGI+LTwvYj4JRGF0ZSBmb3JtYXQgOiA/LzgvMjAwNT9icj48YnI+PGI+LTwvYj4JRW1haWwgZm9ybWF0OiDigJxkZWZlY3RAc2VydmVyLmNvbT9icj5kZGQM9D4VeGjaq5GsipyyG6es0fWlkg==",
        "__EVENTVALIDATION": "/wEdAA3xNeXhrccgebHlZf4L/9INNffes58hs9XHD8v8pv8H3HU67CZhYnGl7UW/tUjloiyWliaRCWbNZdpqkduTP0O90kM4EEIpWbVXU1aIII4yuPtMppeAQJfVxvJeI950exBeOTdpQlUE2JCEchC+A8S/Ei2rwdIFPJe6/H7j7VMG9VpKsY/iDj46WRX8wBIF2SUsy7pm1xaab0/vzw9GeuJAFv3FMy0IKMA4E6OBHGPbzPJmwkBs073ntcZO8gUidrKazPn9NMkaMBuCexMNCxp6Eqs6uREL6ybXbP3gnAtELJtdX04=",
        "txFirstName": firstname,
        "txLastName": lastname,
        "txHN": "",
        "txStreetAddress": "",
        "txCity": "",
        "txState": "",
        "txZipCode": "",
        "txEmail": "",
        "txPhoneNumber": "",
        "txWorkNumber": "",
        "txDateObserved": "",
        "bSubmit": "Next >>"
    }

    s.post(postlocation, data=payload)
    print("first form completed")



    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long + "&key=AIzaSyD0EKYyK97KnMZWTDQTEovUbpM1rxmjzf8")
    data = json.loads(r.text)
    print(data)
    address = data["results"][0]["address_components"]
    number = address[0]["long_name"]
    street = address[1]["long_name"]
    boro = address[3]["long_name"]
    boronum = 0

    if(boro == "Bronx"):
        boronum = 2

    if(boro == "Queens"):
        boronum = 3


    postloc2 = "http://a841-dotvweb01.nyc.gov/Potholeform/ViewController/LocationValidation.aspx?action=create"

    payload2 = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__LASTFOCUS": "",
        "__VIEWSTATE": "/wEPDwUKLTkwMjc1NjMxOQ9kFgICAQ9kFgICBw9kFgQCAQ9kFgJmD2QWCAIBDxBkZBYBZmQCBQ9kFgICAg8QZGQWAGQCCQ9kFgQCAQ9kFgRmDw8WAh4EVGV4dGVkZAICDxBkZBYAZAIDDxBkZBYBZmQCCw9kFgQCAQ9kFgRmDw8WAh8AZWRkAgIPEGRkFgBkAgMPEGRkFgFmZAIDD2QWAmYPZBYCZg8PZBYCHgdvbmNsaWNrBRFzaG93cHJvY2Vzc2luZygpO2RkAOTw81a88BNaOQqS2qsVEtTG5uQ=",
        "__EVENTVALIDATION": "/wEdABYN1J7q5QgqjyFj7ZntzwMUzfg78Z8BXhXifTCAVkevd4JZnRb1y2Cqm6mI7fZ2zFPr9j2AOBWqFg777lmyHks9js5xgB1qtgEgcQ6o5QeKJVxANYx0c6w0ViuNlEx+P6NCEukiiiUkie9HgQ3PZzLBbZV35OTo5PRXBLT6/V7FdD1Pj58PK+QM0Bt6izk9i0hfJvH9EpXF+Y29fagPDFBxChLJqIP89hxtjfkmOYPTs9zc/scrx2CPOtTpmq/aKgq++ruyUiu40CBrL8g5jxwW3wzaRnua9bi3RaKQXLpNN9dq+4YL/GP0IJwQbuB7ZY53PFfToRfGoX9MLeV7o4hmxF6q+U+3q/NYDjpPGgitC3KSUzygTdiwhiheNxHTqkYhBDcv9zrkO9q8vGI9jLB3mRo2FsCWzh2jwT7Mq5vhoxi08poMJjBwaT+xMGu1IkaGXQj3SXdvnUgfhn/VH0pCSVpN+w1hk/vU/bVvYCTfWIDbqAg=",
        "RadioButtonList2": "A",
        "txHouseNumber": number,
        "iddOnstreet:txTextBox": street,
        "ddlOnBoro": boronum,
        "txSpecificLocation": "",
        "rdLane": "DRV",
        "btSubmit": "Submit"

    }

    s.post(postloc2, data=payload2)
    print("second form completed")

submit_form()
