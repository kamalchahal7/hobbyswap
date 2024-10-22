import { ApiError, type Listing } from '$lib/types';
import type { Load } from '@sveltejs/kit';
import listingService from '$lib/services/listing-service';
import { error } from '@sveltejs/kit';
import { goto } from '$app/navigation';
export const load: Load = async ({ fetch, params }) => {
	try {
		console.log(params.listing_id);
		const res = await fetch(`http://localhost:5000/listings/${parseInt(params.listing_id!)}`);
		const listing: Listing = await res.json();
		console.log(listing);
		return {
			listing: listing
		};
	} catch (err) {
		switch (err) {
			case ApiError.UNAUTHORIZED:
				goto('/auth/login');
				break;
			case ApiError.NOT_FOUND:
				error(404, 'Not Found');
				break;
			default:
				console.error(err);
				error(500, `${err}`);
		}
	}
};
