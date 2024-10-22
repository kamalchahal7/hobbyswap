<script lang="ts">
	import { Button, Heading, Img, Label, Textarea } from 'flowbite-svelte';

	import listingService from '$lib/services/listing-service';
	import InputField from '$lib/components/InputField.svelte';
	import TagInputField from '$lib/components/TagInputField.svelte';
	import CategoryInputField from '$lib/components/CategoryInputField.svelte';
	import { ApiError, type Listing } from '$lib/types/app.d';
	import { goto } from '$app/navigation';

	let listing: Listing = {
		title: '',
		condition: '',
		description: '',
		lookingFor: '',
		datePosted: null,
		categories: [],
		tags: [],
		owner: null,
		comments: []
	};

	async function handleCreateListing() {
		try {
			const response = await listingService.createListing(listing);

			goto(`/listings/${response.id}`);
		} catch (err) {
			if (err == ApiError.UNAUTHORIZED) {
				goto('/auth/login');
			}
			console.error(err);
		}
	}
</script>

<Heading class="mb-8">Create New Listing</Heading>

<form class="grid md:grid-cols-2 gap-x-6" on:submit|preventDefault={handleCreateListing}>
	<div class="mb-6 flex justify-center row-span-7">
		<div><Img src="https://picsum.photos/1280/720" alt="sample 1" /></div>
	</div>
	<div>
		<InputField
			id="title"
			label="Title"
			placeholder="What are you offering?"
			bind:value={listing.title}
		/>
		<div class="mb-6">
			<Label for="description-id" class="mb-2">Description</Label>
			<Textarea
				id="description-id"
				placeholder="Tell people a little bit more about the item."
				rows={4}
				name="description"
				bind:value={listing.description}
			/>
		</div>
		<InputField
			id="condition"
			label="Item Condition"
			placeholder="What condition is the item(s) in? (Like new, gently used, any damage, etc.)"
			bind:value={listing.condition}
		/>
		<InputField
			id="looking-for"
			label="Looking For"
			placeholder="What are you looking for in exchange for the item?"
			bind:value={listing.lookingFor}
		/>
		<TagInputField {listing} />
		<CategoryInputField {listing} />
		<Button type="submit">Create!</Button>
	</div>
</form>
