import React, {Component} from 'react';
import {connect} from 'react-redux';
import {getBooks} from '../../actions/books.actions';
import isEmpty from 'lodash/isEmpty';
import './listing.styles.css';
import ListingItem from '../../components/listingItem/listingItem.component';

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

export default connect(mapStateToProps, {getBooks})(BookListing);

