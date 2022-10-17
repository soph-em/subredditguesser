import praw
import re
import json
import redditSecret
reg = re.compile(r".*((\.png)|(\.jpg))")
reddit = praw.Reddit(
    client_id=redditSecret.client_id,
    client_secret=redditSecret.client_secret,
    user_agent="android:com.example.guessr:v1.2.3 (by u/guessrtest)",

)
reddit.read_only = True

with open('src/lib/urls.json', 'r', encoding="utf-8") as f:
    d = json.load(f)

posturl_list = []

top_post = reddit.subreddit(
    'tinder+interestingasfuck+whitepeopletwitter+antiwork+news+pcmasterrace+damnthatsinteresting+leagueoflegends+whatcouldgowrong+facepalm+gaming+politics+therewasanattempt+wallstreetbets+unexpected+movies+dankmemes+buildapc+meirl+wtf+pokemon+shitposting+leopardsatemyface+minecraft+wellthatsucks+todayilearned+europe+anime+pcgaming+dota2+lifeprotips+techsupport+blackpeopletwitter+mildlyvandalised+dataisbeautiful+cozyplaces+funnymemes+meirl+wholesomememes+mademesmile+memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+foodporn+historyporn+wallpapers+earthporn+abandonedporn+liminalspaces+carporn+mapporn+perfecttiming+tumblr+itookapicture+skyporn+astrophotography+spaceporn+photography+science+humansbeingbros+outoftheloop+animemes+nottheonion+sadcringe+choosingbeggars+cats+animalsbeingderps+selfawarewolves+justrolledintotheshop+cursedcomments+lifehacks+deuxmoi+homeimprovements+whatisthisthing+comics+art+meme+blursedimages+thathappened+startledcats+oldpeoplefacebook+gaming+worldnews+pics+food+diy+books+space+gadgets+upliftingnews+getmotivated+tifu+history+philosophy+television+technology+fitness+natureisfuckinglit+oddlysatisfying+nextfuckinglevel+travel+minecraft+whatcouldgowrong+mademesmile+animalsbeingderps+animalsbeingbros+tattoos+gardening+beamazed+trippinthroughtime+bikinibottomtwitter+rarepuppers+starterpacks+cars+eyebleach+kidsarefuckingstupid+makeupaddiction+holup+crappydesign+deepintoyoutube+nasa+camping+wellthatsucks+dnd+diwhy+frugal+dogs+marvelmemes+solotravel+youseeingthisshit+fantasy+programmerhumor+natureismetal+terriblefacebookmemes+boomerhumor+somethingimade+shitposting+wallpaper+softwaregore+catastrophicfailure+madlads+comedyheaven+watches+thatsinsane+iamverysmart+niceguys+forbiddensnacks+oddlyspecific+boneappletea').hot(limit=500)

for post in filter(lambda x: reg.search(x.url), top_post):
    data = {}
    data["image"] = post.url
    data["subreddit"] = post.subreddit.display_name
    data["title"] = post.title
    if data not in d:
        posturl_list.append(data)

print(posturl_list)

new_data = d + posturl_list
with open('urls.json', 'w') as f:
    json.dump(new_data, f)
