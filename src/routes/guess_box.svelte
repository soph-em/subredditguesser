<script lang="ts">
	import { each, object_without_properties, onMount, text } from 'svelte/internal';
	import ButtonAnswer from './buttonAnswer.svelte';
	import ButtonHint from './buttonHint.svelte';
	import Emojis from './emojis.svelte';
	import SubList from './subList.svelte';
	import data from '$lib/urls.json';
	import localStore from './localStore';
	import localStoreDated from './localStoreDated';
	let userGuesses: string[] = [];
	let guess = '';
	let imageCount = 0;
	let current;
	let guesscount = 0;
	let wrongGuess = false;
	let rightGuess = localStoreDated('correct', false);
	// let wrongGuess = localStoreDated('incorrect', false);
	let lastGuess = localStoreDated('incorrect', false);
	// let lastGuess = false;
	let hintTitle = false;
	let hintpadding = true;
	let displayEmojis = false;
	let scoreDiv;
	let emojimodal;
	let dateTime = localStoreDated('date', '');
	let emojiStore = localStoreDated('score', '');
	type Emoji = { numIncorrect: number; correct: boolean; usedHint: boolean; last: boolean };
	let emojisAll = localStore('emojis', [] as Emoji[]);
	// console.log(emojisAll);
	// console.log($emojisAll);

	// displays modal after daily 10 guesses/correct guess
	onMount(() => {
		if ($rightGuess || $lastGuess) {
			emojimodal.showModal();
		}
	});
	// date formatting function - lines 37-53
	const date = new Date();

	date.setHours(0, 0, 0, 0);

	// ----------------------------------------------------

	function padTo2Digits(num) {
		return num.toString().padStart(2, '0');
	}

	function formatDate(date) {
		return [
			date.getFullYear(),
			padTo2Digits(date.getMonth() + 1),
			padTo2Digits(date.getDate())
		].join('-');
	}

	$: current = data[Object.keys(data)[imageCount]];

	//function that limits user to ten guesses
	function limit() {
		if (guesscount == 10 && !$rightGuess) {
			$lastGuess = true;
			hintTitle = true;

			guess = current['subreddit'];
			$dateTime = formatDate(new Date());
			userGuesses = [];
			guessLimit();
			$emojisAll = [
				{
					numIncorrect: guesscount,
					correct: $rightGuess,
					usedHint: hintTitle,
					last: $lastGuess
				}
			];
		}
	}

	function guessLimit() {
		if (imageCount >= 0) {
			emojimodal.showModal();
		}
	}
	//changes state when user guesses correctly
	function correct() {
		if (guess.toLowerCase().trim() == current['subreddit'].toLowerCase()) {
			$rightGuess = true;
			$dateTime = formatDate(new Date());
			userGuesses = [];
			guessLimit();
			$emojisAll = [
				{
					numIncorrect: guesscount + 1,
					correct: $rightGuess,
					usedHint: hintTitle,
					last: $lastGuess
				}
			];
			hintTitle = true;
		} else {
			wrongGuess = true;
			setTimeout(() => (wrongGuess = false), 500);
			saveInput(guess);
			guess = '';
		}
		guesscount += 1;
		limit();
	}
	//changes state when user clicks next button - main use in unlimited mode, possibly unnecessary in daily mode
	function next() {
		guess = '';
		$rightGuess = false;
		hintTitle = false;
		$lastGuess = false;
		userGuesses = [];
		guesscount = 0;
	}
	//changes state when user clicks 'hint' button
	function hint() {
		hintTitle = true;
		hintpadding = false;
	}

	const saveInput = (guess) => {
		userGuesses = [...userGuesses, guess];
	};
</script>

<dialog bind:this={emojimodal}>
	<p class="modalHeader">Daily Challenge Score</p>
	<div class=" innerdialog column">
		<p class="modalSubreddit">/r/{current['subreddit']}</p>
		<div class="emojiSection" bind:this={scoreDiv}>
			{#each $emojisAll as emoji}
				<Emojis {...emoji} />
			{/each}
		</div>
		<div class="modalButtons">
			<button
				class="button"
				on:click={() => {
					const str = scoreDiv.innerText;

					const strDate = str + ' - ' + formatDate(new Date()) + '\n' + 'redditguesser.pages.dev/';
					navigator.clipboard.writeText(strDate);
				}}>Copy</button
			>
			<a class="button" href="/unlimitedMode">Unlimited Mode</a>

			<button class="button" on:click={() => emojimodal.close()}>Close</button>
		</div>
	</div>
</dialog>

<section class="sidebar section.dark">
	<div
		class="row border"
		class:wrongGuess
		class:rightGuess={$rightGuess}
		class:lastGuess={$lastGuess}
	>
		<div class="column">
			<h1>Daily Challenge</h1>
			<!-- <Emojis numIncorrect={guesscount} correct={rightGuess} usedHint={hintTitle} /> -->
			<div class="hintwidth flex-centre">
				{#if hintTitle}
					<div class="titlepadding">
						<p>{current['title']}</p>
					</div>
				{:else}
					<div class="hintpadding">
						<ButtonHint on:click={hint}>Click for hint</ButtonHint>
					</div>
				{/if}
			</div>
			<div class="constrainImage">
				<img src={current['image']} alt="Reddit" />
			</div>
			<div class="flex-centre centreline">
				<label for="guess">/r/</label>
				<input id="guess" bind:value={guess} placeholder="Your guess" />
			</div>
			<div class="flex-centre">
				{#if imageCount <= 1}
					{#if $rightGuess || $lastGuess}
						<!-- <ButtonAnswer on:click={next}>Next</ButtonAnswer> -->
						<p>Come back tomorrow for the next challenge</p>
						<!-- {:else if lastGuess}
						<ButtonAnswer on:click={next}>Next Question</ButtonAnswer> -->
					{:else if !$rightGuess}
						<ButtonAnswer on:click={correct}>Submit guess</ButtonAnswer>
					{/if}
				{/if}
			</div>
		</div>

		<div class="column scroller">
			<SubList guesses={userGuesses} />
		</div>
	</div>
</section>

<style>
	.modalSubreddit {
		font-size: small;
	}
	dialog {
		overflow: none;
		width: fit-content;
	}
	.flex-centre {
		align-self: center;
		overflow: hidden;
	}
	.modalHeader {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.emojiSection {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 5px 0;
		/* font-size: 30px; */
		font-size: small;
		padding-bottom: 15px;
		text-align: center;
		overflow: none;
	}
	.modalButtons {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 0 20px;
	}
	.button {
		padding: 3px;
		margin: 5px;
		/* width: 100px; */
		border-radius: 4px;
		background: rgb(239, 247, 255, 1);
		font-family: 'Noto Sans', sans-serif;
		font-size: 14px;
		cursor: pointer;
		text-align: center;
		/* color: rgb(255, 86, 0, 1); */
		color: rgb(89, 89, 89);
		outline: none;
		font-weight: bold;
		border: 2px solid rgb(187, 221, 255);
		align-self: stretch;
	}
	a {
		text-decoration: none;
	}
	a:hover {
		outline: #00183b;
	}
	.button:hover {
		/* color: rgb(255, 86, 0, 1); */
		border: 2px solid rgb(60, 100, 142);
		background: rgb(110, 183, 255);
		color: white;
	}
	button {
		padding: 3px;
		margin: 5px;
		/* width: 100px; */
		outline: none;
		border: none;
	}
	button:hover {
		outline: black;
	}
	dialog::backdrop {
		background-color: rgba(1, 1, 1, 0.767);
	}
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

		align-items: center;
		justify-content: center;
		text-align: center;
		font-family: 'Noto Sans', monospace;
	}

	p {
		display: inline-flex;
		font-family: 'Noto Sans', monospace;
		justify-content: center;
		margin: 0;
		padding: 5px;
	}

	img {
		max-width: 500px;
		max-height: 500px;
	}

	input {
		line-height: 25px;
		font-family: 'Noto Sans', monospace;
	}
	label {
		font-weight: lighter;
		font-size: x-large;
		text-align: right;
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

	/* .sidebar {
		display: flex;
		align-self: right;
		justify-content: right;
		justify-self: right;
		flex-direction: row;
		align-items: flex-start;
	} */

	.border {
		border: 15px solid rgb(255, 255, 255);
		border-bottom: 15px solid rgb(255, 255, 255);
		box-shadow: 9px 7px 5px 0px #77717c;
		margin: 50px;
		background: white;
		transition: all 300ms;
	}

	.wrongGuess {
		border: 15px solid rgb(176, 35, 0);
		box-shadow: 9px 7px 5px 0px #77717c;
		background: rgb(176, 35, 0);
		margin: 50px;
		/* opacity: 20%; */
	}

	.rightGuess {
		border: 15px solid rgb(0, 211, 63);
		box-shadow: 9px 7px 5px 0px #77717c;
		background: rgb(0, 211, 63);
		margin: 50px;
	}

	.lastGuess {
		border: 15px solid rgb(89, 89, 89);
		box-shadow: 9px 7px 5px 0px #77717c;
		background: rgb(89, 89, 89);
		margin: 50px;
	}

	.flex-centre {
		align-self: center;
		overflow: hidden;
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

	.innerdialog {
		max-height: 250px;
		width: 200px;
		border: #a799b5;
	}
</style>
