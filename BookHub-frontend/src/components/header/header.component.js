import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import UserNav from '../userNav/userNav.component';
import Nav from '../nav/nav.component';

import './heade.styles.scss';

export default function Header(props) {
	function renderSubNav(props) {
		if (props.isUserLogin) {
			return <Nav />;
		} else {
			return <UserNav user={props.user} />;
		}
	}

	return (
		<header className='header-main'>
			<div className="header-sub">
				<div className="wrapper">
					{renderSubNav(props)}
				</div>
			</div>

			<div className="header-nav">
				<div className="wrapper">
					<div className="header-logo">
						<Link to={'/'}>BookHub</Link>
					</div>
					<nav className="nav-main">
						<ul>
							<li><Link to={'/'}>Home</Link></li>
							<li><Link to={'/'}>Categories</Link></li>
							<li><Link to={'/'}>Contact</Link></li>
						</ul>
					</nav>
				</div>
			</div>
		</header>
	);
}

Header.propTypes = {
	user: PropTypes.object.isRequired,
	isUserLogin: PropTypes.bool.isRequired
};
