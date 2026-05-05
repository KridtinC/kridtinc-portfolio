<script lang="ts">
	import { onMount } from 'svelte';
	import { activeSection } from '$lib/stores';
	import Hero from '$lib/components/Hero.svelte';
	import About from '$lib/components/About.svelte';
	import Experience from '$lib/components/Experience.svelte';
	import Skills from '$lib/components/Skills.svelte';
	import Work from '$lib/components/Work.svelte';
	import Contact from '$lib/components/Contact.svelte';

	onMount(() => {
		const sections = document.querySelectorAll('section[id]');
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						activeSection.set(entry.target.id);
					}
				});
			},
			{ rootMargin: '-40% 0px -50% 0px' }
		);
		sections.forEach((s) => observer.observe(s));
		return () => observer.disconnect();
	});
</script>

<Hero />
<About />
<Experience />
<Skills />
<Work />
<Contact />
