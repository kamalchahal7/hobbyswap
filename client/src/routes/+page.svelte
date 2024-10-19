<script lang="ts">
	import { Alert } from 'flowbite-svelte';
</script>

<h1 class="text-3xl font-bold underline">Hello world!</h1>

<Alert>
	<span class="font-medium">Info alert!</span>
	This is an alert.
</Alert>

<!--
This should probably be the main page, including search
1. Page should prompt anon users to get started by signing up
2. Should have category examples
3. Should have search
-->

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
