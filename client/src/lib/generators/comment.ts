import { faker } from '@faker-js/faker';
import type { Comment, Listing } from '$lib/types';
import { generateUser } from '$lib/generators/user';

export function generateComment(listing: Listing): Comment {
	return {
		id: faker.number.int(),
		text: faker.lorem.paragraph(),
		owner: generateUser(),
		listing
	};
}

export function generateComments(
	count: number | { min: number; max: number },
	listing: Listing
): Comment[] {
	const length = faker.helpers.rangeToNumber(count);

	return Array(length)
		.fill(0)
		.map(() => generateComment(listing));
}
