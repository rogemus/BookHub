import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { Icon } from 'semantic-ui-react';

export default function UserNav({user}) {
	return (
		<ul className='align-right'>
			<li><Link to={'/me'}><Icon name="user" />{user.username}</Link></li>
			<li><Link to={'/logout'}><Icon name="sign out" />Sign Out</Link></li>
		</ul>
	);
}

UserNav.propTypes = {
	user: PropTypes.object.isRequired
};
