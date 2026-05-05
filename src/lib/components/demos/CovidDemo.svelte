<script lang="ts">
	import { onMount, onDestroy } from 'svelte';

	let canvas: HTMLCanvasElement;
	let ChartClass: typeof import('chart.js').Chart | null = null;
	let chart: import('chart.js').Chart | null = null;

	type Metric = 'cases' | 'deaths';
	let metric = $state<Metric>('cases');

	const labels = [
		'Mar 2020', 'Jun 2020', 'Sep 2020', 'Dec 2020',
		'Mar 2021', 'Jun 2021', 'Sep 2021', 'Dec 2021'
	];

	const dataset = {
		cases: {
			Thailand: [1523, 3162, 3497, 7425, 29619, 218147, 1536665, 2213502],
			Japan: [3654, 18593, 79316, 236879, 468388, 812340, 1749673, 1734673],
			USA: [189633, 2590884, 6886784, 19680484, 30487770, 34093609, 43068715, 54843855]
		},
		deaths: {
			Thailand: [9, 58, 59, 64, 94, 1760, 15847, 21859],
			Japan: [85, 974, 1565, 3459, 9346, 14905, 17627, 18367],
			USA: [4081, 126093, 200813, 341879, 551810, 610432, 700280, 826312]
		}
	};

	const palette = {
		Thailand: '#f97316',
		Japan: '#f48fb1',
		USA: '#81d4fa'
	};

	function fmt(v: number) {
		if (v >= 1_000_000) return (v / 1_000_000).toFixed(1) + 'M';
		if (v >= 1_000) return (v / 1_000).toFixed(0) + 'K';
		return String(v);
	}

	async function buildChart() {
		if (!ChartClass || !canvas) return;
		if (chart) chart.destroy();

		const d = dataset[metric];
		chart = new ChartClass(canvas, {
			type: 'line',
			data: {
				labels,
				datasets: (Object.entries(d) as [keyof typeof palette, number[]][]).map(([country, values]) => ({
					label: country,
					data: values,
					borderColor: palette[country],
					backgroundColor: palette[country] + '18',
					borderWidth: 2,
					pointBackgroundColor: palette[country],
					pointRadius: 4,
					pointHoverRadius: 6,
					tension: 0.35,
					fill: false
				}))
			},
			options: {
				responsive: true,
				maintainAspectRatio: false,
				interaction: { mode: 'index', intersect: false },
				plugins: {
					legend: {
						labels: {
							color: '#a8b2d8',
							font: { family: 'JetBrains Mono', size: 12 },
							boxWidth: 12,
							boxHeight: 2,
							usePointStyle: false
						}
					},
					tooltip: {
						backgroundColor: '#1a1a1a',
						borderColor: '#2a2a2a',
						borderWidth: 1,
						titleColor: '#ccd6f6',
						bodyColor: '#8892b0',
						titleFont: { family: 'JetBrains Mono', size: 12 },
						bodyFont: { family: 'JetBrains Mono', size: 11 },
						callbacks: {
							label: (ctx) => ` ${ctx.dataset.label}: ${Number(ctx.parsed.y).toLocaleString()}`
						}
					}
				},
				scales: {
					x: {
						grid: { color: 'rgba(255,255,255,0.04)' },
						ticks: { color: '#8892b0', font: { family: 'JetBrains Mono', size: 11 } }
					},
					y: {
						grid: { color: 'rgba(255,255,255,0.04)' },
						ticks: {
							color: '#8892b0',
							font: { family: 'JetBrains Mono', size: 11 },
							callback: (v) => fmt(Number(v))
						}
					}
				}
			}
		});
	}

	onMount(async () => {
		const { Chart, CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend } =
			await import('chart.js');
		Chart.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend);
		ChartClass = Chart;
		await buildChart();
	});

	onDestroy(() => chart?.destroy());

	$effect(() => {
		metric;
		buildChart();
	});
</script>

<div class="rounded-lg border border-navy-lighter bg-navy p-6 font-mono">
	<div class="mb-4 flex items-center justify-between gap-4">
		<div>
			<p class="text-xs text-green uppercase tracking-widest">COVID-19 Cumulative Statistics</p>
			<p class="text-xs text-slate mt-0.5">Sample snapshot · Mar 2020 – Dec 2021</p>
		</div>
		<div class="flex gap-2">
			<button
				class="rounded px-3 py-1.5 text-xs transition-colors {metric === 'cases'
					? 'bg-green/20 text-green border border-green/40'
					: 'text-slate border border-navy-lighter hover:border-slate/40 hover:text-slate-light'}"
				onclick={() => (metric = 'cases')}
			>
				Cases
			</button>
			<button
				class="rounded px-3 py-1.5 text-xs transition-colors {metric === 'deaths'
					? 'bg-green/20 text-green border border-green/40'
					: 'text-slate border border-navy-lighter hover:border-slate/40 hover:text-slate-light'}"
				onclick={() => (metric = 'deaths')}
			>
				Deaths
			</button>
		</div>
	</div>

	<div class="relative h-56">
		<canvas bind:this={canvas}></canvas>
	</div>

	<p class="mt-3 text-xs text-slate/50">
		Data sourced from CSSEGIS & CSSE at Johns Hopkins University · For demonstration purposes
	</p>
</div>
