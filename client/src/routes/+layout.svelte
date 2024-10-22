<script lang="ts">
	import '../app.css';
	import { faker } from '@faker-js/faker';
	import {
		Button,
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		Avatar,
		Dropdown,
		DropdownItem,
		DropdownHeader,
		DropdownDivider
	} from 'flowbite-svelte';
	import { onMount } from 'svelte';

	import { page } from '$app/stores';
	import { useUser } from '$lib/hooks/use-user';
	import { useMessageReceiver } from '$lib/hooks/use-message-receiver';
	import authService from '$lib/services/auth-service';

	const user = useUser();
	useMessageReceiver();

	onMount(async () => {
		const authCheck = await authService.authCheck();
		if (authCheck) {
			$user = authCheck;
		}
	});

	$: activeUrl = $page.url.pathname;
</script>

<Navbar
	class="px-2 sm:px-4 py-2.5fixed w-full z-20 top-0 start-0 rounded-lg border-b bg-background-800"
>
	<NavBrand href="/">
		<!-- <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" /> -->
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
			HobbySwap
		</span>
	</NavBrand>
	<div class="flex items-center md:order-2">
		{#if $user}
			<Button class="me-3" href="/listings/new" size="sm">
				+
				<span class="hidden md:inline"> &nbsp;New Listing </span>
			</Button>
			<Avatar id="avatar-menu" src={faker.image.avatar()} />

			<Dropdown placement="bottom" triggeredBy="#avatar-menu">
				<DropdownHeader>
					<span class="block text-sm">{$user.firstName} {$user.lastName}</span>
					<span class="block truncate text-sm font-medium">{$user.email}</span>
				</DropdownHeader>
				<DropdownItem href="/messages">Messages</DropdownItem>
				<DropdownDivider />
				<DropdownItem>Sign out</DropdownItem>
			</Dropdown>
		{:else}
			<Button class="me-3" href="/auth/login" size="sm" outline>Login</Button>
			<Button class="me-3" href="/auth/signup" size="sm">Get Started</Button>
		{/if}

		<NavHamburger />
		<!-- classMenu={{
				class: 'w-full md:flex md:w-auto md:order-1'
			}} -->
	</div>
	<NavUl {activeUrl}>
		<NavLi href="/">Home</NavLi>
		<!-- <NavLi class="cursor-pointer">
			Categories
		</NavLi> -->
		<!-- <Dropdown class="w-44 z-20">
			<DropdownItem href="/">Category1</DropdownItem>
			<DropdownItem href="/">Category2</DropdownItem>
			<DropdownItem href="/">Category3</DropdownItem>
		</Dropdown> -->
		<NavLi href="/listings">Listings</NavLi>
	</NavUl>
</Navbar>
<div class="overflow-scroll py-16 container mx-auto px-2 sm:px-4">
	<slot />
</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.background.900);
		font-family: theme(fontFamily.primary);
	}
</style>
