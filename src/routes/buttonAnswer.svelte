<button class="button-40 bottombutton" on:click><slot /></button>

<style>
	.button-40 {
		background-color: #111827;
		border: 1px solid transparent;
		border-radius: 0.75rem;
		box-sizing: border-box;
		color: #ffffff;
		cursor: pointer;
		flex: 0 0 auto;
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
		max-width: 200px;
		align-items: center;
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
	.bottombutton {
		/* align: center; */
		margin-top: 20px;
		margin-bottom: 20px;
	}
</style>
