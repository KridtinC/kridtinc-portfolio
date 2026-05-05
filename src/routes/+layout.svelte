<script lang="ts">
	import '../app.css';
	import Nav from '$lib/components/Nav.svelte';
	import { meta } from '$lib/data';

	let { children } = $props();
</script>

<svelte:head>
	<title>{meta.name} — Software Engineer</title>
	<meta name="description" content={meta.bio} />
	<meta property="og:title" content="{meta.name} — Software Engineer" />
	<meta property="og:description" content={meta.bio} />
	<meta name="theme-color" content="#0a192f" />
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
