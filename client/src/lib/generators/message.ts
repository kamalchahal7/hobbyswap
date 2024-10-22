import { faker } from '@faker-js/faker';
import { subDays } from 'date-fns';
import type { Message, User } from '$lib/types';

export function generateMessage(sender: User, receiver: User, sent?: Date): Message {
	return {
		id: faker.number.int({ min: 0 }),
		text: faker.lorem.paragraph(),
		sender,
		receiver,
		sent: sent
			? sent
			: faker.date.between({
					from: new Date(2024, 1),
					to: new Date()
				})
	};
}

export function generateMessages(
	count: number | { min: number; max: number },
	sender: User | null,
	receiver: User | null
): Message[] {
	if (sender === null || receiver === null) {
		return [];
	}
	const length = faker.helpers.rangeToNumber(count);

	const dates = Array(length)
		.fill(0)
		.map((_, index, dates) => {
			return faker.date.between({
				from: dates[index - 1] || new Date(2024, 1),
				to: subDays(new Date(), dates.length - index)
			});
		});

	const messages: Message[] = dates.map((date) => {
		const coin: number = faker.number.int({ min: 0, max: 1 });
		let message: Message;
		if (coin % 2 == 0) {
			message = generateMessage(sender, receiver, date);
		} else {
			message = generateMessage(receiver, sender, date);
		}
		return message;
	});

	return messages;
}
