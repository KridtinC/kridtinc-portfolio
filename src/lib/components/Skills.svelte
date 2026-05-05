<script lang="ts">
	import { skills } from '$lib/data';
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

<section id="skills" class="px-6 py-24 md:px-12 lg:px-16" bind:this={el}>
	<h2 class="section-heading reveal"><span>Skills</span></h2>

	<div class="max-w-xl space-y-8">
		<div class="reveal" style="transition-delay: 80ms;">
			<p class="font-mono text-xs text-green mb-3 tracking-widest uppercase flex items-center gap-2">
				<span>AI & Engineering</span>
			</p>
			<div class="flex flex-wrap gap-2">
				{#each skills.ai as skill}
					<span
						class="rounded px-3 py-1 font-mono text-xs text-green border border-green/30 bg-green/5 hover:bg-green/10 transition-colors duration-200 cursor-default"
					>
						{skill}
					</span>
				{/each}
			</div>
		</div>

		<div class="reveal" style="transition-delay: 160ms;">
			<p class="font-mono text-xs text-slate-light mb-3 tracking-widest uppercase">Experienced</p>
			<div class="flex flex-wrap gap-2">
				{#each skills.experienced as skill}
					<span
						class="rounded px-3 py-1 font-mono text-xs text-slate-light border border-navy-lighter bg-navy-light hover:border-green/40 hover:text-green transition-colors duration-200 cursor-default"
					>
						{skill}
					</span>
				{/each}
			</div>
		</div>

		<div class="reveal" style="transition-delay: 240ms;">
			<p class="font-mono text-xs text-slate mb-3 tracking-widest uppercase">Familiar</p>
			<div class="flex flex-wrap gap-2">
				{#each skills.familiar as skill}
					<span
						class="rounded px-3 py-1 font-mono text-xs text-slate border border-navy-lighter/50 bg-navy-light/50 hover:border-slate/40 hover:text-slate-light transition-colors duration-200 cursor-default"
					>
						{skill}
					</span>
				{/each}
			</div>
		</div>
	</div>
</section>
