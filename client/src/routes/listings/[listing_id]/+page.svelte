<script lang="ts">
	import { goto } from '$app/navigation';
	import { Avatar, Button, Badge, Heading, P, Img, Gallery } from 'flowbite-svelte';
	import { faker } from '@faker-js/faker';
	import { formatDistance } from 'date-fns';

	import Comments from '$lib/components/Comments.svelte';
	import { generateListing } from '$lib/generators/listing';
	import { getFullUserName } from '$lib/generators/user';
	import { useMessageReceiver } from '$lib/hooks/use-message-receiver';
	import type { Listing } from '$lib/types';

	let listing: Listing = generateListing();

	let featuredImage = {
		alt: listing.title,
		src: 'https://picsum.photos/1280/720'
	};

	let images = Array(3)
		.fill(0)
		.map((_, index) => {
			return { alt: listing.title, src: `https://picsum.photos/1280/720?random=${index}` };
		});

	const messageReceiver = useMessageReceiver();
</script>

<div class="flex flex-col md:flex-row gap-6">
	<div class="flex flex-col order-last md:order-first gap-6 basis-1/2">
		<Heading>{listing.title}</Heading>
		<div class="flex gap-10">
			<div class="flex flex-col justify-center w-fit">
				<span
					>Posted {formatDistance(listing.datePosted, new Date(), { addSuffix: true })} by
					<strong>{getFullUserName(listing.owner)}</strong>
				</span>
			</div>
			<Avatar id="avatar-menu" src={faker.image.avatar()} />
			<div>
				<Button
					size="sm"
					on:click={() => {
						$messageReceiver = listing.owner;
						goto('/messages', { replaceState: true });
					}}
				>
					I'm interested!
				</Button>
			</div>
		</div>
		<div class="flex gap-4">
			{#each listing.tags as tag}
				<Badge>{tag.value}</Badge>
			{/each}
		</div>
		<div>
			<h3 class="text-lg font-bold">Categories</h3>
			<div class="flex gap-4">
				{#each listing.categories as category}
					<Badge large color="dark">{category.title}</Badge>
				{/each}
			</div>
		</div>

		<P>{listing.description}</P>
		<div>
			<h3 class="text-lg font-bold">Condition</h3>
			<P>{listing.condition}</P>
		</div>
		<div>
			<h3 class="text-lg font-bold">Looking For</h3>
			<P>{listing.lookingFor}</P>
		</div>
		<Comments {listing} />
	</div>
	<div class="mb-6 flex flex-col gap-4 justify-start basis-1/2">
		<Img
			src={featuredImage.src}
			alt={featuredImage.alt}
			size="max-w-full"
			class="h-auto rounded-lg"
		/>
		<Gallery items={[]} class="grid-cols-3 gap-4">
			{#each images as image}
				<div>
					<Img src={image.src} alt={image.alt} size="max-w-" class="h-auto rounded-lg" />
				</div>
			{/each}
		</Gallery>
	</div>
</div>
