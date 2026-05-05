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

		<div class="reveal flex flex-wrap gap-4" style="transition-delay: 300ms;">
			<a href="mailto:{meta.email}" class="btn-green">Say Hello</a>
			<a
				href={meta.github}
				target="_blank"
				rel="noopener noreferrer"
				class="btn-green"
				style="border-color: transparent; color: #a8b2d8;"
			>
				GitHub →
			</a>
			<a
				href={meta.linkedin}
				target="_blank"
				rel="noopener noreferrer"
				class="btn-green"
				style="border-color: transparent; color: #a8b2d8;"
			>
				LinkedIn →
			</a>
		</div>

		<p class="reveal mt-16 font-mono text-xs text-slate" style="transition-delay: 400ms;">
			Designed & built by Kridtin Chawalratikool
		</p>
	</div>
</section>
