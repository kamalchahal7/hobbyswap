<script lang="ts">
	import { get } from 'svelte/store';
	import {
		Button,
		Badge,
		Heading,
		P,
		Img,
		Gallery,
		Label,
		Textarea
	} from 'flowbite-svelte';
	import { formatDistance } from 'date-fns';

	import { generateListing } from '$lib/generators/listing';
	import type { Listing } from '$lib/types/app.d';
	import { getFullUserName } from '$lib/generators/user';

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
</script>

<div class="flex flex-col md:flex-row gap-6">
	<div class="flex flex-col gap-6 basis-1/2">
		<Heading>{listing.title}</Heading>
		<div class="flex">
			{#each listing.tags as tag}
				<Badge>{tag.value}</Badge>
			{/each}
		</div>
		<div>
			<h3 class="text-lg font-bold">Categories</h3>
			<div class="flex">
				{#each listing.categories as category}
					<Badge large color="dark">{category.title}</Badge>
				{/each}
			</div>
		</div>
		<div>
			Posted {formatDistance(listing.datePosted, new Date(), { addSuffix: true })} by
			<strong>{getFullUserName(listing.owner)}</strong>
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
	</div>
	<div class="mb-6 flex flex-col gap-4 justify-center basis-1/2">
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
