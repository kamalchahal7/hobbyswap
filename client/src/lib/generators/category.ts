import { faker } from '@faker-js/faker';
import type { Category } from '$lib/types';

export function generateCategory(): Category {
	return {
		title: faker.commerce.department()
	};
}

export function generateCategories(count: number | { min: number; max: number }): Category[] {
	const length = faker.helpers.rangeToNumber(count);

	return Array(length).fill(0).map(generateCategory);
}
