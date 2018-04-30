import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import './bookDetails.styles.scss';

const authors = (authors) => {
	return (
		authors.map((author) => {
			return (
				<span key={author.id}>
					<Link to={`/listing?authors=${author.id}`}>{`${author.first_name} ${author.last_name}`}</Link>
				</span>
			);
		})
	);
};

export default function BookDetails({book}) {
	return (
		<div className='book-details'>
			<div className="book-details-main-title">
				<h1>
					{book.title}
				</h1>
			</div>
			<div className="book-details-content">
				<div className="book-details-img">
					<img src={book.image_url} alt={book.title} />
				</div>
				<div className="book-details-info">
					<div className="book-details-info-title">
						<h2>
							{book.title}
						</h2>

						<div className="book-details-publishers">
							<h5>
								Publisher:
							</h5>
							<span>
								{book.publisher.name}
							</span>
						</div>

						<div className="book-details-authors">
							<h5>
								Authors:
							</h5>
							<span>
								{authors(book.authors)}
							</span>
						</div>
					</div>
					<div className="book-details-info-desc">
						<h5>
							Short Description
						</h5>
						<p>
							Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi aperiam culpa doloremque
							exercitationem id illum impedit laboriosam natus quo, reiciendis repellat ullam vel
							voluptatibus. Asperiores et iste labore praesentium quos!
						</p>
					</div>
				</div>
			</div>

			<div className="book-details-long-desc">
				<h2>
					Description
				</h2>
				<p>
					Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur debitis doloremque doloribus
					quia quibusdam totam veniam. Aliquam consectetur cum dicta eaque facilis fugiat iure minus
					necessitatibus recusandae sunt? Asperiores, veritatis.
					Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur debitis doloremque doloribus
					quia
					quibusdam totam veniam. Aliquam consectetur cum dicta eaque facilis fugiat iure minus necessitatibus
					recusandae sunt? Asperiores, veritatis.
				</p>
				<p>
					Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur debitis doloremque doloribus
					quia
					quibusdam totam veniam. Aliquam consectetur cum dicta eaque facilis fugiat iure minus necessitatibus
					recusandae sunt? Asperiores, veritatis.
				</p>
				<p>
					Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur debitis doloremque doloribus
					quia
					quibusdam totam veniam. Aliquam consectetur cum dicta eaque facilis fugiat iure minus necessitatibus
					recusandae sunt? Asperiores, veritatis.
				</p>
			</div>
		</div>
	);
}

BookDetails.propTypes = {
	book: PropTypes.object.isRequired
};
