import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';
import {
	Card
} from 'semantic-ui-react';

export default function ListingItem({book}){
	return (
		<div className='listing-item'>
			<Card
				image={book.image_url}
				header={<Link to={`books/${book.id}`}>{book.title}</Link>}
				meta={book.publisher.name}
			/>
		</div>
	);
}

ListingItem.propTypes = {
	book: PropTypes.object.isRequired
};
