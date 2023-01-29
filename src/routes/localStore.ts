import { browser } from '$app/environment';
import { writable } from 'svelte/store';

const store = <T>(key: string, fallbackValue: T) => {
	const s = writable<T>(
		browser && window.localStorage.getItem(key)
			? JSON.parse(window.localStorage.getItem(key)!)
			: fallbackValue
	);

	s.subscribe((value) => {
		if (browser) {
			window.localStorage.setItem(key, JSON.stringify(value));
		}
	});
	return s;
};

export default store;
