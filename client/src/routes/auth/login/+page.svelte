<script lang="ts">
	import axios from 'axios';
	import { Button, A } from 'flowbite-svelte';
	import { goto } from '$app/navigation';

	import { type User, type LoginDto } from '$lib/types/app.d';
	import InputField from '$lib/components/InputField.svelte';
	import { useUser } from '$lib/hooks/use-user';

	const user = useUser();

	async function login(e: MouseEvent) {
		e.preventDefault();
		const data: LoginDto = {
			email,
			password
		};
		try {
			const response = await axios.post('http://localhost:5000/login', data, {
				withCredentials: true
			});
			const userData: User = response.data;
			$user = userData;
			await goto('/');
		} catch (err) {
			console.error(err);
		}
	}

	let email: string;
	let password: string;
</script>

<h1 class="text-3xl mb-4">Welcome Back!</h1>

<form>
	<div class="flex flex-col gap-6 mb-6">
		<InputField
			required
			type="email"
			label="Email Address"
			id="email"
			placeholder="john.doe@company.com"
			bind:value={email}
		/>
		<InputField
			required
			type="password"
			label="Password"
			id="password"
			placeholder="•••••••••"
			bind:value={password}
		/>
		<div class="flex flex-col gap-2">
			<A href="/auth/forgot-password">Forgot your password?</A>
			<A href="/auth/signup">Don't have an account?</A>
		</div>
	</div>
	<Button type="submit" on:click={login}>Submit</Button>
</form>
