<script lang="ts">
	import { Checkbox, Label } from 'flowbite-svelte';
	import type { CategoryOption, Listing } from '$lib/types/app.d';

	export let listing: Listing;

	let availableCategories: CategoryOption[] = [
		{ id: 1, title: 'Electronics' },
		{ id: 2, title: 'Books' },
		{ id: 3, title: 'Clothing' }
		// Add more predefined tags as needed
	]
		.map((category) => ({ ...category, chosen: false }))
		.sort((a: CategoryOption, b: CategoryOption) => {
			return a.title.localeCompare(b.title);
		});

	$: listing.categories = availableCategories
		.filter((category) => category.chosen)
		.map((category) => ({
			id: category.id,
			title: category.title
		}));

	$: console.log(listing.categories);
</script>

<div class="mb-6">
	<Label class="mb-2">Categories</Label>
	<div class="flex gap-2">
		{#each availableCategories as category, i}
			<Checkbox
				on:click={() => {
					availableCategories[i].chosen = !availableCategories[i].chosen;
				}}
			>
				{category.title}
			</Checkbox>
		{/each}
	</div>
</div>
