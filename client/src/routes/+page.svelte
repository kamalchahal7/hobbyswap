<script lang="ts">
	import { Button, Heading, Img, List, Li, P } from 'flowbite-svelte';

	import { useUser } from '$lib/hooks/use-user';

	const user = useUser();
</script>

<div class="flex flex-col md:flex-row gap-10 md:gap-72">
	<div class="flex flex-col gap-6 order-last md:order-first">
		<Heading>New Hobby? No Problem.</Heading>
		<P>
			Whether you're in need of some new gear or are looking to make room in your closet after you
			lost interest in a hobby, HobbySwap is the spot!
		</P>
		<List>
			<Li>Get equipment for your new interests without having to pay the big bucks!</Li>
			<Li>Trade gently used or unused new items for things you'll actually use (hopefully)!</Li>
			<Li>Don't like your new hobby as much as you thought? Swap again and again until you do!</Li>
		</List>

		<div class="grid gap-6 mb-6 md:grid-cols-2">
			{#if $user}
				<Button href="/listings">I need new stuff!</Button>
				<Button href="/listings/new">I want to get rid of stuff...</Button>
			{:else}
				<p>Getting started is free and always will be. No credit card required!</p>
				<Button size="sm" href="/auth/signup">Start Trading</Button>
			{/if}
		</div>
	</div>
	<Img
		src="https://picsum.photos/1280/720?random=home"
		alt="HobbySwap"
		size="max-w-xl"
		class="rounded-lg"
	/>
</div>
