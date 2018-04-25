import React from 'react';
import { Link } from 'react-router-dom';
import { Icon } from 'semantic-ui-react';

export default function Nav() {
	return (
		<ul>
			<li><Link to={'/'}><Icon name="home" /> Home</Link></li>
			<li><Link to={'/login'}><Icon name="sign in" /> Sign in</Link></li>
			<li><Link to={'/register'}><Icon name="add user " /> Register</Link></li>
		</ul>
	);
}
