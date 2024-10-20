declare global {
	interface UserDTO {
		email: string;
		first_name: string;
		last_name: string;
		date_of_birth: string;
	}

	interface LoginDTO {
		email: string;
		password: string;
	}

	interface SignupDTO extends UserDTO {
		password: string;
		confirm_password: string;
	}
}

export {};
