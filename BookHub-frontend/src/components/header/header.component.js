import React from 'react';
import {Container} from 'semantic-ui-react';
import {Link} from 'react-router-dom';
import './header.styles.css';

const renderUserDetails = (user) => {
	return <p>user</p>;
};

const renderNav = () => {
	return (
		<nav>
			<ul>
				<li><Link to={'/'}>Home</Link></li>
				<li><Link to={'login'}>Login</Link></li>
				<li><Link to={'register'}>Register</Link></li>
			</ul>
		</nav>
	);
};

export default ({user}) => {
	if (user) {
		return (
			<header className='header-main'>
				<Container text>
					{renderUserDetails(user)}
				</Container>
			</header>
		);
	}

	return (
		<header className='header-main'>
			<Container text>
				{renderNav()}
			</Container>
		</header>
	);
};
