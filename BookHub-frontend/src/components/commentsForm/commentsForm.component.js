import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import PropTypes from 'prop-types';

export default class CommentsForm extends React.Component {
	render() {
		return (
			<Form onSubmit={this.props.handleSubmit}>
				<Form.TextArea onChange={this.props.handleChange} value={this.props.value} />
				<Button content='Add Comment' labelPosition='left' icon='edit' primary />
			</Form>
		);
	}
}

CommentsForm.propTypes = {
	handleChange: PropTypes.func.isRequired,
	handleSubmit: PropTypes.func.isRequired,
	value: PropTypes.string.isRequired
};
