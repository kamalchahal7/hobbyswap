import axios from 'axios';
import type { LoginDto, LoginResponse, SignupDto, User } from '$lib/types';

axios.defaults.withCredentials = true;

async function signUp(data: SignupDto) {
	await axios.post('http://localhost:5000/register', data);
}

async function login(data: LoginDto): Promise<User> {
	const response = await axios.post('http://localhost:5000/login', data);
	const loginResponse: LoginResponse = response.data;
	const userData: User = {
		...loginResponse,
		id: parseInt(loginResponse.user_id),
		firstName: loginResponse.first_name,
		lastName: loginResponse.last_name
	};
	return userData;
}

async function logout(): Promise<boolean> {
	try {
		await axios.post('http://localhost:5000/logout');
		return true;
	} catch {
		return false;
	}
}

export default {
	signUp,
	login,
	logout
};
