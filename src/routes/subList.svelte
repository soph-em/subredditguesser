<script lang="ts">
	const datalist =
		'tinder+news+pcmasterrace+damnthatsinteresting+leagueoflegends+whatcouldgowrong+facepalm+gaming+politics+therewasanattempt+unexpected+movies+dankmemes+buildapc+meirl+wtf+pokemon+minecraft+todayilearned+europe+anime+pcgaming+dota2+lifeprotips+techsupport+mildlyvandalised+dataisbeautiful+cozyplaces+funnymemes+wholesomememes+mademesmile+memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+wallpapers+liminalspaces+perfecttiming+tumblr+itookapicture+astrophotography+photography+science+outoftheloop+animemes+nottheonion+cats+selfawarewolves+justrolledintotheshop+cursedcomments+lifehacks+homeimprovements+whatisthisthing+comics+art+meme+blursedimages+thathappened+startledcats+worldnews+food+diy+books+space+gadgets+upliftingnews+getmotivated+history+philosophy+television+technology+fitness+oddlysatisfying+travel+animalsbeingderps+animalsbeingbros+tattoos+gardening+beamazed+trippinthroughtime+bikinibottomtwitter+rarepuppers+starterpacks+cars+eyebleach+makeupaddiction+holup+crappydesign+deepintoyoutube+nasa+camping+wellthatsucks+dnd+diwhy+frugal+dogs+marvelmemes+solotravel+fantasy+programmerhumor+natureismetal+terriblefacebookmemes+somethingimade+wallpaper+softwaregore+catastrophicfailure+madlads+comedyheaven+thatsinsane+iamverysmart+forbiddensnacks+oddlyspecific+boneappletea';

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
