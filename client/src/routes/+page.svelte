<script lang="ts">
	import { Button, List, Li } from 'flowbite-svelte';

	import { type User } from '$lib/types/app.d';
	import { useUser } from '$lib/hooks/use-user';

	const user = useUser();
	const userData: User = {
		firstName: 'John',
		lastName: 'Doe',
		email: 'johndoe@gmail.com'
	};
	user.set(userData);
</script>

<div class="flex flex-col gap-6">
	<h1 class="text-3xl">One hobbyist's junk is another's new love!</h1>
	<p>
		Whether you're in need of some new gear or are looking to make room in your closet after you
		lost interest in a hobby, HobbySwap is the spot!
	</p>
	<List>
		<Li>Get equipment for your new interests without having to pay the big bucks</Li>
		<Li>Trade gently used or unused new items for things you'll actually use (hopefully)</Li>
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
