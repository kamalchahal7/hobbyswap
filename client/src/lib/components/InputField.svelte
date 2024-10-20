<script lang="ts">
	import { Input, Label } from 'flowbite-svelte';

	export let required: boolean | null | undefined;
	export let id: string;
	export let type:
		| 'number'
		| 'image'
		| 'text'
		| 'search'
		| 'time'
		| 'hidden'
		| 'color'
		| 'tel'
		| 'url'
		| 'email'
		| 'date'
		| 'datetime-local'
		| 'file'
		| 'month'
		| 'password'
		| 'reset'
		| 'submit'
		| 'week'
		| undefined = 'text';
	export let value: string;
	export let label: string;
	export let placeholder: string;
</script>

<div class="mb-6">
	<Label for={id} class="mb-2">{label}</Label>
	<Input {type} {id} {placeholder} {required} bind:value />
</div>
