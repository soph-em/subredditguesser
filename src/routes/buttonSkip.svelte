<!-- HTML !-->
<button class="button-60" on:click><slot /></button>

<style>
	.button-60 {
		align-items: center;
		appearance: none;
		background-color: #fff;
		border: 1px solid #dbdbdb;
		border-radius: 0.375em;
		box-shadow: none;
		box-sizing: border-box;
		color: #363636;
		cursor: pointer;
		font-size: 0.75rem;
		height: 2em;
		width: 10em;
		text-align: center;
		touch-action: manipulation;
		vertical-align: top;
	}

	.button-60:hover {
		border-color: #b5b5b5;
	}
</style>
