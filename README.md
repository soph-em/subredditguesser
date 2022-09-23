Work in progress.

Reddit guesser similar to geoguessr - displays image for the user to then guess which subreddit it was obtained from.

Data imported using python script/json:

```
import praw
import json

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",

)
reddit.read_only = True

posturl_list = []

top_post = reddit.subreddit(
    'memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+foodporn+historyporn+wallpapers+earthport+abandonedporn+liminalspaces+carporn+mapporn+perfecttiming+tumblr+itookapicture+skyporn+astrophotography+spaceporn+cosyplaces+photography').hot(limit=12)
for post in top_post:
    data = {}
    if not '.gif' in post.url and not 'v.redd.it' in post.url:
        data["image"] = post.url
        data["subreddit"] = post.subreddit.display_name
        posturl_list.append(data)


print(posturl_list)

json.dumps(posturl_list)
with open('urls.json', 'w', encoding="utf-8") as f:
    json.dump(posturl_list, f, ensure_ascii=False, indent=4)
```
