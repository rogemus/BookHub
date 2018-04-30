import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

export default function UserNav({user}) {
	return (
		<ul>
			<li><Link to={'/me'}>{user.username}</Link></li>
			<li><Link to={'/logout'}>Sign Out</Link></li>
		</ul>
	);
}

UserNav.propTypes = {
	user: PropTypes.object.isRequired
};
