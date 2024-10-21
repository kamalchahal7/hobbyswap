import { useWritable } from '$lib/hooks/use-shared-store';

export const useLoading = (name: string) => useWritable<boolean>(`loading-${name}`, true);

interface ImageLoaderState {
	[src: string]: boolean;
}

export const useImageLoader = () => {
	const { subscribe, update } = useWritable<ImageLoaderState>('image-loader', {});

	return {
		subscribe,
		setLoading: (src: string) => update((state) => ({ ...state, [src]: false })),
		setLoaded: (src: string) => update((state) => ({ ...state, [src]: true })),
		reset: () => update(() => ({}))
	};
};
