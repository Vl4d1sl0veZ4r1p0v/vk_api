# coding=utf-8
import argparse
import os
from utils import send_query, count_friends
from user.user import User


VERSION = os.getenv("VERSION", "5.131")
APP_ID = os.getenv("APP_ID", "7879934")
AUTH_QUERY = os.getenv("AUTH_QUERY", 'https://oauth.vk.com/authorize?client_id={}&display=page' \
             '&redirect_uri=https://oauth.vk.com/blank.html&scope=friends' \
             '&response_type=token&v={}'.format(APP_ID, VERSION))
QUERY_TEMPLATE = os.getenv("QUERY_TEMPLATE", "https://api.vk.com/method/friends.get?user_id={}" \
                 "&access_token={}&v={}&fields=first_name")
TOKEN = os.getenv("VK_TOKEN")
if TOKEN is None:
    raise ValueError("You need set environment variable VK_TOKEN with your "
                     "application token")


def get_args():
    parser = argparse.ArgumentParser(description="engine")
    parser.add_argument("-i", "--id",
                        type=int,
                        help="user id in vk")
    parser.add_argument("-a", "--auth",
                        action="store_true",
                        default=False,
                        help="use this args for authentification"
                        )
    return parser.parse_args()


def find_friends(user_id):
    data = send_query(user_id)
    response = data.get("response", {})
    friends_ids = response.get("items", {})
    friends = []
    for friend in friends_ids:
        user = User.from_dict(friend)
        user.count = count_friends(user.id)
        friends.append(user)
    return friends


if __name__ == "__main__":
    args = get_args()
    if args.auth:
        print("Open this link into your browser")
        print(AUTH_QUERY)
        print("And enter your access_token")
        TOKEN = input("Access_token: ")
    friends = find_friends(args.id)
    print(*sorted(friends, key=lambda f: f.count, reverse=True), sep="\n")
