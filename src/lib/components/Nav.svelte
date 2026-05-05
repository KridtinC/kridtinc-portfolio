<script lang="ts">
	import { onMount } from 'svelte';
	import { activeSection, mobileMenuOpen } from '$lib/stores';
	import { meta } from '$lib/data';

	const navLinks = [
		{ id: 'about', label: 'About' },
		{ id: 'experience', label: 'Experience' },
		{ id: 'skills', label: 'Skills' },
		{ id: 'work', label: 'Work' },
		{ id: 'contact', label: 'Contact' }
	];

	let currentSection = $state('hero');

	const unsubscribe = activeSection.subscribe((v) => (currentSection = v));

	onMount(() => {
		return unsubscribe;
	});

	function scrollTo(id: string) {
		document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
		mobileMenuOpen.set(false);
	}

	let menuOpen = $state(false);

	function toggleMenu() {
		menuOpen = !menuOpen;
	}
</script>

<!-- Mobile top bar -->
<div
	class="fixed top-0 right-0 left-0 z-50 flex items-center justify-between px-6 py-5 lg:hidden"
	style="background: rgba(15,15,15,0.9); backdrop-filter: blur(8px);"
>
	<button
		class="font-mono text-sm text-green-400 tracking-widest"
		onclick={() => scrollTo('hero')}
	>
		KC
	</button>
	<button
		class="flex flex-col gap-1.5 p-1"
		onclick={toggleMenu}
		aria-label="Toggle menu"
	>
		<span
			class="block h-px w-6 bg-slate-300 transition-transform duration-300"
			class:rotate-45={menuOpen}
			class:translate-y-[10px]={menuOpen}
		></span>
		<span
			class="block h-px w-6 bg-slate-300 transition-opacity duration-300"
			class:opacity-0={menuOpen}
		></span>
		<span
			class="block h-px w-6 bg-slate-300 transition-transform duration-300"
			class:-rotate-45={menuOpen}
			class:-translate-y-[10px]={menuOpen}
		></span>
	</button>
</div>

<!-- Mobile menu overlay -->
{#if menuOpen}
	<div
		class="fixed inset-0 z-40 flex flex-col items-center justify-center gap-8 lg:hidden"
		style="background: rgba(15,15,15,0.97); backdrop-filter: blur(12px);"
	>
		{#each navLinks as link}
			<button
				class="flex flex-col items-center gap-1 text-slate-light hover:text-green transition-colors"
				onclick={() => scrollTo(link.id)}
			>
				<span class="font-mono text-xs text-green">0{navLinks.indexOf(link) + 1}.</span>
				<span class="text-xl font-semibold text-offwhite">{link.label}</span>
			</button>
		{/each}
		<a href="mailto:{meta.email}" class="btn-green mt-4">Get In Touch</a>
	</div>
{/if}

<!-- Desktop left sidebar -->
<aside
	class="fixed top-0 left-0 z-30 hidden h-screen w-[45%] max-w-[480px] xl:w-[40%] flex-col justify-between px-16 py-24 lg:flex"
>
	<!-- Top: name + tagline + nav -->
	<div>
		<a
			href="#hero"
			class="block mb-3"
			onclick={(e) => { e.preventDefault(); scrollTo('hero'); }}
		>
			<h1 class="text-4xl font-bold text-offwhite leading-tight tracking-tight">
				Kridtin<br />Chawalratikool
			</h1>
		</a>
		<p class="font-mono text-sm text-green mb-1">{meta.role}</p>
		<p class="text-slate text-sm leading-relaxed max-w-xs mb-12">
			Building scalable systems and end-to-end applications with Go & TypeScript.
		</p>

		<nav class="flex flex-col gap-2">
			{#each navLinks as link, i}
				<button
					class="group flex items-center gap-4 py-2 text-left transition-all duration-200"
					onclick={() => scrollTo(link.id)}
				>
					<span
						class="h-px transition-all duration-200 {currentSection === link.id
							? 'w-12 bg-offwhite'
							: 'w-6 bg-slate group-hover:w-12 group-hover:bg-slate-light'}"
					></span>
					<span
						class="font-mono text-xs tracking-widest transition-colors {currentSection === link.id
							? 'text-offwhite'
							: 'text-slate group-hover:text-slate-light'}"
					>
						{link.label.toUpperCase()}
					</span>
				</button>
			{/each}
		</nav>
	</div>

	<!-- Bottom: socials -->
	<div class="flex flex-col gap-6">
		<div class="flex items-center gap-5">
			<a
				href={meta.github}
				target="_blank"
				rel="noopener noreferrer"
				class="text-slate hover:text-green transition-colors"
				aria-label="GitHub"
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
					<path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
				</svg>
			</a>
			<a
				href={meta.linkedin}
				target="_blank"
				rel="noopener noreferrer"
				class="text-slate hover:text-green transition-colors"
				aria-label="LinkedIn"
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
					<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
				</svg>
			</a>
			<a
				href="mailto:{meta.email}"
				class="text-slate hover:text-green transition-colors"
				aria-label="Email"
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
				</svg>
			</a>
		</div>
		<p class="font-mono text-xs text-slate">
			{meta.email}
		</p>
	</div>
</aside>
