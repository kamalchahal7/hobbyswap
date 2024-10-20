<script>
	import '../app.css';
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

	import { page } from '$app/stores';
	$: activeUrl = $page.url.pathname;
</script>

<div class="relative px-8">
	<Navbar class="px-2 sm:px-4 py-2.5fixed w-full z-20 top-0 start-0 border-b">
		<NavBrand href="/">
			<!-- <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" /> -->
			<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
				HobbySwap
			</span>
		</NavBrand>
		<div class="flex items-center md:order-2">
			<Button class="me-3" href="/listings/new" size="sm">
				+
				<span class="hidden md:inline"> &nbsp;New Listing </span>
			</Button>
			<Avatar id="avatar-menu" />
			<NavHamburger />
			<!-- classMenu={{
				class: 'w-full md:flex md:w-auto md:order-1'
			}} -->
		</div>
		<Dropdown placement="bottom" triggeredBy="#avatar-menu">
			<DropdownHeader>
				<span class="block text-sm">Bonnie Green</span>
				<span class="block truncate text-sm font-medium">name@flowbite.com</span>
			</DropdownHeader>
			<DropdownItem>Settings</DropdownItem>
			<DropdownDivider />
			<DropdownItem>Sign out</DropdownItem>
		</Dropdown>
		<NavUl {activeUrl}>
			<NavLi href="/">Home</NavLi>
			<NavLi class="cursor-pointer">
				<!-- Dropdown<ChevronDownOutline class="w-6 h-6 ms-2 text-primary-800 dark:text-white inline" /> -->
				Categories
			</NavLi>
			<Dropdown class="w-44 z-20">
				<DropdownItem href="/">Category1</DropdownItem>
				<DropdownItem href="/">Category2</DropdownItem>
				<DropdownItem href="/">Category3</DropdownItem>
			</Dropdown>
			<NavLi href="/listings">Listings</NavLi>
		</NavUl>
	</Navbar>
	<div class="overflow-scroll pb-16">
		<!-- <div class="mt-16" /> -->
		<div class="px-2 sm:px-6">
			<slot />
		</div>
	</div>
</div>
