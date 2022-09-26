<script lang="ts">
	const datalist =
		'funnymemes+meirl+wholesomememes+mademesmile+memes+aww+humansbeingbros+pics+oldschoolcool+catsplayingdnd+funny+adviceanimals+mildlyinteresting+woahdude+foodporn+historyporn+wallpapers+earthporn+abandonedporn+liminalspaces+carporn+mapporn+perfecttiming+tumblr+itookapicture+skyporn+astrophotography+spaceporn+cosyplaces+photography';
	const sublist = datalist.split('+').sort();
	export let guesses: string[];

	// console.log(sublist);
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
	}
	ul {
		/* border: 15px solid rgb(255, 255, 255); */
		/* border-bottom: 25px solid rgb(255, 255, 255); */
		/* box-shadow: 9px 7px 5px 0px #a799b5; */
		/* background-color: rgb(255, 255, 255); */
	}
	.strike {
		text-decoration: line-through;
	}
</style>
