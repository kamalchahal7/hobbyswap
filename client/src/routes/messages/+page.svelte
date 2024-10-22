<script lang="ts">
	import { faker } from '@faker-js/faker';
	import { Avatar, Listgroup, Drawer, Button, CloseButton } from 'flowbite-svelte';
	import { InfoCircleSolid, ArrowRightOutline } from 'flowbite-svelte-icons';
	import { sineIn } from 'svelte/easing';

	import type { User } from '$lib/types';
	import { generateUser, getFullUserName } from '$lib/generators/user';
	import Conversation from '$lib/components/Conversation.svelte';
	import { useMessageReceiver } from '$lib/hooks/use-message-receiver';

	// Conversations are just a bunch of users
	let userList: User[] = Array(6).fill(0).map(generateUser);
	let users: Record<number, User> = {};
	userList.forEach((user: User) => {
		users[user.id] = user;
	});

	let sidebarData = userList
		.map((user) => {
			return { name: getFullUserName(user), user };
		})
		.sort((a, b) => {
			return a.name.localeCompare(b.name);
		});

	let usersHidden = true;
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn
	};

	const currentReceiver = useMessageReceiver();

	$: console.log($currentReceiver);
</script>

<div class="flex flex-col gap-4">
	<div class="w-fit">
		<Button on:click={() => (usersHidden = false)} class="min-w-fit">All Conversations</Button>
	</div>

	<Conversation />
</div>

<Drawer
	placement="left"
	transitionType="fly"
	{transitionParams}
	bind:hidden={usersHidden}
	id="usersSidebar"
>
	<div class="flex">
		<Listgroup
			active
			items={sidebarData}
			let:item
			class="w-4/5"
			on:click={(e) => {
				$currentReceiver = e.detail.user;
				usersHidden = true;
			}}
		>
			<div class="flex items-start space-x-4 rtl:space-x-reverse">
				<Avatar border class=" ring-primary-400" src={faker.image.avatar()}>
					{item.user.firstName[0]}{item.user.lastName[0]}
				</Avatar>
				<div class="h-10 flex flex-col justify-center font-medium dark:text-white">
					{item.name}
				</div>
			</div>
		</Listgroup>
		<CloseButton on:click={() => (usersHidden = true)} class="mb-4 dark:text-white h-fit" />
	</div>
</Drawer>
