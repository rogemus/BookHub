import React from 'react';
import map from 'lodash/map';
import isEmpty from 'lodash/isEmpty';
import PropTypes from 'prop-types';
import './errorNotification.styles.scss';

export default class ErrorNotification extends React.Component {
	renderErrors() {
		if (this.props.errors && !isEmpty(this.props.errors)) {
			const content = this.parserErrors();

			setTimeout(() => {
				this.props.onCloseClick();
			}, 5000);

			return (
				<div className='error-notification'>
					<div onClick={this.props.onCloseClick} className="error-notification-close">
						x
					</div>
					<div className="error-notification-header">
						<h4>Error !</h4>
					</div>
					<div className="error-notification-content">
						{content}
					</div>
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
	errors: PropTypes.object,
	onCloseClick: PropTypes.func.isRequired
};
