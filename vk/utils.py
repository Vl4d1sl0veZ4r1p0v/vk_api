# coding=utf-8
import requests
import json


def send_query(user_id, query_template, token, version):
    query = query_template.format(user_id, token, version)
    response = requests.get(query)
    return json.loads(response.text)


def count_friends(user_id):
    data = send_query(user_id)
    return 0 if "error" in data else data["response"]["count"]