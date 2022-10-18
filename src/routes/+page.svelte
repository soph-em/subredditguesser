<script>
	import Darkmode from './darkmode.svelte';
	import GuessBox from './guess_box.svelte';
	import SubList from './subList.svelte';
	import TestHeader from './testHeader.svelte';
</script>

<section class="boxes">
	<div>
		<GuessBox />
	</div>
</section>

<style>
	.boxes {
		max-width: fit-content;
	}
	h1 {
		font-family: 'JetBrains Mono', monospace;
	}
</style>
