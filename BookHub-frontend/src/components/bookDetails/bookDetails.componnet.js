import React from 'react';
import PropTypes from 'prop-types';
import {
	Grid,
	Image,
	Divider,
	Header
} from 'semantic-ui-react';

export default function BookDetails({book}) {
	return (
		<Grid divided='vertically'>
			<Grid.Row columns={2}>
				<Grid.Column>
					<Image src={book.image_url} />
				</Grid.Column>
				<Grid.Column>
					<Header as='h1'>{book.title}</Header>
					<Header as='h3'>{book.publisher.name}</Header>
					<Divider />
					<p>
						Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi aperiam culpa doloremque
						exercitationem id illum impedit laboriosam natus quo, reiciendis repellat ullam vel
						voluptatibus. Asperiores et iste labore praesentium quos!
					</p>
				</Grid.Column>
			</Grid.Row>
		</Grid>
	);
}

BookDetails.propTypes = {
	book: PropTypes.object.isRequired
};
