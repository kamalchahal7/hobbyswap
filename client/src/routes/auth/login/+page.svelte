<script lang="ts">
	import { Input, Label, Button, A } from 'flowbite-svelte';
</script>

<h1 class="text-3xl mb-4">Welcome Back!</h1>

<form>
	<div class="flex flex-col gap-6 mb-6">
		<div>
			<Label for="email" class="mb-2">Email address</Label>
			<Input type="email" id="email" placeholder="john.doe@company.com" required />
		</div>
		<div>
			<Label for="password" class="mb-2">Password</Label>
			<Input type="password" id="password" placeholder="•••••••••" required />
		</div>
		<div class="flex flex-col gap-2">
			<A href="/auth/forgot-password">Forgot your password?</A>
			<A href="/auth/signup">Don't have an account?</A>
		</div>
	</div>
	<Button type="submit">Submit</Button>
</form>
