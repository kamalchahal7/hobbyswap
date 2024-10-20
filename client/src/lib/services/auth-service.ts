import axios from 'axios';
import type { LoginDto, SignupDto, User } from '$lib/types/app.d';

axios.defaults.withCredentials = true;

async function signUp(data: SignupDto) {
	await axios.post('http://localhost:5000/register', data);
}

async function login(data: LoginDto): Promise<User> {
	const response = await axios.post('http://localhost:5000/login', data);
	const userData: User = response.data;
	return userData;
}

export default {
	signUp,
	login
};
