import React from 'react';
import { Link } from 'react-router-dom';

export default function Nav() {
	return (
		<ul>
			<li><Link to={'/login'}>Sign in</Link></li>
			<li><Link to={'/register'}>Register</Link></li>
		</ul>
	);
}
