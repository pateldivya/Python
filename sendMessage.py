from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACc76af9ba53c62062ba46bfd3016b75a8" 
AUTH_TOKEN = "c81643758831b348d8e80636adc8afb4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
message = client.sms.messages.create(
    to="+16309985068", 
    from_="+13314256791", 
    body="Hello",
)

print(message.sid)
