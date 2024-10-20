import { useWritable } from '$lib/hooks/use-shared-store';

export const useUser = () => useWritable<User | null>('user', null);
