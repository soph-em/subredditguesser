Work in progress.

Reddit guesser similar to geoguessr - displays image for the user to then guess which subreddit it was obtained from.

Data from python script:

```
import praw
import json
import re
reg = re.compile(r".*((\.png)|(\.jpg))")

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",

)
reddit.read_only = True

posturl_list = []

top_post = reddit.subreddit(
    'memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+foodporn+historyporn+wallpapers+earthport+abandonedporn+liminalspaces+carporn+mapporn+perfecttiming+tumblr+itookapicture+skyporn+astrophotography+spaceporn+cosyplaces+photography').hot(limit=12)
for post in filter(lambda x: reg.search(x.url), top_post):
    data = {}
    data["image"] = post.url
    data["subreddit"] = post.subreddit.display_name
    data["title"] = post.title
    posturl_list.append(data)


print(posturl_list)

json.dumps(posturl_list)
with open('urls.json', 'r', encoding="utf-8") as f:
    d = json.load(f)

new_data = d + posturl_list
with open('urls.json', 'w') as f:
    json.dump(new_data, f)
```
