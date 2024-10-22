<script lang="ts">
	import { Checkbox, Label } from 'flowbite-svelte';

	import { generateCategories } from '$lib/generators/category';
	import type { CategoryOption, Listing } from '$lib/types';

	export let listing: Listing;

	let availableCategories: CategoryOption[] = generateCategories(10)
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
	<div class="flex flex-wrap gap-2">
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
