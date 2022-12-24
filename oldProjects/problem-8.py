import pandas as pd
import datetime


def sendEmail(to, sub, msg):

    print(f"Email to {to} sent with subject: {sub} and message {msg}")


if __name__ == "__main__":
    df = pd.read_excel("automate.ods")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    print(yearNow)
    print(type(yearNow))
    # print(today)
    # print(type(today))
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item["Birthday"])
        bday = item['Birthday'].strftime("%d-%m")
        print(bday)

        msg = "I don't send birthday to people but you are such an awesome person in my life that I'm bound to send you an email on this occassion of your birthday. You are the best person and friend that I ever have."

        print(item["Year"])
        print(type(item["Year"]))

        if (today == bday) and yearNow not in item["Year"]:
            print("HAPPY BIRTHDAY!")
            sendEmail(item["Email"], "Happy Birthday", item["Dialogue"])
            writeInd.append(index)
