<script lang="ts">
	import '../app.css';
	import Nav from '$lib/components/Nav.svelte';
	import { meta } from '$lib/data';
	import { onMount } from 'svelte';

	let { children } = $props();

	onMount(() => {
		const link = document.createElement('link');
		link.rel = 'stylesheet';
		link.href =
			'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap';
		document.head.appendChild(link);
	});
</script>

<svelte:head>
	<title>{meta.name} — Senior Software Engineer</title>
	<meta name="description" content={meta.bio} />

	<!-- Open Graph -->
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://kridtinc-portfolio.pages.dev" />
	<meta property="og:title" content="{meta.name} — Senior Software Engineer" />
	<meta property="og:description" content={meta.bio} />
	<meta property="og:image" content="https://kridtinc-portfolio.pages.dev/og-image.png" />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta property="og:site_name" content="{meta.name}" />
	<meta property="og:locale" content="en_US" />

	<!-- Twitter / X -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="{meta.name} — Senior Software Engineer" />
	<meta name="twitter:description" content={meta.bio} />
	<meta name="twitter:image" content="https://kridtinc-portfolio.pages.dev/og-image.png" />

	<meta name="theme-color" content="#0f0f0f" />

	<!-- Preconnect for faster font loading when JS kicks in -->
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
</svelte:head>

<div class="relative min-h-screen">
	<Nav />
	<div class="lg:flex">
		<!-- Left sticky column (BC layout) -->
		<div class="hidden lg:block lg:w-[45%] xl:w-[40%]"></div>

		<!-- Content -->
		<main id="main-content" class="lg:ml-auto lg:w-[55%] xl:w-[60%]">
			{@render children()}
		</main>
	</div>
</div>
