import { writable } from 'svelte/store';

export const activeSection = writable('hero');
export const mobileMenuOpen = writable(false);
