<script lang="ts">
	let { url, title }: { url: string; title: string } = $props();

	let status = $state<'loading' | 'loaded' | 'error'>('loading');

	function onLoad() {
		status = 'loaded';
	}

	// Most sites block iframes via X-Frame-Options.
	// We detect a load event but can't detect X-Frame block reliably,
	// so we show an open-external fallback button always.
</script>

<div class="rounded-lg border border-navy-lighter overflow-hidden bg-navy-light font-mono">
	<!-- Browser chrome bar -->
	<div class="flex items-center gap-3 px-4 py-2.5 border-b border-navy-lighter bg-navy">
		<div class="flex gap-1.5 shrink-0">
			<div class="h-3 w-3 rounded-full bg-red-500/60"></div>
			<div class="h-3 w-3 rounded-full bg-yellow-500/60"></div>
			<div class="h-3 w-3 rounded-full bg-green-500/60"></div>
		</div>
		<div class="flex-1 flex items-center gap-2 bg-navy-lighter rounded px-3 py-1">
			<svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-slate/50 shrink-0">
				<rect width="20" height="16" x="2" y="4" rx="2"/>
				<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
			</svg>
			<span class="text-xs text-slate truncate">{url}</span>
		</div>
		<a
			href={url}
			target="_blank"
			rel="noopener noreferrer"
			class="shrink-0 text-slate hover:text-green transition-colors"
			title="Open in new tab"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
				<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
			</svg>
		</a>
	</div>

	<!-- Loading indicator -->
	{#if status === 'loading'}
		<div class="flex items-center justify-center gap-3 py-6 text-slate text-sm">
			<div class="h-4 w-4 animate-spin rounded-full border-2 border-slate/20 border-t-green"></div>
			<span>Loading…</span>
		</div>
	{/if}

	<!-- iframe -->
	<iframe
		src={url}
		{title}
		class="w-full border-0 transition-opacity duration-300 {status === 'loaded' ? 'opacity-100' : 'opacity-0'}"
		style="height: 520px;"
		onload={onLoad}
		sandbox="allow-scripts allow-same-origin allow-forms allow-popups"
	></iframe>

	<!-- Fallback hint -->
	<div class="border-t border-navy-lighter px-4 py-2.5 flex items-center justify-between">
		<span class="text-xs text-slate/50">If the demo doesn't load, it may block embedding.</span>
		<a
			href={url}
			target="_blank"
			rel="noopener noreferrer"
			class="text-xs text-green hover:underline flex items-center gap-1"
		>
			Open full site →
		</a>
	</div>
</div>
