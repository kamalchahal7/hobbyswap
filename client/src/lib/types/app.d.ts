// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces

declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export interface User {
	email: string;
	firstName: string;
	lastName: string;
	dateOfBirth?: DateTime;
	listings?: Listing[];
	comments?: Comment[];
}

export interface Tag {
	value: string;
	categories?: Category[];
}

export interface Category {
	id?: number;
	title: string;
	tags?: Tag[];
}

export interface CategoryOption extends Category {
	chosen: boolean;
}

export interface Listing {
	id?: number;
	title: string;
	description: string;
	condition: string;
	lookingFor: string;
	// images: string;
	datePosted: DateTime | null;
	categories: Category[];
	tags: Tag[];
	owner: User | null;
	comments: Comment[];
}

export interface Comment {
	id: number;
	text: string;
	owner: User;
	listing: Listing;
	replyTo?: Comment;
}

export interface UserDto {
	email: string;
	first_name: string;
	last_name: string;
	date_of_birth: string;
}

export interface LoginDto {
	email: string;
	password: string;
}

export interface SignupDto extends UserDto {
	password: string;
	confirmation: string;
}

export interface LoginResponse {
	user_id: string;
	first_name: string;
	last_name: string;
	email: string;
}

export {};
