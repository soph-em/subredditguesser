<script>
	// import image from
	import '../app.css';
	import myJson from 'C:/Users/sophi/Documents/Coding Moments/urls.json';

	let guess = '';
	let answer = 'tumblr';

	function correct() {
		if (guess == answer) {
			alert('Correct');
		} else alert('Incorrect');
	}
	console.log(myJson);
</script>

<h1>RedditGuesser</h1>

<section class="boxes">
	<div>
		<!-- <div class="row">
			<div class="column">
				<div class="blue-column">Column One</div>
			</div>
			<div class="column">
				<div class="green-column">Some Text in Column Two</div>
			</div>
			<div class="column">
				<div>Column Three</div>
			</div>
            
		</div> -->
		<img src="https://i.redd.it/yigtauq1hkp91.png" alt="Reddit" />
		<label for="guess">/r/</label>
		<input id="guess" bind:value={guess} placeholder="Your guess" />
		<button type="button" on:click={correct}>Click me!</button>
	</div>
</section>

<style>
	.boxes {
		display: flex;
		flex-direction: column;
		font-size: large;
		font-weight: bold;
	}

	/* .row {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		width: 100%;
	}

	.column {
		display: flex;
		flex-direction: column;
		flex-basis: 100%;
		flex: 2;
	} */
	img {
		border: 15px solid rgb(255, 255, 255);
		box-shadow: 9px 7px 5px 0px #a799b5;
	}
</style>
