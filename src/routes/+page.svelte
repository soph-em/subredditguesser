<script>
	// import image from
	import '../app.css';
	import GuessBox from './guess_box.svelte';
</script>

<h1>RedditGuesser</h1>

<section class="boxes">
	<div>
		<GuessBox />
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
	</div>
</section>

<style>
	.boxes {
		max-width: fit-content;
	}

	h1 {
		font-family: 'JetBrains Mono', monospace;
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
</style>
