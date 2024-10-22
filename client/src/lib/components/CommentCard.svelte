<script lang="ts">
	import { faker } from '@faker-js/faker';
	import { Avatar, P } from 'flowbite-svelte';
	import type { Comment } from '$lib/types';
	import { getFullUserName } from '$lib/generators/user';

	export let comment: Comment;
</script>

<div class="p-2">
	<div class="flex items-start space-x-4 rtl:space-x-reverse mb-2">
		<Avatar border class=" ring-primary-400" src={faker.image.avatar()}>
			{comment.owner.firstName[0]}{comment.owner.lastName[0]}
		</Avatar>
		<div class="h-10 flex flex-col justify-center font-medium dark:text-white">
			{getFullUserName(comment.owner)}
		</div>
	</div>
	<P>{comment.text}</P>
</div>
