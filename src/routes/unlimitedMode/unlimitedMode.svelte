<script lang="ts">
	// console.log(data);
	import { each, object_without_properties } from 'svelte/internal';
	import ButtonAnswer from '.././buttonAnswer.svelte';
	import ButtonHint from '.././buttonHint.svelte';
	import ButtonSkip from '.././buttonSkip.svelte';
	import SubList from '.././subList.svelte';
	import data from 'C:/Users/sophi/Documents/Coding Moments/RedditScraper/urls.json';
	let userGuesses: string[] = [];
	let guess = '';
	let count = 200;
	let current;
	$: current = data[Object.keys(data)[count]];

	function correct() {
		if (guess.toLowerCase().trim() == current['subreddit'].toLowerCase()) {
			rightGuess = true;
			hintTitle = true;

			userGuesses = [];
		} else {
			wrongGuess = true;

			setTimeout(() => (wrongGuess = false), 500);
			saveInput(guess);
			guess = '';
		}
	}
	function next() {
		count += 1;
		guess = '';
		rightGuess = false;
		hintTitle = false;
		userGuesses = [];
	}
	function hint() {
		hintTitle = true;
		hintpadding = false;
		console.log(current['title']);
	}

	const saveInput = (guess) => {
		userGuesses = [...userGuesses, guess];
		console.log(userGuesses);
	};

	let wrongGuess = false;
	let rightGuess = false;
	let hintTitle = false;
	let hintpadding = true;
</script>

<section class="sidebar section.dark">
	<div class="row border" class:wrongGuess class:rightGuess>
		<div class="column">
			<div class="hintwidth flex-centre">
				{#if hintTitle}
					<div class="titlepadding">
						<p>{current['title']}</p>
					</div>
				{:else}
					<div class="hintpadding">
						<ButtonHint on:click={hint}>Click for hint</ButtonHint>
					</div>
					<!-- <div class="hintbutton">
						<ButtonAnswer on:click={hint}>Click for hint</ButtonAnswer>
					</div> -->
					<!-- <button class="button-30 buttonhint" type="button" >Click for hint</button> -->
				{/if}
			</div>
			<div class="constrainImage">
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
			<div class="hintwidth flex-centre">
				<ButtonSkip on:click={next}>Skip</ButtonSkip>
			</div>
		</div>

		<div class="column scroller">
			<SubList guesses={userGuesses} />
		</div>
	</div>

	<!-- <p>{current['subreddit']}</p> -->
</section>

<style>
	.hintpadding {
		padding-top: 20px;
		padding-bottom: 20px;
	}
	.titlepadding {
		padding-top: 10px;
		padding-bottom: 20px;
	}
	section {
		display: flex;
		flex-direction: column;
		flex-direction: row;

		align-items: center;
		justify-content: center;
		text-align: center;
		font-family: 'Noto Sans', monospace;
	}

	p {
		display: inline-flex;
		font-family: 'Noto Sans', monospace;
		justify-content: center;
		/* width: 350px;
		max-height: 900px; */
	}

	img {
		max-width: 500px;
		max-height: 400px;
	}

	input {
		line-height: 25px;
		font-family: 'Noto Sans', monospace;
		/* box-shadow: 0px 0px 2px 2px #a799b5; */
	}
	label {
		font-weight: lighter;
		font-size: x-large;
		text-align: right;
		/* padding-top: 150px; */
	}

	.column {
		display: flex;
		flex-direction: column;
		flex-basis: 100%;
		flex: 1;
	}

	.row {
		display: flex;
		flex-direction: row;
		/* width: 50%; */
	}
	.constrainImage {
		max-width: 100vh;
		max-height: 100%;
		max-height: 500px;
	}
	.hintwidth {
		width: 200px;
	}

	.sidebar {
		display: flex;
		align-self: right;
		justify-content: right;
		justify-self: right;
		flex-direction: row;
		align-items: flex-start;
	}

	.border {
		border: 15px solid rgb(255, 255, 255);
		border-bottom: 15px solid rgb(255, 255, 255);
		box-shadow: 9px 7px 5px 0px #a799b5;
		margin: 50px;
		background: white;
		transition: all 300ms;
	}

	.wrongGuess {
		border: 15px solid rgb(176, 35, 0);
		box-shadow: 9px 7px 5px 0px #a799b5;
		background: rgb(176, 35, 0);
		margin: 50px;
		/* opacity: 20%; */
	}

	.rightGuess {
		border: 15px solid rgb(0, 211, 63);
		box-shadow: 9px 7px 5px 0px #a799b5;
		background: rgb(0, 211, 63);
		margin: 50px;
	}

	/* .flex-centre > * {
		align-self: center;
		justify-self: center;
		align-content: center;
	} */
	.flex-centre {
		/* display: flex;
		margin: auto;
		margin-top: 15px; */
		align-self: center;
		overflow: hidden;
		/* padding-top: 20px; */
	}

	.centreline {
		display: flex;
		align-items: center;
		flex-direction: row;
		padding-top: 15px;
	}

	/* SCROLLBAR */
	.scroller {
		width: 250px;
		max-height: 500px;
		overflow-y: scroll;
		padding-left: 20px;
		scrollbar-width: thin;
	}
	/* scrollbar firefox */
	* {
		scrollbar-width: auto;
		scrollbar-color: #0047b1;
	}

	/* scrollbar Chrome, Edge, and Safari */
	*::-webkit-scrollbar {
		width: 16px;
	}

	*::-webkit-scrollbar-track {
	}

	*::-webkit-scrollbar-thumb {
		background-color: #00183b;
		border-radius: 10px;
		border: 3px solid;
	}

	::-webkit-scrollbar-corner {
		background-color: transparent;
	}
</style>
