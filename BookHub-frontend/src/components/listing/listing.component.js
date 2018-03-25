import React from 'react';
import './listing.styles.css';
import ListingItem from '../../components/listingItem/listingItem.component';

const list = (items) => {
	return items.map((book) => {
		return (
			<div key={book.id} className="listing-item">
				<ListingItem book={book}/>
			</div>
		);
	});
};

export default ({items}) => {
	return (<div className='listing'>{list(items)}</div>);
};
