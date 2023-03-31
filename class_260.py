from etherpad_lite import EtherpadLiteClient
from datetime import datetime
etherclient = EtherpadLiteClient(base_params={'apikey': '5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

new_pad = etherclient.createPad(padID='mynewpad', text='hello Everyone, How are you ???')
print('Your new pad is : ', new_pad)

createAuthor = etherclient.createAuthor(name='CloudUser')
print(createAuthor)

padcount = etherclient.padUsersCount(padID='mynewpad')
print(padcount)

timestamp = etherclient.getLastEdited(padID = 'mynewpad')
print(timestamp)
lastedit = timestamp['lastEdited']

date_conversion = datetime.fromtimestamp(lastedit/1000.0)
print("date _time: ", date_conversion)

delete_pad = etherclient.deletePad(padID='mynewpad')
print(delete_pad)