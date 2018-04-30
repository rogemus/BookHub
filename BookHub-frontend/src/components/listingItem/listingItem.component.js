import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

export default function ListingItem({book}) {
	return (
		<div className='listing-item'>
			<div className="listing-item-content">
				<div className="listing-item-img">
					<img src={book.image_url} alt={book.title} />
				</div>
				<div className="listing-item-header">
					<h2>
						<Link to={`books/${book.id}`}>{book.title}</Link>
					</h2>
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
