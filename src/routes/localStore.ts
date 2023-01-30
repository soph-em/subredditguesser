import { browser } from '$app/environment';
import { writable } from 'svelte/store';

const store = <T>(key: string, fallbackValue: T) => {
	const s = writable<T>(
		browser && window.localStorage.getItem(key)
			? JSON.parse(window.localStorage.getItem(key)!)
			: fallbackValue
	);

	s.subscribe((value) => {
		console.log(`SUBSCRIBED: ${key}`);
		if (browser) {
			console.log(`SET ITEM: ${key} = ${value}`);

			window.localStorage.setItem(key, JSON.stringify(value));
		}
	});
	return s;
};

export default store;
