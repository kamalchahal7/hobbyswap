<script lang="ts">
	import { Label, Textarea } from 'flowbite-svelte';

	// import type { Listing, Tag, Category } from '$lib/types/app.d';
	import InputField from '$lib/components/InputField.svelte';

	let title: string;
	let condition: string;
	let description: string;
	let lookingFor: string;
</script>

<form>
	<InputField id="title" label="Title" placeholder="What are you offering?" bind:value={title} />
	<div class="mb-6">
		<Label for="textarea-id" class="mb-2">Description</Label>
		<Textarea
			id="textarea-id"
			placeholder="Tell people a little bit more about the item."
			rows={4}
			name="message"
			bind:value={description}
		/>
	</div>
</form>
