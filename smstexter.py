from twilio.rest import Client

def messege():
    account_sid = 'ACf7c6ad4287594da43bbeac100b7f53e4'
    auth_token = '2da3a9e00f38f55e3c2b3e370cdf3b43'
    client = Client(account_sid, auth_token)
    # body = "raj"
    f = open('database.csv','r')
    body = f.read()

    message = client.messages.create(
        from_='+12057840665',
        body = body,
        to='+916387591732'
    )