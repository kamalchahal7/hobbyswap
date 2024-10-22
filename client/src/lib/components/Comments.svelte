<script lang="ts">
	import { Button, Heading, Label, Textarea } from 'flowbite-svelte';

	import CommentCard from '$lib/components/CommentCard.svelte';
	import type { Comment, Listing } from '$lib/types';
	import { useUser } from '$lib/hooks/use-user';

	export let listing: Listing;
	const user = useUser();

	let newComment: Comment = {
		text: '',
		listing,
		owner: $user!,
		replyTo: null
	};
</script>

<div class="flex flex-col gap-6">
	<Heading tag="h3">Comments</Heading>
	<div class="flex flex-col gap-2">
		<Label for="newcomment-id">Add a comment</Label>
		<Textarea id="newcomment-id" bind:value={newComment.text}></Textarea>
		<Button class="w-fit">Comment</Button>
	</div>
	{#each listing.comments as comment}
		<CommentCard {comment} />
	{/each}
</div>
