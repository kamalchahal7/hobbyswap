<script lang="ts">
	import axios from 'axios';
	import { Button, Checkbox, A, Toast } from 'flowbite-svelte';

	import { type SignupDto } from '$lib/types/app.d';
	import InputField from '$lib/components/InputField.svelte';
	import { goto } from '$app/navigation';

	let registered = false;

	async function signUp(e: MouseEvent) {
		e.preventDefault();
		const data: SignupDto = {
			first_name: firstName,
			last_name: lastName,
			date_of_birth: dateOfBirth,
			email,
			password,
			confirmation: confirmPassword
		};
		try {
			await axios.post('http://localhost:5000/register', data);
			registered = true;
			setTimeout(() => {
				goto('/login');
			}, 1000);
		} catch (err) {
			console.error(err);
		}
	}

	let firstName: string;
	let lastName: string;
	let email: string;
	let dateOfBirth: string;
	let agreement: boolean = false;
	let password: string;
	let confirmPassword: string;
</script>

{#if registered}
	<Toast>Registration successful! Redirecting you to the login page . . .</Toast>
{/if}

<h1 class="text-3xl mb-4">Hey There!</h1>

<form>
	<div class="grid gap-6 mb-6 md:grid-cols-2">
		<InputField
			required
			label="First Name"
			id="first_name"
			placeholder="John"
			bind:value={firstName}
		/>
		<InputField required label="Last Name" id="last_name" placeholder="Doe" bind:value={lastName} />
	</div>
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
		label="Date of Birth"
		id="date_of_birth"
		placeholder="1970-01-01"
		type="date"
		bind:value={dateOfBirth}
	/>
	<InputField
		required
		type="password"
		label="Password"
		id="password"
		placeholder="•••••••••"
		bind:value={password}
	/>
	<InputField
		required
		type="password"
		label="Confirm Password"
		id="confirm_password"
		placeholder="•••••••••"
		bind:value={confirmPassword}
	/>
	<Checkbox
		class="mb-6 space-x-1 rtl:space-x-reverse"
		required
		on:click={() => {
			agreement = !agreement;
		}}
	>
		I agree with the <A
			href="/legal/terms-and-conditions"
			class="text-primary-700 dark:text-primary-600 hover:underline"
		>
			terms and conditions
		</A> and the <A
			href="/legal/privacy-policy"
			class="text-primary-700 dark:text-primary-600 hover:underline"
		>
			privacy policy
		</A>.
	</Checkbox>
	<Button type="submit" on:click={signUp}>Submit</Button>
</form>
