import axios from 'axios';
import { ApiError, type Listing, type ListingDto, type User } from '$lib/types';

axios.defaults.withCredentials = true;

async function createListing(listingData: Listing): Promise<Listing> {
	const data: ListingDto = {
		...listingData,
		looking_for: listingData.lookingFor,
		lookingFor: undefined
	};

	try {
		const response = await axios.post('http://localhost:5000/listings', data);
		const newListing: Listing = response.data;

		return newListing;
	} catch (err) {
		if (axios.isAxiosError(err)) {
			throw ApiError.UNAUTHORIZED;
		} else {
			throw err;
		}
	}
}

async function getListing(listingId: number): Promise<Listing> {
	try {
		const response = await axios.get(`http://localhost:5000/listings/${listingId}`);
		const listing: Listing = response.data;
		return listing;
	} catch (err) {
		if (!axios.isAxiosError(err)) {
			throw err;
		}
		if (err.status === 401) {
			throw ApiError.UNAUTHORIZED;
		} else if (err.status === 404) {
			throw ApiError.NOT_FOUND;
		} else {
			throw err;
		}
	}
}

export default {
	createListing,
	getListing
};
