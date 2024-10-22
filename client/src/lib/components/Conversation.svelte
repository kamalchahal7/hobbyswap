<script lang="ts">
	import type { User, Message } from '$lib/types';
	import { Heading, Textarea, Button } from 'flowbite-svelte';
	import { getFullUserName } from '$lib/generators/user';
	import { generateMessages } from '$lib/generators/message';
	import { useMessageReceiver } from '$lib/hooks/use-message-receiver';
	import { useUser } from '$lib/hooks/use-user';

	let currentReceiver = useMessageReceiver();
	let sender = useUser();

	let messageText: string = '';

	$: messages = generateMessages(5, $sender, $currentReceiver);

	$: console.log($currentReceiver, $sender);

	function getMessageContainerClasses(message: Message) {
		const receiverClasses = 'justify-start';
		const senderClasses = 'justify-end';
		const bubbleClasses = message.sender == $sender ? senderClasses : receiverClasses;
		return `flex p-4 ${bubbleClasses}`;
	}

	function getMessageClasses(message: Message) {
		const receiverClasses = 'bg-primary-200';
		const senderClasses = 'bg-primary-100';
		const bubbleClasses = message.sender == $sender ? senderClasses : receiverClasses;
		return `flex p-4 basis-2/3 rounded-lg ${bubbleClasses}`;
	}
</script>

<div class="bg-background-800 p-4 rounded-lg">
	{#if $currentReceiver}
		<div class="flex flex-col gap-4">
			<Heading>{getFullUserName($currentReceiver)}</Heading>
			<div class="bg-background-700 p-8 rounded-lg flex flex-col gap-4">
				<div>
					{#each messages as message}
						<div class={getMessageContainerClasses(message)}>
							<div class={getMessageClasses(message)}>
								<p>{message.text}</p>
							</div>
						</div>
					{:else}
						<p>No messages yet!</p>
					{/each}
				</div>
				<Textarea id="newcomment-id" bind:value={messageText}></Textarea>
				<div class="flex justify-end">
					<Button class="w-fit">Comment</Button>
				</div>
			</div>
		</div>
	{:else}
		<Heading>Messages</Heading>
	{/if}
</div>
