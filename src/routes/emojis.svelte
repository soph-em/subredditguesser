<script>
	let guessEmoji = {
		0: '1️⃣',
		1: '2️⃣',
		2: '3️⃣',
		3: '4️⃣',
		4: '5️⃣',
		5: '6️⃣',
		6: '7️⃣',
		7: '8️⃣',
		8: '9️⃣',
		wrong: '❌',
		guess: '✅',
		right: '🌟'
	};

	export let numIncorrect;
	export let usedHint;
	export let correct;
	export let lastGuess;
	// console.log(numIncorrect);
</script>

<div>
	{#each Array(numIncorrect) as _, index}
		{#if index != numIncorrect - 1}
			{guessEmoji[index]}
		{:else if correct && !usedHint}
			{guessEmoji.right}
		{:else if correct}
			{guessEmoji.guess}
		{:else}
			{guessEmoji.wrong}
		{/if}
	{/each}
</div>
