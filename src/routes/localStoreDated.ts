import { browser } from '$app/environment';
import { writable } from 'svelte/store';
const date = new Date();
// Reset a Date's time to midnight
date.setHours(0, 0, 0, 0);
// Format a date to YYYY-MM-DD (or any other format)
function padTo2Digits(num: number) {
	return num.toString().padStart(2, '0');
}
function formatDate(date: Date) {
	return [date.getFullYear(), padTo2Digits(date.getMonth() + 1), padTo2Digits(date.getDate())].join(
		'-'
	);
}

const store = <T>(key: string, fallbackValue: T) => {
	const dateTime = formatDate(new Date());
	let isToday = false;
	if (browser) {
		const savedDate = window.localStorage.getItem('localStorageDate');
		isToday = dateTime === savedDate ?? false;
		console.log('is today', isToday, 'date', dateTime, 'saved', savedDate);
	}
	const s = writable<T>(
		browser && window.localStorage.getItem(key) && isToday
			? JSON.parse(window.localStorage.getItem(key)!)
			: fallbackValue
	);

	s.subscribe((value) => {
		console.log(`SUBSCRIBED: ${key}`);
		if (browser) {
			// console.log(`SET ITEM: ${key} = ${value}`);

			window.localStorage.setItem(key, JSON.stringify(value));
			window.localStorage.setItem('localStorageDate', formatDate(new Date()));
		}
	});
	return s;
};

export default store;
