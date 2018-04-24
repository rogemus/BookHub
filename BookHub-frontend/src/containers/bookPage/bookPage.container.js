import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import isEmpty from 'lodash/isEmpty';
import { getBook } from '../../actions/book.actions';
import { getComments } from '../../actions/comments.actions';
import BookDetails from '../../components/bookDetails/bookDetails.componnet';
import CommentsList from '../../components/commentsList/commentsList.component';

class BookPage extends Component {
	constructor(props) {
		super(props);

		this.handleCommentsSubmit = this.handleCommentsSubmit.bind(this);
	}

	componentDidMount() {
		this.props.getBook(this.props.match.params.id);
		this.props.getComments(this.props.match.params.id);
	}

	updatePageTitle() {
		document.title = `BookHub | ${this.props.book.title}`;
	}

	handleCommentsSubmit(e) {
		console.log(e);
	}

	renderBookDetails() {
		if (!isEmpty(this.props.book)) {
			this.updatePageTitle();

			return <BookDetails book={this.props.book} />;
		}
	}

	renderComments() {
		if (!isEmpty(this.props.commentsList)) {
			return <CommentsList commentsList={this.props.commentsList} onSubmit={this.handleCommentsSubmit} />;
		}
	}

	render() {
		return (
			<div>
				{this.renderBookDetails()}
				{this.renderComments()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		book: state.book.bookData,
		commentsList: state.comments.list
	};
}

BookPage.propTypes = {
	getBook: PropTypes.func,
	getComments: PropTypes.func,
	book: PropTypes.object,
	match: PropTypes.object,
	commentsList: PropTypes.array
};

export default connect(mapStateToProps, {getBook, getComments})(BookPage);

