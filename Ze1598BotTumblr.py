import pytumblr

#Module with the bots' credentials
import Ze1598Bot_credentials as bot_info
#Client object needed will be the already existing client object from 'Ze1598Bot_credentials'
client = bot_info.client

#module that contains two functions to inform of time and date
import get_Time_Date as T_D

#module that tests the internet connection being used, for down/upload speeds and ping
import InternetConnection_SpeedPing as ConnectSpeed

#[Text]Date and time update
client.create_text('ze1598bot', state="published", slug="testing-text-posts", title="Date and time update", body='{}\n{}.'.format(T_D.current_date(T_D.day_format), T_D.TalkingClock(T_D.time_format)))

#[Text]Connection speeds update
client.create_text('ze1598bot', state="published", slug="testing-text-posts", title="Connection speeds update", body='Current connection speeds\n{}\n{}\n{}'.format(ConnectSpeed.ping, ConnectSpeed.download, ConnectSpeed.upload))

#Create a photo post using a link from the web
client.create_photo('ze1598bot', state="published", tags=["first photo post", "papa bless", "have a kitten"], source="https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/articles/health_tools/taking_care_of_kitten_slideshow/photolibrary_rm_photo_of_kitten_in_grass.jpg")

print('Your post has been sent')