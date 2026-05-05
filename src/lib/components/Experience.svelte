<script lang="ts">
	import { experience, volunteering } from '$lib/data';
	import { onMount } from 'svelte';

	type Job = { company: string; role: string; period: string; location: string; url: string | null; note?: string; bullets: string[] };

	let activeTab = $state(0);
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

<section id="experience" class="px-6 py-24 md:px-12 lg:px-16" bind:this={el}>
	<h2 class="section-heading reveal"><span>Experience</span></h2>

	<div class="reveal flex max-w-2xl flex-col gap-0 md:flex-row" style="transition-delay: 100ms;">
		<!-- Company tabs -->
		<div class="mb-6 flex overflow-x-auto md:mb-0 md:flex-col md:overflow-x-visible">
			{#each experience as job, i}
				<button
					class="relative shrink-0 px-4 py-3 text-left font-mono text-sm transition-all duration-200 md:border-l-2 md:border-b-0 border-b-2
					{activeTab === i
						? 'text-green md:border-l-green border-b-green bg-navy-light'
						: 'text-slate md:border-l-navy-lighter border-b-navy-lighter hover:text-slate-light hover:bg-navy-light/50'}"
					onclick={() => (activeTab = i)}
				>
					<span class="whitespace-nowrap">{job.company.split(' ').slice(0, 2).join(' ')}</span>
				</button>
			{/each}
		</div>

		<!-- Job details -->
		<div class="pl-0 md:pl-8 flex-1">
			{#key activeTab}
				{@const job = experience[activeTab] as Job}
				<div class="animate-[fadeSlideIn_0.3s_ease_forwards]">
					<h3 class="text-lg font-semibold text-offwhite mb-1">
						{job.role}
						{#if job.url}
							<span class="text-green"> @ <a href={job.url} target="_blank" rel="noopener noreferrer" class="hover:underline">{job.company}</a></span>
						{:else}
							<span class="text-green"> @ {job.company}</span>
						{/if}
					</h3>
					<div class="flex flex-wrap items-center gap-3 mb-5">
						<p class="font-mono text-xs text-slate">{job.period}{job.location ? ` · ${job.location}` : ''}</p>
						{#if job.note}
							<span class="font-mono text-xs px-2 py-0.5 rounded border border-green/30 text-green bg-green/5">
								↑ {job.note}
							</span>
						{/if}
					</div>
					<ul class="space-y-3">
						{#each job.bullets as bullet}
							<li class="flex gap-3 text-sm text-slate leading-relaxed">
								<span class="mt-1.5 shrink-0 text-green">▹</span>
								<span>{bullet}</span>
							</li>
						{/each}
					</ul>
				</div>
			{/key}
		</div>
	</div>

	<!-- Volunteering -->
	<div class="reveal mt-16 max-w-2xl" style="transition-delay: 200ms;">
		<p class="font-mono text-xs text-slate tracking-widest uppercase mb-6">Volunteering</p>
		<div class="space-y-6">
			{#each volunteering as v}
				<div class="flex gap-4 group">
					<div class="mt-1 shrink-0 w-1.5 h-1.5 rounded-full bg-navy-lighter group-hover:bg-green transition-colors duration-200 mt-2"></div>
					<div>
						<h4 class="text-sm font-medium text-slate-lightest">{v.role}</h4>
						<p class="font-mono text-xs text-slate mt-0.5 mb-1.5">
							{v.org} · {v.period}
							<span class="ml-2 text-slate/50">{v.category}</span>
						</p>
						<p class="text-sm text-slate leading-relaxed">{v.description}</p>
						{#if v.link}
							<a
								href={v.link}
								target="_blank"
								rel="noopener noreferrer"
								class="mt-2 inline-flex items-center gap-1.5 font-mono text-xs text-green hover:underline"
							>
								<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
									<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/>
								</svg>
								{v.linkLabel} →
							</a>
						{/if}
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	@keyframes fadeSlideIn {
		from {
			opacity: 0;
			transform: translateY(8px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}
</style>
