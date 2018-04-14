import React from 'react';
import PropTypes from 'prop-types';
import ListingItem from '../../components/listingItem/listingItem.component';
import './listing.styles.css';

const list = (items) => {
	return items.map((book) => {
		return (
			<div key={book.id} className="listing-item">
				<ListingItem book={book} />
			</div>
		);
	});
};

export default function Listing({items}) {
	return (<div className='listing'>{list(items)}</div>);
}

Listing.propTypes = {
	items: PropTypes.array.isRequired
};
