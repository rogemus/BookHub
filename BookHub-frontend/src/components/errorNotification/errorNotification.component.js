import React from 'react';
import map from 'lodash/map';
import isEmpty from 'lodash/isEmpty';
import { Message } from 'semantic-ui-react';
import PropTypes from 'prop-types';

export default class ErrorNotification extends React.Component {
	renderErrors() {
		if (this.props.errors && !isEmpty(this.props.errors)) {
			const content = this.parserErrors();

			return (
				<div className='error-notification'>
					<Message
						color='red'
						icon='attention'
						onDismiss={this.props.onCloseClick}
						header='Error !'
						content={content}
					/>
				</div>
			);
		}
	}

	parserErrors() {
		return (
			<div>
				{map(this.props.errors, (error, index) => {
					return <p key={index}>{error}</p>;
				})}
			</div>
		);
	}

	render() {
		return (
			<div>
				{this.renderErrors()}
			</div>
		);
	}
}

ErrorNotification.propTypes = {
	errors: PropTypes.object.isRequired,
	onCloseClick: PropTypes.func.isRequired
};
