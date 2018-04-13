import React from 'react';
import PropTypes from 'prop-types';
import { Container } from 'semantic-ui-react';
import UserNav from '../userNav/userNav.component';
import Nav from '../nav/nav.component';
import './header.styles.css';

export default function Header({user}) {
	if (user) {
		return (
			<header className='header-main'>
				<Container text>
					<nav>
						<UserNav user={user}/>
					</nav>
				</Container>
			</header>
		);
	}

	return (
		<header className='header-main'>
			<Container text>
				<nav>
					<Nav />
				</nav>
			</Container>
		</header>
	);
}

Header.propTypes = {
	user: PropTypes.object
};
