import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { logOutUser } from '../../actions/authentication.actions';

class LogoutPage extends Component {
	componentDidMount() {
		document.title = 'BookHub | Log Out';

		this.props.logOutUser();
	}

	render() {
		return (
			<div>
				<h2> Bye Bye :* </h2>
				<h1> See you soon </h1>
			</div>
		);
	}
}

LogoutPage.propTypes = {
	logOutUser: PropTypes.func.isRequired
};

export default connect(null, {logOutUser})(LogoutPage);

