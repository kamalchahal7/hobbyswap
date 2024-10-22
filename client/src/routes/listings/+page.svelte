<script lang="ts">
	import { onMount } from 'svelte';

	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { formatDistance } from 'date-fns';
	import { generateListings } from '$lib/generators/listing';
	import { getFullUserName } from '$lib/generators/user';
	import type { Listing } from '$lib/types';
	import { Search, Button, Heading, Gallery, Img } from 'flowbite-svelte';
	import { SearchOutline } from 'flowbite-svelte-icons';

	function updateUrl() {
		const params = new URLSearchParams($page.url.searchParams);
		if (searchInput) params.set('search', searchInput);
		else params.delete('search');
		goto(`?${params.toString()}`, { replaceState: true });
	}

	async function handleSearch() {
		// This function is called when the search button is clicked
		// The filtering is already handled reactively, so we don't need to do anything here
		// You could add additional functionality here if needed
		searchTerm = searchInput;
		await searchListings();
		updateUrl();
	}

	async function searchListings(): Promise<Listing[]> {
		return (filteredListings = listings.filter((listing) =>
			listing.title.toLowerCase().includes(searchTerm.toLowerCase())
		));
	}

	let listings: Listing[] = generateListings(15);
	let filteredListings: Listing[] = [];
	let searchInput = '';
	let searchTerm = '';

	onMount(() => {
		const params = $page.url.searchParams;
		searchTerm = params.get('search') || '';
		searchListings();
	});

	$: console.log(filteredListings);
</script>

<main>
	<div class="flex flex-col gap-2 mb-4 p-2">
		<Heading tag="h2">Let's Get Going!</Heading>

		<form class="flex gap-2" on:submit|preventDefault={handleSearch}>
			<Search bind:value={searchInput} size="md" placeholder="What are you looking for?" />
			<Button class="!p-2.5" type="submit">
				<SearchOutline class="w-6 h-6" />
			</Button>
		</form>
	</div>
	<Gallery class="gap-4 sm:grid-cols-2 md:grid-cols-3" items={[]}>
		{#each filteredListings as listing, i}
			<a
				class="rounded-lg p-4 bg-background-700 hover:bg-primary-200 flex flex-col gap-2"
				href={`/listings/${listing.id}`}
			>
				<Heading tag="h4">{listing.title}</Heading>
				<Img
					src={`https://picsum.photos/1280/720?random=${i}`}
					alt={listing.title}
					class="rounded-lg"
				/>
				<div>
					Posted {formatDistance(listing.datePosted, new Date(), { addSuffix: true })} by
					<strong>{getFullUserName(listing.owner)}</strong>
				</div>
			</a>
		{/each}
	</Gallery>
</main>
