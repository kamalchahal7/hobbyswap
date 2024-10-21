<script lang="ts">
	import { Button, Heading, Img, Label, Textarea } from 'flowbite-svelte';

	// import type { Listing, Tag, Category } from '$lib/types/app.d';
	import InputField from '$lib/components/InputField.svelte';
	import TagInputField from '$lib/components/TagInputField.svelte';
	import CategoryInputField from '$lib/components/CategoryInputField.svelte';
	import type { Listing } from '$lib/types/app.d';

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

<form class="grid md:grid-cols-2 gap-x-6">
	<div class="mb-6 flex justify-center">
		<Img src="https://picsum.photos/1280/720" class="row-span-7" alt="sample 1" />
	</div>
	<div>
		<InputField
			id="title"
			label="Title"
			placeholder="What are you offering?"
			bind:value={listing.title}
		/>
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
		<Button>Create!</Button>
	</div>
</form>
