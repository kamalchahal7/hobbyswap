import { faker } from '@faker-js/faker';

import { generateCategories } from '$lib/generators/category';
import { generateComments } from '$lib/generators/comment';
import { generateTags } from '$lib/generators/tag';
import { generateUser } from '$lib/generators/user';
import type { Listing } from '$lib/types';

export function generateListing(): Listing {
	const newListing: Listing = {
		title: faker.commerce.productName(),
		condition: faker.lorem.sentence({
			min: 10,
			max: 25
		}),
		description: faker.commerce.productDescription(),
		lookingFor: faker.lorem.sentence({
			min: 10,
			max: 25
		}),
		datePosted: faker.date.between({
			from: new Date(2024, 1),
			to: new Date()
		}),
		categories: generateCategories({
			min: 1,
			max: 3
		}),
		tags: generateTags({
			min: 1,
			max: 3
		}),
		owner: generateUser(),
		comments: []
	};

	newListing.comments = generateComments({ min: 0, max: 3 }, newListing);

	return newListing;
}
