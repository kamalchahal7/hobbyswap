<script lang="ts">
	import { Alert } from 'flowbite-svelte';
</script>

<h1 class="text-3xl font-bold underline">Hello world!</h1>

<Alert>
	<span class="font-medium">Info alert!</span>
	This is an alert.
</Alert>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
