import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import PropTypes from 'prop-types';

export default class CommentsForm extends React.Component {
	render() {
		return (
			<Form onSubmit={this.props.onSubmit}>
				<Form.TextArea />
				<Button content='Add Comment' labelPosition='left' icon='edit' primary />
			</Form>
		);
	}
}

CommentsForm.propTypes = {
	onSubmit: PropTypes.func.isRequired
};
