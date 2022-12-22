import pandas as pd
import datetime


def sendEmail(to, sub, msg):

    pass


if __name__ == "__main__":
    df = pd.read_excel("automate.ods")
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    # print(today)
    # print(type(today))

    for index, item in df.iterrows():
        print(index, item["Birthday"])
        bday = item['Birthday'].strftime("%d-%m")
        print(bday)

        msg = "I don't send birthday to people but you are such an awesome person in my life that I'm bound to send you an email on this occassion of your birthday. You are the best person and friend that I ever have."

        if (today == bday):
            print("HAPPY BIRTHDAY!")
            sendEmail(to, "Happy Birthday", item["Dialogue"])
