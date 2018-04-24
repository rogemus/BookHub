import React from 'react';
import { Comment } from 'semantic-ui-react';
import PropTypes from 'prop-types';

export default class CommentsListItem extends React.Component {
	renderDate(submit_date) {
		const date = new Date(submit_date);

		return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
	}

	render() {
		return (
			<Comment>
				<Comment.Content>
					<Comment.Author as='a'>
						{this.props.comment.author}
					</Comment.Author>
					<Comment.Metadata>
						<div>{this.renderDate(this.props.comment.submit_date)}</div>
					</Comment.Metadata>
					<Comment.Text>
						{this.props.comment.text}
					</Comment.Text>
				</Comment.Content>
			</Comment>
		);
	}
}

CommentsListItem.propTypes = {
	comment: PropTypes.object.isRequired
};
