import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

export default function UserNav({user}) {
	return (
		<ul className='align-right'>
			<li><Link to={'/me'}>{user.username}</Link></li>
		</ul>
	);
}

UserNav.propTypes = {
	user: PropTypes.object.isRequired
};
