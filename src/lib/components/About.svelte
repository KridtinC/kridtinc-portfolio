<script lang="ts">
	import { meta } from '$lib/data';
	import { onMount } from 'svelte';

	let el: HTMLElement;

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((e) => {
					if (e.isIntersecting) {
						e.target.classList.add('visible');
					}
				});
			},
			{ threshold: 0.1 }
		);
		el.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
		return () => observer.disconnect();
	});
</script>

<section id="about" class="px-6 py-24 md:px-12 lg:px-16" bind:this={el}>
	<h2 class="section-heading reveal"><span>About Me</span></h2>

	<div class="max-w-xl">
		{#each meta.about as para, i}
			<p
				class="reveal mb-5 leading-relaxed text-slate"
				style="transition-delay: {i * 100}ms;"
			>
				{para}
			</p>
		{/each}

		<div class="reveal mt-10 grid grid-cols-2 gap-4" style="transition-delay: 300ms;">
			<div
				class="rounded border border-navy-lighter bg-navy-light p-5 transition-all duration-200 hover:-translate-y-1 hover:border-green/20"
			>
				<p class="font-mono text-2xl font-semibold text-green mb-1">6+</p>
				<p class="text-sm text-slate">Years of experience</p>
			</div>
			<div
				class="rounded border border-navy-lighter bg-navy-light p-5 transition-all duration-200 hover:-translate-y-1 hover:border-green/20"
			>
				<p class="font-mono text-2xl font-semibold text-green mb-1">3.09</p>
				<p class="text-sm text-slate">GPA · Chulalongkorn</p>
			</div>
		</div>

		<div class="reveal mt-8 flex flex-wrap gap-3" style="transition-delay: 400ms;">
			<a
				href="https://github.com/KridtinC"
				target="_blank"
				rel="noopener noreferrer"
				class="btn-green text-xs"
			>
				GitHub →
			</a>
			<a
				href="https://www.linkedin.com/in/kridtinc"
				target="_blank"
				rel="noopener noreferrer"
				class="btn-green text-xs"
			>
				LinkedIn →
			</a>
		</div>
	</div>
</section>
