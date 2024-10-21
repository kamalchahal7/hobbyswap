import { faker } from '@faker-js/faker';
import type { Tag } from '$lib/types';

export function generateTag(): Tag {
	return {
		value: faker.commerce.productAdjective()
	};
}

export function generateTags(count: number | { min: number; max: number }): Tag[] {
	const length = faker.helpers.rangeToNumber(count);

	return Array(length).fill(0).map(generateTag);
}
