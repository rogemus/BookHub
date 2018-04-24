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
			return <CommentsList
				user={this.props.currentUser}
				commentsList={this.props.commentsList}
				onSubmit={this.handleCommentsSubmit} />;
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
		commentsList: state.comments.list,
		currentUser: state.user.current
	};
}

BookPage.propTypes = {
	getBook: PropTypes.func.isRequired,
	getComments: PropTypes.func.isRequired,
	currentUser: PropTypes.object.isRequired,
	book: PropTypes.object.isRequired,
	match: PropTypes.object.isRequired,
	commentsList: PropTypes.array.isRequired
};

export default connect(mapStateToProps, {getBook, getComments})(BookPage);

