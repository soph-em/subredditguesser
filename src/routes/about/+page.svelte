<script>
	import TestHeader from '../testHeader.svelte';
</script>

<div class="section boxes">
	<div class="column content">
		<h1>How to play</h1>

		<p>
			Guess the subreddit the image is from. The list on the right gives options and will strike
			through incorrect guesses. If you get stuck press the 'Hint' button to reveal the title of the
			post.
			<br />
			<br />
			Play on daily mode to get a daily challenge and share how you did with friends. Play unlimited
			mode to have an unlimited amount of guesses and challenges.
		</p>
	</div>
</div>

<style>
	.column {
		flex-direction: column;
	}
	.content {
		width: 50%;
	}
	.section {
		text-align: center;
		font-family: 'Noto Sans', monospace;
		display: flex;
		justify-content: center;
	}
</style>
