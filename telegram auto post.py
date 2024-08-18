from telethon import TelegramClient
from telethon.tl.functions.channels import CheckUsernameRequest
from telethon.tl.types import InputChannelEmpty
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import time
api_id = 7357692
api_hash = 'b113123d7856fda37b8a23726cbd6ba7' 
phone = '+212666666666' #telegram number
groups = [
    'ebay_seller_plus',
    'ebaymethod',
    'digitale_maroc',
    'ma_digital',
    'Ebay41',
    'Ebaybdarija0',
    'moroccanebaysellers',
    'eBayservices9',
    'iptv4kgratuit',
    'buysell_sam',
    'iptv_mac',
    'FANTASYSELLERS',
    'ecomparadise',
    'ebayaliexpressdigitale',
    'usdt_maroc',
    'aliexpressellermaroc',
    'AffiliateMarketing_Cpa',
    'Mailing_morocco',
    'mailersmorocco',
    'mailingmoroccopro',
    'fiverr_morocco',
    'ebay2k22',
    'USAfreelancer',
    'fiverr_gig_promotion',
    'youcanshopchat',
    'ecommaroctop',
    'Aliexpressseller12',
    'aliexpressbrazilseller',
    'netflixsellersoumit',
    'azure_seller',
    'etsydigitalchat',
    'amazon_web_services',
    'etsyarab'

]
# mesaage

msg='''
your msg
 
'''
# connect
client = TelegramClient('session_name',
                        api_id,
                        api_hash,
                        )
client.start()
# snd
while True:
    print('start again ----------')
    for member in groups:
        try:
            destination_channel_username = member
            entity = client.get_entity(destination_channel_username)
            client.send_message(entity=entity, message=msg)
            print("DONE POST  IN ", member)
        except:
            pass
    print('w8 10mn to try again -----------')
    break
print("DONE")