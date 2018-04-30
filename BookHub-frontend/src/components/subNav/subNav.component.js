import React from 'react';
import PropTypes from 'prop-types';
import UserNav from '../userNav/userNav.component';
import Nav from '../nav/nav.component';

export default function SubNav(props) {
	if (props.isUserLogin) {
		return <UserNav user={props.user} />;
	}

	return <Nav />;
}

SubNav.propTypes = {
	user: PropTypes.object.isRequired,
	isUserLogin: PropTypes.bool.isRequired
};
