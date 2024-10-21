<script lang="ts">
	import { Button, Heading, Label, Textarea } from 'flowbite-svelte';

	// import type { Listing, Tag, Category } from '$lib/types/app.d';
	import InputField from '$lib/components/InputField.svelte';
	import TagInputField from '$lib/components/TagInputField.svelte';
	import CategoryInputField from '$lib/components/CategoryInputField.svelte';
	import type { Listing } from '$lib/types/app';

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
</script>

<Heading class="mb-8">Create New Listing</Heading>

<form class="grid grid-cols-2">
	<InputField
		id="title"
		label="Title"
		placeholder="What are you offering?"
		bind:value={listing.title}
	/>
	<span />
	<div class="mb-6">
		<Label for="textarea-id" class="mb-2">Description</Label>
		<Textarea
			id="textarea-id"
			placeholder="Tell people a little bit more about the item."
			rows={4}
			name="message"
			bind:value={listing.description}
		/>
	</div>
	<span />
	<InputField
		id="condition"
		label="Item Condition"
		placeholder="What condition is the item(s) in? (Like new, gently used, any damage, etc.)"
		bind:value={listing.condition}
	/>
	<span />
	<InputField
		id="looking-for"
		label="Looking For"
		placeholder="What are you looking for in exchange for the item?"
		bind:value={listing.lookingFor}
	/>
	<span />
	<TagInputField {listing} />
	<span />
	<CategoryInputField {listing} />
	<span />
	<Button>Create!</Button>
</form>
