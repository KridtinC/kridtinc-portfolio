<script lang="ts">
	import { meta } from '$lib/data';
	import { onMount } from 'svelte';

	let el: HTMLElement;

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
			{ threshold: 0.1 }
		);
		el.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
		return () => observer.disconnect();
	});
</script>

<section id="contact" class="px-6 py-24 md:px-12 lg:px-16 pb-32" bind:this={el}>
	<div class="max-w-md">
		<p class="reveal font-mono text-sm text-green mb-3" style="transition-delay: 0ms;">
			04. What's Next?
		</p>
		<h2 class="reveal text-4xl font-bold text-offwhite mb-5" style="transition-delay: 100ms;">
			Get In Touch
		</h2>
		<p class="reveal text-slate leading-relaxed mb-10" style="transition-delay: 200ms;">
			I'm currently open to new opportunities. Whether you have a question, a project in mind, or
			just want to say hi — my inbox is always open.
		</p>

		<div class="reveal flex flex-col gap-3" style="transition-delay: 300ms;">
			<div class="flex flex-wrap gap-3">
				<a href="mailto:{meta.email}" class="btn-green whitespace-nowrap">Say Hello</a>
				<a
					href="/resume.pdf"
					download="Kridtin_Chawalratikool_Resume.pdf"
					class="btn-green whitespace-nowrap inline-flex items-center gap-2"
				>
					<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
						<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>
					</svg>
					Resume
				</a>
			</div>
			<div class="flex gap-3">
				<a
					href={meta.github}
					target="_blank"
					rel="noopener noreferrer"
					class="btn-green whitespace-nowrap"
					style="border-color: transparent; color: #aaaaaa;"
				>
					GitHub →
				</a>
				<a
					href={meta.linkedin}
					target="_blank"
					rel="noopener noreferrer"
					class="btn-green whitespace-nowrap"
					style="border-color: transparent; color: #aaaaaa;"
				>
					LinkedIn →
				</a>
			</div>
		</div>

		<p class="reveal mt-16 font-mono text-xs text-slate" style="transition-delay: 400ms;">
			Designed & built by Kridtin Chawalratikool
		</p>
	</div>
</section>
