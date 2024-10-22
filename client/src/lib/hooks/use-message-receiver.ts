import type { User } from '$lib/types/app.d';
import { useWritable } from '$lib/hooks/use-shared-store';

export const useMessageReceiver = () => useWritable<User | null>('message-receiver', null);
