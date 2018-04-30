import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import './listingItem.styles.scss';

export default function ListingItem({book}) {
	return (
		<div className='listing-item'>
			<div className="listing-item-content">
				<div className="listing-item-img">
					<Link to={`books/${book.id}`}>
						<img src={book.image_url} alt={book.title} />
					</Link>
				</div>
				<div className="listing-item-header">
					<h3>
						<Link to={`books/${book.id}`}>{book.title}</Link>
					</h3>
				</div>
				<div className="listing-item-meta">
					{book.publisher.name}
				</div>
			</div>
		</div>
	);
}

ListingItem.propTypes = {
	book: PropTypes.object.isRequired
};
