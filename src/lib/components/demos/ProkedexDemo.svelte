<script lang="ts">
	import { onMount } from 'svelte';

	let query = $state('charizard');
	let inputVal = $state('charizard');
	let pokemon = $state<Record<string, unknown> | null>(null);
	let loading = $state(false);
	let error = $state('');

	const typeColors: Record<string, string> = {
		fire: '#FF6B35',
		water: '#4FC3F7',
		grass: '#81C784',
		electric: '#FFD54F',
		psychic: '#F48FB1',
		normal: '#A8A878',
		flying: '#A890F0',
		poison: '#A040A0',
		ground: '#E0C068',
		rock: '#B8A038',
		bug: '#A8B820',
		ghost: '#705898',
		steel: '#B8B8D0',
		ice: '#98D8D8',
		dragon: '#7038F8',
		dark: '#705848',
		fairy: '#EE99AC',
		fighting: '#C03028'
	};

	const suggestions = ['pikachu', 'charizard', 'mewtwo', 'eevee', 'gengar', 'snorlax', 'bulbasaur'];

	async function fetchPokemon(name = query) {
		if (!name.trim()) return;
		loading = true;
		error = '';
		pokemon = null;
		try {
			const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${name.toLowerCase().trim()}`);
			if (!res.ok) throw new Error(`"${name}" not found. Try: pikachu, charizard, mewtwo…`);
			pokemon = await res.json();
		} catch (e: unknown) {
			error = e instanceof Error ? e.message : 'Unknown error';
		} finally {
			loading = false;
		}
	}

	onMount(() => fetchPokemon());

	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		query = inputVal;
		fetchPokemon(inputVal);
	}

	function getSprite(p: Record<string, unknown>) {
		const other = p.sprites as Record<string, unknown>;
		const oa = (other?.other as Record<string, unknown>)?.['official-artwork'] as Record<string, unknown>;
		return (oa?.front_default as string) || ((p.sprites as Record<string, unknown>)?.front_default as string);
	}

	function getTypes(p: Record<string, unknown>) {
		return (p.types as { type: { name: string } }[]).map((t) => t.type.name);
	}

	function getStats(p: Record<string, unknown>) {
		return (p.stats as { stat: { name: string }; base_stat: number }[]).map((s) => ({
			name: s.stat.name.replace('special-', 'sp.').replace('-', ' '),
			val: s.base_stat
		}));
	}
</script>

<div class="rounded-lg border border-navy-lighter bg-navy p-6 font-mono">
	<!-- Search -->
	<form onsubmit={handleSubmit} class="mb-6 flex gap-2">
		<input
			type="text"
			bind:value={inputVal}
			placeholder="Name or number…"
			class="flex-1 rounded border border-navy-lighter bg-navy-light px-4 py-2 text-sm text-slate-lightest placeholder-slate/50 outline-none focus:border-green/60 focus:ring-1 focus:ring-green/20 transition-colors"
		/>
		<button
			type="submit"
			class="rounded border border-green/60 px-4 py-2 text-xs text-green hover:bg-green/10 transition-colors"
		>
			Search
		</button>
	</form>

	<!-- Quick picks -->
	<div class="mb-6 flex flex-wrap gap-2">
		{#each suggestions as s}
			<button
				class="rounded px-2.5 py-1 text-xs text-slate border border-navy-lighter hover:border-green/40 hover:text-green transition-colors capitalize {query === s ? 'border-green/40 text-green' : ''}"
				onclick={() => { inputVal = s; query = s; fetchPokemon(s); }}
			>
				{s}
			</button>
		{/each}
	</div>

	<!-- States -->
	{#if loading}
		<div class="flex items-center justify-center gap-3 py-12 text-slate">
			<div class="h-5 w-5 animate-spin rounded-full border-2 border-slate/30 border-t-green"></div>
			<span class="text-sm">Loading…</span>
		</div>
	{:else if error}
		<div class="py-8 text-center text-sm text-red-400">{error}</div>
	{:else if pokemon}
		{@const types = getTypes(pokemon)}
		{@const stats = getStats(pokemon)}
		{@const sprite = getSprite(pokemon)}
		<div class="flex flex-col gap-6 sm:flex-row">
			<!-- Sprite + identity -->
			<div class="flex flex-col items-center gap-3 sm:w-44 shrink-0">
				<div
					class="flex h-36 w-36 items-center justify-center rounded-lg bg-navy-light border border-navy-lighter"
					style="background: radial-gradient({typeColors[types[0]] || '#333'}22, #1a1a1a 70%);"
				>
					{#if sprite}
						<img src={sprite} alt={pokemon.name as string} class="h-28 w-28 object-contain drop-shadow-lg" />
					{:else}
						<span class="text-4xl">?</span>
					{/if}
				</div>
				<div class="text-center">
					<p class="text-xs text-slate mb-1">#{String(pokemon.id).padStart(3, '0')}</p>
					<h3 class="text-lg font-semibold capitalize text-slate-lightest">{pokemon.name as string}</h3>
					<div class="mt-2 flex justify-center gap-2">
						{#each types as type}
							<span
								class="rounded px-2.5 py-0.5 text-xs font-semibold capitalize text-navy"
								style="background: {typeColors[type] || '#888'};"
							>
								{type}
							</span>
						{/each}
					</div>
				</div>
				<div class="flex gap-4 text-xs text-slate">
					<span>H: {((pokemon.height as number) / 10).toFixed(1)}m</span>
					<span>W: {((pokemon.weight as number) / 10).toFixed(1)}kg</span>
				</div>
			</div>

			<!-- Stats -->
			<div class="flex-1 space-y-2.5">
				<p class="text-xs text-green uppercase tracking-widest mb-3">Base Stats</p>
				{#each stats as stat}
					<div class="flex items-center gap-3">
						<span class="w-16 text-right text-xs text-slate shrink-0 capitalize">{stat.name}</span>
						<span class="w-8 text-right text-xs text-slate-light shrink-0">{stat.val}</span>
						<div class="flex-1 h-1.5 rounded-full bg-navy-lighter overflow-hidden">
							<div
								class="h-full rounded-full transition-all duration-700"
								style="width: {Math.min((stat.val / 255) * 100, 100)}%; background: {typeColors[types[0]] || '#64ffda'};"
							></div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	{/if}
</div>
