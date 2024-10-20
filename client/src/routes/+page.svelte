<script lang="ts">
	import { Button } from 'flowbite-svelte';

	import { useUser } from '$lib/hooks/use-user';

	const user = useUser();
</script>

<div class="flex flex-col gap-6">
	<h1 class="text-3xl">One hobbyist's junk is another's new love!</h1>
	<p>
		Whether you're in need of some new gear or are looking to make room in your closet after you
		lost interest in a hobby, HobbySwap is the spot!
	</p>
	<div class="grid gap-6 mb-6 md:grid-cols-2">
		{#if $user}
			<Button href="/listings">I want new stuff!</Button>
			<Button href="/listings/new">I want to get rid of stuff...</Button>
		{:else}
			<p>Getting started is free and always will be. No credit card required!</p>
			<Button size="sm" href="/auth/signup">Sign Up</Button>
		{/if}
	</div>
</div>
