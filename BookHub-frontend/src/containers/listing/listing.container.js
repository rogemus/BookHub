import React, {Component} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import isEmpty from 'lodash/isEmpty';
import {getBooks} from '../../actions/books.actions';
import ListingItem from '../../components/listingItem/listingItem.component';
import './listing.styles.css';

class BookListing extends Component {
	componentDidMount() {
		this.props.getBooks();
	}

	renderListing() {
		if (!isEmpty(this.props.books)) {
			return this.props.books.map((book) => {
				return <ListingItem book={book} key={book.id}/>;
			});
		}
	}

	render() {
		return (
			<div className='listing'>
				{this.renderListing()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		books: state.books.booksList
	};
}

BookListing.propTypes = {
	books: PropTypes.array,
	getBooks: PropTypes.func
};

export default connect(mapStateToProps, {getBooks})(BookListing);

