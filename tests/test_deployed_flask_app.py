import json
import requests

BASE_URL = "http://122.35.146.37:5001/predict/"


def test_test_page():
    resp = requests.get(BASE_URL)
    assert resp.status_code == 200
    assert resp.content == 200


# def test_status():
#     # Additional headers.
#     headers = {"Content-Type": "application/json"}
#     # Body
#     payload = {
#         "url": "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
#     }
#     resp = requests.post(BASE_URL, headers=headers, data=json.dumps(payload, indent=4))
#     print(resp.content)
#     assert resp.status_code == 200


# def test_predict():
#     # Additional headers.
#     headers = {"Content-Type": "application/json"}
#     # Body
#     payload = {
#         "url": "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
#     }
#     resp = requests.post(BASE_URL, headers=headers, data=json.dumps(payload, indent=4))
#     resp_json = resp.json()
#     # resp_json = json.loads(resp.data.decode("utf-8"))
#     expected = {"class_id": "n02099712", "class_name": "Labrador_retriever"}
#     assert len(resp_json) == len(expected)
#     for item, expected_item in zip(resp_json.items(), expected.items()):
#         assert item[0] == expected_item[0]
#         assert item[1] == expected_item[1]
