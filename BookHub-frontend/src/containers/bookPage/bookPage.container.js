import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import isEmpty from 'lodash/isEmpty';
import { getBook } from '../../actions/book.actions';
import BookDetails from '../../components/bookDetails/bookDetails.componnet';

class BookPage extends Component {
	componentDidMount() {
		this.props.getBook(this.props.match.params.id);
	}

	renderBookDetails() {
		if (!isEmpty(this.props.book)) {
			this.updatePageTitle();

			return <BookDetails book={this.props.book}/>;
		}
	}

	updatePageTitle() {
		document.title = `BookHub | ${this.props.book.title}`;
	}

	render() {
		return (
			<div>
				{this.renderBookDetails()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		book: state.book.bookData
	};
}

BookPage.propTypes = {
	getBook: PropTypes.func,
	book: PropTypes.object,
	match: PropTypes.object
};

export default connect(mapStateToProps, {getBook})(BookPage);

