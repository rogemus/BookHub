import React from 'react';
import isEmpty from 'lodash/isEmpty';
import { Comment, Header } from 'semantic-ui-react';
import PropTypes from 'prop-types';
import CommentsForm from '../commentsForm/commentsForm.component';
import CommentsListItem from '../commentsListItem/commentsListItem.component';

export default class CommentsList extends React.Component {
	renderList() {
		return this.props.commentsList.map((comment) => <CommentsListItem key={comment.id} comment={comment} />);
	}

	renderForm() {
		if (!isEmpty(this.props.user)) {
			return <CommentsForm onSubmit={this.props.onSubmit} />;
		}
	}

	render() {
		return (
			<Comment.Group>
				<Header as='h3' dividing>Comments</Header>
				{this.renderList()}
				{this.renderForm()}
			</Comment.Group>
		);
	}
}

CommentsList.propTypes = {
	onSubmit: PropTypes.func.isRequired,
	commentsList: PropTypes.array.isRequired,
	user: PropTypes.object.isRequired
};
