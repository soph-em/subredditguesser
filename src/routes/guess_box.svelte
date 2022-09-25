<script>
	import { object_without_properties } from 'svelte/internal';
	import ButtonAnswer from './buttonAnswer.svelte';
	import ButtonHint from './buttonHint.svelte';
	import data from 'C:/Users/sophi/Documents/Coding Moments/RedditScraper/urls.json';

	let guess = '';
	let count = 0;
	let current;
	$: current = data[Object.keys(data)[count]];

	function correct() {
		if (guess.toLowerCase().trim() == current['subreddit'].toLowerCase()) {
			rightGuess = true;
			hintTitle = true;
			// setTimeout(() => (rightGuess = false), 1000);

			setTimeout(myCount, 1200);
		} else {
			wrongGuess = true;
			setTimeout(() => (wrongGuess = false), 500);
			guess = '';
		}
	}
	function next() {
		count += 1;
		guess = '';
		rightGuess = false;
		hintTitle = false;
	}
	function hint() {
		hintTitle = true;
		console.log(current['title']);
	}
	// console.log(data);
	let wrongGuess = false;
	let rightGuess = false;
	let hintTitle = false;
</script>

<section>
	<div class="fixflex border" class:wrongGuess class:rightGuess>
		<div>
			{#if hintTitle}
				<p>{current['title']}</p>
			{:else}
				<!-- COPY THIS -->
				<ButtonHint on:click={hint}>Click for hint</ButtonHint>
				<!-- <button class="button-30 buttonhint" type="button" >Click for hint</button> -->
			{/if}
		</div>
		<div>
			<img src={current['image']} alt="Reddit" />
		</div>
		<div class="flex-centre centreline">
			<label for="guess">/r/</label>
			<input id="guess" bind:value={guess} placeholder="Your guess" />
		</div>

		{#if rightGuess}
			<ButtonAnswer on:click={next}>Next</ButtonAnswer>
		{:else}
			<ButtonAnswer on:click={correct}>Submit guess</ButtonAnswer>
		{/if}
	</div>

	<!-- <p>{current['subreddit']}</p> -->
</section>

<style>
	section {
		display: flex;
		flex-direction: column;

		align-items: center;
		justify-content: center;
		text-align: center;
		font-family: 'JetBrains Mono', monospace;
	}

	p {
		display: inline-flex;
		font-family: 'JetBrains Mono', monospace;
		justify-content: center;
		width: 350px;
	}

	.border {
		border: 15px solid rgb(255, 255, 255);
		border-bottom: 25px solid rgb(255, 255, 255);
		box-shadow: 9px 7px 5px 0px #a799b5;
		margin: 50px;
		background: white;
		transition: all 300ms;
	}

	img {
		/* max-height: 500px; */
		max-width: 500px;
		min-width: 350px;
	}

	input {
		font-family: 'JetBrains Mono', monospace;
	}

	.wrongGuess {
		border: 15px solid rgb(176, 35, 0);
		box-shadow: 9px 7px 5px 0px #a799b5;
		background: rgb(176, 35, 0);
		/* opacity: 20%; */
	}

	.rightGuess {
		border: 15px solid rgb(0, 211, 63);
		box-shadow: 9px 7px 5px 0px #a799b5;
		background: rgb(0, 211, 63);
	}
	input {
		line-height: 25px;
		/* box-shadow: 0px 0px 2px 2px #a799b5; */
	}
	label {
		font-weight: lighter;
		font-size: x-large;
		text-align: right;
		/* padding-top: 150px; */
	}

	/* .flex-centre > * {
		align-self: center;
		justify-self: center;
		align-content: center;
	} */
	.flex-centre {
		/* display: flex; */
		margin: auto;
		margin-top: 15px;
	}

	.centreline {
		display: flex;
		align-items: center;
		flex-direction: row;
	}

	.fixflex {
		display: flex;
		flex-direction: column;
	}
</style>
