import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import _isEmpty from 'lodash/isEmpty';
import { getCurrentUserData } from '../../actions/user.actions';
import UserDetails from '../../components/userDetails/userDetails.component';

class CurrentUserPage extends Component {
	componentDidMount() {
		document.title = 'BookHub | Me';

		this.props.getCurrentUserData(this.props.token);
	}

	renderUserDetails() {
		if (!_isEmpty(this.props.userData)) {
			return <UserDetails userData={this.props.userData} />;
		}
	}

	render() {
		return (
			<div>
				{this.renderUserDetails()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		userData: state.user.userData,
		token: state.authentication.token
	};
}

CurrentUserPage.propTypes = {
	token: PropTypes.string.isRequired,
	userData: PropTypes.object.isRequired,
	getCurrentUserData: PropTypes.func.isRequired
};

export default connect(mapStateToProps, {getCurrentUserData})(CurrentUserPage);

