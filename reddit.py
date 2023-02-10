import praw
import re
import json
import os
reg = re.compile(r".*((\.png)|(\.jpg))")
reddit = praw.Reddit(
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
    user_agent="android:com.example.guessr:v1.2.3 (by u/guessrtest)",

)
reddit.read_only = True

with open('src/lib/urls.json', 'r', encoding="utf-8") as f:
    d = json.load(f)

posturl_list = []

top_post = reddit.subreddit(
    'tinder+news+pcmasterrace+damnthatsinteresting+leagueoflegends+whatcouldgowrong+facepalm+gaming+politics+therewasanattempt+unexpected+movies+dankmemes+buildapc+meirl+wtf+pokemon+minecraft+todayilearned+europe+anime+pcgaming+dota2+lifeprotips+techsupport+mildlyvandalised+dataisbeautiful+cozyplaces+funnymemes+wholesomememes+mademesmile+memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+wallpapers+liminalspaces+perfecttiming+tumblr+itookapicture+astrophotography+photography+science+outoftheloop+animemes+nottheonion+cats+selfawarewolves+justrolledintotheshop+cursedcomments+lifehacks+homeimprovements+whatisthisthing+comics+art+meme+blursedimages+thathappened+startledcats+worldnews+food+diy+books+space+gadgets+upliftingnews+getmotivated+history+philosophy+television+technology+fitness+oddlysatisfying+travel+animalsbeingderps+animalsbeingbros+tattoos+gardening+beamazed+trippinthroughtime+bikinibottomtwitter+rarepuppers+starterpacks+cars+eyebleach+makeupaddiction+holup+crappydesign+deepintoyoutube+nasa+camping+wellthatsucks+dnd+diwhy+frugal+dogs+marvelmemes+solotravel+fantasy+programmerhumor+natureismetal+terriblefacebookmemes+somethingimade+wallpaper+softwaregore+catastrophicfailure+madlads+comedyheaven+thatsinsane+iamverysmart+forbiddensnacks+oddlyspecific+boneappletea'
).hot(limit=500)

for post in filter(lambda x: reg.search(x.url), top_post):
    data = {}
    data["image"] = post.url
    data["subreddit"] = post.subreddit.display_name
    data["title"] = post.title
    if data not in d:
        posturl_list.append(data)

print(posturl_list)

new_data = posturl_list
with open('src/lib/urls.json', 'w') as f:
    json.dump(new_data, f)
