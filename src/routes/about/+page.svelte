<script>
	import TestHeader from '../testHeader.svelte';
</script>

<div class="section boxes">
	<div class="column">
		<h1>How to play</h1>
		<p>
			Guess the subreddit the image is from. The list on the right gives options and will strike
			through incorrect items. If you get stuck press the 'Hint' button to reveal the title of the
			post.
		</p>
	</div>
</div>

<style>
	p {
		max-width: 500px;
	}
	.column {
		flex-direction: column;
	}
	.section {
		display: flex;
		flex-direction: column;
		flex-direction: row;

		align-items: center;
		align-self: center;
		justify-content: center;
		text-align: center;
		font-family: 'Noto Sans', monospace;
	}
	.boxes {
		max-width: fit-content;
	}
</style>
