import { faker, type SexType } from '@faker-js/faker';

import type { User } from '$lib/types/app.d';

export function generateUser(): User {
	const userSex: SexType = faker.helpers.arrayElement(['female', 'male']);
	return {
		email: faker.internet.email(),
		firstName: faker.person.firstName(userSex),
		lastName: faker.person.lastName(userSex)
	};
}

export function getFullUserName(user: User | null): string {
	if (user === null) {
		return 'Unknown';
	}

	return `${user.firstName} ${user.lastName}`;
}
