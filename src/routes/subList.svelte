<script lang="ts">
	const datalist =
		'tinder+interestingasfuck+whitepeopletwitter+antiwork+news+pcmasterrace+damnthatsinteresting+leagueoflegends+whatcouldgowrong+facepalm+gaming+politics+therewasanattempt+wallstreetbets+unexpected+movies+dankmemes+buildapc+meirl+wtf+pokemon+shitposting+leopardsatemyface+minecraft+todayilearned+europe+anime+pcgaming+dota2+lifeprotips+techsupport+blackpeopletwitter+mildlyvandalised+dataisbeautiful+cozyplaces+funnymemes+wholesomememes+mademesmile+memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+foodporn+historyporn+wallpapers+earthporn+abandonedporn+liminalspaces+carporn+mapporn+perfecttiming+tumblr+itookapicture+skyporn+astrophotography+spaceporn+photography+science+outoftheloop+animemes+nottheonion+sadcringe+choosingbeggars+cats+selfawarewolves+justrolledintotheshop+cursedcomments+lifehacks+deuxmoi+homeimprovements+whatisthisthing+comics+art+meme+blursedimages+thathappened+startledcats+oldpeoplefacebook+worldnews+food+diy+books+space+gadgets+upliftingnews+getmotivated+tifu+history+philosophy+television+technology+fitness+natureisfuckinglit+oddlysatisfying+nextfuckinglevel+travel+animalsbeingderps+animalsbeingbros+tattoos+gardening+beamazed+trippinthroughtime+bikinibottomtwitter+rarepuppers+starterpacks+cars+eyebleach+kidsarefuckingstupid+makeupaddiction+holup+crappydesign+deepintoyoutube+nasa+camping+wellthatsucks+dnd+diwhy+frugal+dogs+marvelmemes+solotravel+youseeingthisshit+fantasy+programmerhumor+natureismetal+terriblefacebookmemes+boomerhumor+somethingimade+wallpaper+softwaregore+catastrophicfailure+madlads+comedyheaven+watches+thatsinsane+iamverysmart+niceguys+forbiddensnacks+oddlyspecific+boneappletea';

	const sublist = datalist.split('+').sort();
	export let guesses: string[];
</script>

<ul>
	{#each sublist as item}
		<li class:strike={guesses.includes(item)}>
			{item}
		</li>
	{/each}
</ul>

<style>
	li {
		text-align: left;
		font-size: small;
		list-style: none;
		font: 'Noto Sans';
	}

	.strike {
		text-decoration: line-through;
	}
</style>
