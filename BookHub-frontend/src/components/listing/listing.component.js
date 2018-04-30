import React from 'react';
import PropTypes from 'prop-types';
import ListingItem from '../../components/listingItem/listingItem.component';
import './listing.styles.scss';

const list = (items) => {
	return items.map((book) => {
		return <ListingItem key={book.id} book={book} />;
	});
};

export default function Listing({items}) {
	return <div className='listing'>{list(items)}</div>;
}

Listing.propTypes = {
	items: PropTypes.array.isRequired
};
