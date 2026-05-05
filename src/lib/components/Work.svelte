<script lang="ts">
	import { onMount } from 'svelte';
	import { projects } from '$lib/data';
	import ProkedexDemo from './demos/ProkedexDemo.svelte';
	import CovidDemo from './demos/CovidDemo.svelte';

	let el: HTMLElement;
	let hovered = $state<string | null>(null);
	let expanded = $state<string | null>(null);

	function toggleDemo(id: string) {
		expanded = expanded === id ? null : id;
	}

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
			{ threshold: 0.1 }
		);
		el.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
		return () => observer.disconnect();
	});
</script>

<section id="work" class="px-6 py-24 md:px-12 lg:px-16" bind:this={el}>
	<h2 class="section-heading reveal"><span>Work</span></h2>

	<div class="max-w-2xl">
		{#each projects as project, i}
			<div class="reveal" style="transition-delay: {i * 80}ms;">
				<!-- Row: EK-style -->
				<div
					class="group relative border-t border-navy-lighter last:border-b py-7 transition-all duration-300 cursor-pointer {hovered === project.id && hovered !== expanded ? 'pl-3' : ''}"
					onmouseenter={() => (hovered = project.id)}
					onmouseleave={() => (hovered = null)}
					onclick={() => project.hasDemo && toggleDemo(project.id)}
					role="button"
					tabindex="0"
					onkeydown={(e) => e.key === 'Enter' && project.hasDemo && toggleDemo(project.id)}
					aria-expanded={expanded === project.id}
				>
					<!-- Hover bg -->
					<div
						class="pointer-events-none absolute inset-0 transition-opacity duration-300 rounded {hovered === project.id ? 'opacity-100' : 'opacity-0'}"
						style="background: linear-gradient(90deg, rgba(249,115,22,0.04) 0%, transparent 100%);"
					></div>

					<div class="relative flex items-start justify-between gap-4">
						<!-- Left: number + title -->
						<div class="flex items-baseline gap-4 min-w-0">
							<span
								class="font-mono text-sm shrink-0 transition-colors duration-200 {hovered === project.id ? 'text-green' : 'text-slate/50'}"
							>
								{project.num}
							</span>
							<div class="min-w-0">
								<h3
									class="text-xl font-semibold transition-colors duration-200 leading-tight {hovered === project.id ? 'text-offwhite' : 'text-slate-lightest'}"
								>
									{project.name}
								</h3>
								<p
									class="mt-1.5 text-sm text-slate leading-relaxed transition-all duration-300 {hovered === project.id ? 'text-slate-light' : ''}"
								>
									{project.description}
								</p>
							</div>
						</div>

						<!-- Right: stack + links -->
						<div class="flex flex-col items-end gap-3 shrink-0">
							{#if project.url}
								<a
									href={project.url}
									target="_blank"
									rel="noopener noreferrer"
									onclick={(e) => e.stopPropagation()}
									class="text-slate hover:text-green transition-colors"
									aria-label="View on GitHub"
								>
									<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
										<path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
									</svg>
								</a>
							{/if}
							{#if project.stack.length}
								<div class="flex flex-wrap justify-end gap-1.5">
									{#each project.stack as tech}
										<span class="font-mono text-xs text-slate">{tech}</span>
									{/each}
								</div>
							{/if}
							{#if project.hasDemo}
								<span
									class="font-mono text-xs transition-colors duration-200 flex items-center gap-1 {expanded === project.id ? 'text-green' : 'text-slate/60 group-hover:text-green/70'}"
								>
									{expanded === project.id ? '↑ Close' : '↓ Demo'}
								</span>
							{/if}
						</div>
					</div>
				</div>

				<!-- Demo panel -->
				{#if expanded === project.id && project.hasDemo}
					<div
						class="mb-4 overflow-hidden rounded-lg animate-[demoSlide_0.35s_cubic-bezier(0.16,1,0.3,1)_forwards]"
					>
						{#if project.demoType === 'prokedex'}
							<ProkedexDemo />
						{:else if project.demoType === 'covid'}
							<CovidDemo />
						{/if}
					</div>
				{/if}
			</div>
		{/each}
	</div>
</section>

<style>
	@keyframes demoSlide {
		from {
			opacity: 0;
			transform: translateY(-8px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}
</style>
