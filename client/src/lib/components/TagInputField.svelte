<script lang="ts">
	import { Search, Label, Badge, Listgroup } from 'flowbite-svelte';
	import { CloseOutline } from 'flowbite-svelte-icons';

	import type { Tag, Listing } from '$lib/types';
	import { generateTags } from '$lib/generators/tag';

	export let listing: Listing;

	let searchTerm = '';
	let availableTags: Tag[] = generateTags(10);

	function addTag(tag: Tag) {
		if (!listing.tags.some((t: Tag) => t.value === tag.value)) {
			listing.tags = [...listing.tags, tag];
		}
		searchTerm = '';
	}

	function removeTag(tag: Tag) {
		listing.tags = listing.tags.filter((t: Tag) => t.value !== tag.value);
	}

	function filterTags(availableTags: Tag[], searchTerm: string) {
		let result: Tag[] = [{ value: searchTerm }];
		result.push(
			...availableTags.filter(
				(tag) =>
					tag.value.toLowerCase().includes(searchTerm.toLowerCase()) &&
					!listing.tags.some((t: Tag) => t.value === tag.value)
			)
		);
		return result;
	}

	$: filteredTags = filterTags(availableTags, searchTerm);
</script>

<div>
	<Label class="mb-2">Tags</Label>
	<div class="mb-4">
		<Search bind:value={searchTerm} size="md" placeholder="Search for tags, or add your own!" />
	</div>

	{#if filteredTags.length > 0 && searchTerm}
		<div class="mb-4">
			<Listgroup
				active
				items={filteredTags}
				let:item
				class="w-48"
				on:click={(e) => addTag(e.detail)}
			>
				{item.value}
			</Listgroup>
		</div>
	{/if}

	<div class="flex flex-wrap gap-2 mb-4">
		{#each listing.tags as tag}
			<Badge class="flex items-center">
				{tag.value}
				<button on:click={() => removeTag(tag)} class="ml-2 focus:outline-none">
					<CloseOutline class="w-3 h-3" />
				</button>
			</Badge>
		{/each}
	</div>
</div>
