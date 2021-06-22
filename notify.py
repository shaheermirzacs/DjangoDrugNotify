#!/usr/bin/env python

import firebase_admin
from firebase_admin import credentials, messaging
import requests
import sys
from datetime import date

# baseUrl = "http://127.0.0.1:8000"
baseUrl = "https://drugnotify.herokuapp.com"


class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def getUsers():
    url = f"{baseUrl}/users"
    response = requests.get(url)
    response = response.json()
    print(response)
    return response


def saveTestToDB(user, testing, message):
    today = date.today()
    print(today)
    url = f"{baseUrl}/tests/"

    response = requests.post(
        url,
        data={
            "user": user.identifier,
            "date_checked": today,
            "testing": testing,
            "message": message,
        },
    )


def notifyUser(user, message):
    cred = credentials.Certificate(
        "drugtestnotify-firebase-adminsdk-trdly-a05ce5b447.json"
    )
    firebase_admin.initialize_app(cred)

    message = messaging.Message(
        notification=messaging.Notification(
            title=f"Hello {user.first_name}", body=message
        ),
        token=user.token,
    )

    response = messaging.send(message)
    print("Successfully sent message:", response)


def checkForTest(user):
    url = "https://sentry.cordanths.com/Sentry/WebCheckin/Log"

    response = requests.post(
        url,
        data={
            "phone": user.phone,
            "last_name": user.last_name,
            "ivr_code": user.ivr_code,
            "lang": "en",
        },
    )

    response = response.json()[0]

    if "text" in response:
        msg = response["text"]
    else:
        msg = response["error_msg"]

    testing = "required" in msg
    notificationMessage = "Aw shit drink that water boii" if testing else msg

    notifyUser(user, notificationMessage)
    saveTestToDB(user, testing, notificationMessage)


def main():
    if len(sys.argv) > 2:
        user = User(
            phone=sys.argv[1],
            first_name=sys.argv[2],
            last_name=sys.argv[3],
            ivr_code=sys.argv[4],
            token=sys.argv[5],
            identifier=sys.argv[6],
        )

        checkForTest(user)

    else:
        notificationPeriod = sys.argv[1]

        response = getUsers()

        for data in response:
            if data[f"notify_{notificationPeriod}"]:
                user = User(**data)
                checkForTest(user)


if __name__ == "__main__":
    main()
