import React from 'react';
import PropTypes from 'prop-types';

export default class CommentsListItem extends React.Component {
	renderDate(submit_date) {
		const date = new Date(submit_date);

		return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
	}

	render() {
		return (
			<div className='comment'>
				<div className='comment-header'>
					<div className='comment-author'>
						{this.props.comment.author}
					</div>
					<div className="comment-metadata">
						{this.renderDate(this.props.comment.submit_date)}
					</div>
				</div>
				<div className="comment-content">
					{this.props.comment.text}
				</div>
			</div>
		);
	}
}

CommentsListItem.propTypes = {
	comment: PropTypes.object.isRequired
};
