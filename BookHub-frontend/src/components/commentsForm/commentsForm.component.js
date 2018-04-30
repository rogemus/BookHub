import React from 'react';
import PropTypes from 'prop-types';

export default class CommentsForm extends React.Component {
	render() {
		return (
			<form onSubmit={this.props.handleSubmit} className="form">
				<textarea onChange={this.props.handleChange} placeholder="Insert your comment here">
				</textarea>
				<button className="btn">
					Add Comment
				</button>
			</form>
		);
	}
}

CommentsForm.propTypes = {
	handleChange: PropTypes.func.isRequired,
	handleSubmit: PropTypes.func.isRequired,
	value: PropTypes.string.isRequired
};
