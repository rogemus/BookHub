import React from 'react';
import { Comment, Header } from 'semantic-ui-react';
import PropTypes from 'prop-types';
import CommentsForm from '../commentsForm/commentsForm.component';
import CommentsListItem from '../commentsListItem/commentsListItem.component';

export default class CommentsList extends React.Component {
	renderList() {
		return this.props.commentsList.map((comment) => <CommentsListItem key={comment.id} comment={comment} />);
	}

	render() {
		return (
			<Comment.Group>
				<Header as='h3' dividing>Comments</Header>
				{this.renderList()}
				<CommentsForm onSubmit={this.props.onSubmit} />
			</Comment.Group>
		);
	}
}

CommentsList.propTypes = {
	commentsList: PropTypes.array.isRequired,
	onSubmit: PropTypes.func.isRequired
};
