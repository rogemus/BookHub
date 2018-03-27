import React from 'react';
import {Container} from 'semantic-ui-react';
import {Link} from 'react-router-dom';
import './header.styles.css';

const renderUserDetails = (user) => {
	return (
		<ul className='align-right'>
			<li><Link to={'/me'}>{user.username}</Link></li>
		</ul>
	);
};

const renderNav = () => {
	return (
		<ul>
			<li><Link to={'/'}>Home</Link></li>
			<li><Link to={'login'}>Login</Link></li>
			<li><Link to={'register'}>Register</Link></li>
		</ul>
	);
};

export default ({user}) => {
	if (user) {
		return (
			<header className='header-main'>
				<Container text>
					<nav>
						<ul>
							{renderUserDetails(user)}
						</ul>
					</nav>
				</Container>
			</header>
		);
	}

	return (
		<header className='header-main'>
			<Container text>
				<nav>
					{renderNav()}
				</nav>
			</Container>
		</header>
	);
};
