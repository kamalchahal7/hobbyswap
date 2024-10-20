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

<Navbar>
	<NavBrand href="/">
		<!-- <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" /> -->
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
			HobbySwap
		</span>
	</NavBrand>
	<div class="flex items-center md:order-2">
		<Button class="me-3" href="/listings/new">
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
<slot />
