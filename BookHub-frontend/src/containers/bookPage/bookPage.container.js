import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import isEmpty from 'lodash/isEmpty';
import { getBook } from '../../actions/book.actions';
import { getComments, createComment } from '../../actions/comments.actions';
import BookDetails from '../../components/bookDetails/bookDetails.componnet';
import CommentsList from '../../components/commentsList/commentsList.component';

class BookPage extends Component {
	constructor(props) {
		super(props);

		this.state = {
			commentContent: ''
		};
	}

	componentDidMount() {
		this.props.getBook(this.props.match.params.id);
		this.props.getComments(this.props.match.params.id);
	}

	updatePageTitle() {
		document.title = `BookHub | ${this.props.book.title}`;
	}

	handleCommentsSubmit() {
		this.props.createComment(this.props.match.params.id, this.state.commentContent, this.props.token)
			.then(() => this.props.getComments(this.props.match.params.id));
	}

	handleCommentChange(e) {
		this.setState({commentContent: e.target.value});
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
				value={this.state.commentContent}
				isUserLogin={this.props.isUserLogin}
				commentsList={this.props.commentsList}
				handleChange={this.handleCommentChange.bind(this)}
				handleSubmit={this.handleCommentsSubmit.bind(this)} />;
		}
	}

	render() {
		return (
			<div className='page-container'>
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
		currentUser: state.user.current,
		isUserLogin: state.authentication.isLogin,
		token: state.authentication.token
	};
}

BookPage.propTypes = {
	getBook: PropTypes.func.isRequired,
	getComments: PropTypes.func.isRequired,
	createComment: PropTypes.func.isRequired,
	currentUser: PropTypes.object.isRequired,
	token: PropTypes.string.isRequired,
	isUserLogin: PropTypes.bool.isRequired,
	book: PropTypes.object.isRequired,
	match: PropTypes.object.isRequired,
	commentsList: PropTypes.array.isRequired
};

export default connect(mapStateToProps, {getBook, getComments, createComment})(BookPage);

