import React from 'react';
import {Link} from 'react-router-dom';
import {
	Card
} from 'semantic-ui-react';

const bookTitle = (id, title) => {
	return (
		<Link to={`books/${id}`}>{title}</Link>
	);
};

export default ({book}) => {
	return (
		<Card
			image={book.image_url}
			header={bookTitle(book.id, book.title)}
			meta={book.publisher.name}
		/>
	);
};
