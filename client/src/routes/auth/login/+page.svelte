<script lang="ts">
	import { Button, A } from 'flowbite-svelte';

	import { goto } from '$app/navigation';
	import InputField from '$lib/components/InputField.svelte';
	import { useUser } from '$lib/hooks/use-user';
	import authService from '$lib/services/auth-service';

	const user = useUser();

	async function login(e: MouseEvent) {
		e.preventDefault();
		try {
			$user = await authService.login({
				email,
				password
			});
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
