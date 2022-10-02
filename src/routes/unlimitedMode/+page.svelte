<script>
	// import image from
	import Darkmode from '.././darkmode.svelte';
	import GuessBox from '.././guess_box.svelte';
	import SubList from '.././subList.svelte';
	import TestHeader from '.././testHeader.svelte';
	import UnlimitedMode from './unlimitedMode.svelte';
</script>

<!-- <TestHeader class="row" /> -->
<!-- <div class="row">
	<h1>RedditGuesser</h1>
	<div class="spacer" />
	<Darkmode />
</div> -->

<section class="boxes">
	<div>
		<h1>Unlimited Mode</h1>
		<UnlimitedMode />
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
	/* .togglebutton {
		display: flex;

		justify-content: end;
	} */
	.spacer {
		flex: 999;
	}
	.row {
		display: flex;
		align-content: center;
	}
	h1 {
		/* display: flex;
		flex-direction: row; */
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
