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
