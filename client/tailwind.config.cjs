import flowbitePlugin from 'flowbite/plugin';
/** @type {import('tailwindcss').Config} */
export default {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		'./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}',
		'./node_modules/flowbite-svelte-icons/**/*.{html,js,svelte,ts}'
	],
	darkMode: 'selector',
	theme: {
		extend: {
			fontFamily: {
				primary: ['Poppins', 'sans-serif']
			},
			colors: {
				// flowbite-svelte
				primary: {
					50: '#f0f9ff',
					100: '#e0f2fe',
					200: '#bae6fd',
					300: '#7dd3fc',
					400: '#38bdf8',
					500: '#0ea5e9',
					600: '#0284c7',
					700: '#0369a1',
					800: '#075985',
					900: '#0c4a6e'
				},
				russian_violet: {
					DEFAULT: '#3c1642',
					100: '#0c040d',
					200: '#18091a',
					300: '#240d27',
					400: '#2f1134',
					500: '#3c1642',
					600: '#752b81',
					700: '#af41c0',
					800: '#c980d5',
					900: '#e4c0ea'
				},
				carribean_blue: {
					DEFAULT: '#086375',
					100: '#021418',
					200: '#032830',
					300: '#053c48',
					400: '#07515f',
					500: '#086375',
					600: '#0da1bf',
					700: '#28cff0',
					800: '#70dff5',
					900: '#b7effa'
				},
				turquoise: {
					DEFAULT: '#1dd3b0',
					100: '#062a23',
					200: '#0c5446',
					300: '#117f69',
					400: '#17a98c',
					500: '#1dd3b0',
					600: '#41e5c4',
					700: '#70ecd3',
					800: '#a0f2e2',
					900: '#cff9f0'
				},
				green_yellow: {
					DEFAULT: '#affc41',
					100: '#253e01',
					200: '#497d02',
					300: '#6ebb03',
					400: '#93f904',
					500: '#affc41',
					600: '#befd66',
					700: '#cefd8c',
					800: '#dffeb3',
					900: '#effed9'
				},
				background: {
					DEFAULT: '#b2ff9e',
					100: '#115300',
					200: '#21a500',
					300: '#32f800',
					400: '#6fff4b',
					500: '#b2ff9e',
					600: '#c1ffb1',
					700: '#d0ffc5',
					800: '#e0ffd8',
					900: '#efffec'
				}
			}
		}
	},
	plugins: [flowbitePlugin]
};
