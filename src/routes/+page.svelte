<script>
	import Darkmode from './darkmode.svelte';
	import GuessBox from './guess_box.svelte';
	import SubList from './subList.svelte';
	import TestHeader from './testHeader.svelte';
</script>

<section class="boxes">
	<div class="content">
		<GuessBox />
	</div>
</section>

<style>
	.content {
		width: 100%;
		display: flex;
		justify-content: center;
	}
</style>
