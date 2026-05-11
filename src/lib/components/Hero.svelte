<script lang="ts">
	import { onMount } from 'svelte';
	import { meta } from '$lib/data';

	let heroEl: HTMLElement;
	let mouseX = $state(0);
	let mouseY = $state(0);

	function handleMouseMove(e: MouseEvent) {
		const rect = heroEl.getBoundingClientRect();
		mouseX = e.clientX - rect.left;
		mouseY = e.clientY - rect.top;
	}

	function scrollTo(id: string) {
		document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
	}

	let visible = $state(false);
	onMount(() => {
		setTimeout(() => (visible = true), 100);
	});
</script>

<section
	id="hero"
	role="banner"
	bind:this={heroEl}
	onmousemove={handleMouseMove}
	class="relative flex min-h-screen flex-col px-6 pt-24 pb-10 md:px-12 lg:px-16 overflow-hidden"
>
	<!-- Cursor glow -->
	<div
		class="pointer-events-none absolute inset-0 transition-opacity duration-500"
		style="background: radial-gradient(400px at {mouseX}px {mouseY}px, rgba(249,115,22,0.06), transparent 70%);"
	></div>

	<!-- Main content — grows to fill, vertically centered -->
	<div class="relative z-10 flex flex-1 flex-col justify-center max-w-xl">
		<p
			class="mb-5 font-mono text-sm text-green transition-all duration-700 {visible
				? 'opacity-100 translate-y-0'
				: 'opacity-0 translate-y-4'}"
			style="transition-delay: 100ms;"
		>
			Hi, my name is
		</p>

		<h1
			class="mb-3 text-5xl font-bold leading-tight text-offwhite md:text-6xl transition-all duration-700 {visible
				? 'opacity-100 translate-y-0'
				: 'opacity-0 translate-y-4'}"
			style="transition-delay: 200ms;"
		>
			{meta.name}.
		</h1>

		<h2
			class="mb-6 text-4xl font-bold leading-tight text-slate md:text-5xl transition-all duration-700 {visible
				? 'opacity-100 translate-y-0'
				: 'opacity-0 translate-y-4'}"
			style="transition-delay: 300ms;"
		>
			I build things for the web.
		</h2>

		<p
			class="mb-10 max-w-md leading-relaxed text-slate transition-all duration-700 {visible
				? 'opacity-100 translate-y-0'
				: 'opacity-0 translate-y-4'}"
			style="transition-delay: 400ms;"
		>
			{meta.bio}
		</p>

		<div
			class="flex flex-wrap gap-4 transition-all duration-700 {visible
				? 'opacity-100 translate-y-0'
				: 'opacity-0 translate-y-4'}"
			style="transition-delay: 500ms;"
		>
			<button class="btn-green" onclick={() => scrollTo('work')}>See my work</button>
			<a href="/resume.pdf" download="Kridtin_Chawalratikool_Resume.pdf" class="btn-green flex items-center gap-2">
				<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>
				</svg>
				Resume
			</a>
			<a href="mailto:{meta.email}" class="btn-green" style="border-color: transparent; color: #aaaaaa;">
				Get in touch →
			</a>
		</div>
	</div>

	<!-- Scroll indicator — always at bottom, never overlapping -->
	<div
		class="relative z-10 flex flex-col items-start gap-2 transition-all duration-700 {visible
			? 'opacity-100'
			: 'opacity-0'}"
		style="transition-delay: 700ms;"
	>
		<span class="font-mono text-xs text-slate/50 tracking-widest">SCROLL</span>
		<div class="h-10 w-px bg-slate/20 relative overflow-hidden">
			<div
				class="absolute left-0 w-full bg-green"
				style="height: 40%; animation: scrollPulse 1.8s ease-in-out infinite;"
			></div>
		</div>
	</div>
</section>

<style>
	@keyframes scrollPulse {
		0%   { top: -40%; opacity: 1; }
		100% { top: 100%; opacity: 0; }
	}
</style>
