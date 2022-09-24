<script>
	import { object_without_properties } from 'svelte/internal';
	import data from 'C:/Users/sophi/Documents/Coding Moments/RedditScraper/urls.json';
	let guess = '';
	let count = 0;
	let current;
	$: current = data[Object.keys(data)[count]];

	function correct() {
		if (guess == current['subreddit']) {
			rightGuess = true;
			setTimeout(() => (rightGuess = false), 1000);
			function myCount() {
				count += 1;
			}
			setTimeout(myCount, 1200);
			setTimeout((guess = ''), 1200);
		} else {
			wrongGuess = true;
			setTimeout(() => (wrongGuess = false), 500);
			guess = '';
		}
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
	<div class="border" class:wrongGuess class:rightGuess>
		<div>
			{#if hintTitle}
				<p>{current['title']}</p>
			{:else}
				<button class="button-30 buttonhint" type="button" on:click={hint}>Click for hint</button>
			{/if}
		</div>
		<div>
			<img src={current['image']} alt="Reddit" />
		</div>
		<div class="flex-centre">
			<label for="guess">/r/</label>
			<input style="border:none" id="guess" bind:value={guess} placeholder="Your guess" />
		</div>
		<button type="button" class="button-40 bottombutton" on:click={correct}>Submit guess</button>
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

	.border {
		border: 15px solid rgb(255, 255, 255);
		border-bottom: 25px solid rgb(255, 255, 255);
		box-shadow: 9px 7px 5px 0px #a799b5;
		margin: 50px;
		background: white;
		transition: all 300ms;
	}

	img {
		max-height: 500px;
		max-width: 500px;
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
		box-shadow: 0px 0px 2px 2px #a799b5;
	}
	label {
		font-weight: lighter;
		font-size: x-large;
		text-align: right;
	}
	.bottombutton {
		align: center;
		margin-top: 20px;
	}

	/* CSS */
	.button-40 {
		background-color: #111827;
		border: 1px solid transparent;
		border-radius: 0.75rem;
		box-sizing: border-box;
		color: #ffffff;
		cursor: pointer;
		flex: 0 0 auto;
		font-family: 'JetBrains Mono', monospace;
		font-size: 1.125rem;
		font-weight: 600;
		line-height: 1.5rem;
		padding: 0.75rem 1.2rem;
		text-align: center;
		text-decoration: none #6b7280 solid;
		text-decoration-thickness: auto;
		transition-duration: 0.2s;
		transition-property: background-color, border-color, color, fill, stroke;
		transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
		user-select: none;
		-webkit-user-select: none;
		touch-action: manipulation;
		width: auto;
	}

	.button-40:hover {
		background-color: #374151;
	}

	.button-40:focus {
		box-shadow: none;
		outline: 2px solid transparent;
		outline-offset: 2px;
	}

	@media (min-width: 768px) {
		.button-40 {
			padding: 0.75rem 1.5rem;
		}
	}

	/* CSS */
	.button-30 {
		align-items: center;
		appearance: none;
		background-color: #fcfcfd;
		border-radius: 4px;
		border-width: 0;
		box-shadow: rgba(45, 35, 66, 0.4) 0 2px 4px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px,
			#d6d6e7 0 -3px 0 inset;
		box-sizing: border-box;
		color: #36395a;
		cursor: pointer;
		display: inline-flex;
		font-family: 'JetBrains Mono', monospace;
		height: 48px;
		justify-content: center;
		line-height: 1;
		list-style: none;
		overflow: hidden;
		padding-left: 16px;
		padding-right: 16px;
		position: relative;
		text-align: left;
		text-decoration: none;
		transition: box-shadow 0.15s, transform 0.15s;
		user-select: none;
		-webkit-user-select: none;
		touch-action: manipulation;
		white-space: nowrap;
		will-change: box-shadow, transform;
		font-size: 18px;
	}

	.button-30:focus {
		box-shadow: #d6d6e7 0 0 0 1.5px inset, rgba(45, 35, 66, 0.4) 0 2px 4px,
			rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #d6d6e7 0 -3px 0 inset;
	}

	.button-30:hover {
		box-shadow: rgba(45, 35, 66, 0.4) 0 4px 8px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px,
			#d6d6e7 0 -3px 0 inset;
		transform: translateY(-2px);
	}

	.button-30:active {
		box-shadow: #d6d6e7 0 3px 7px inset;
		transform: translateY(2px);
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

	.buttonhint {
		margin-bottom: 15px;
	}

	
</style>
