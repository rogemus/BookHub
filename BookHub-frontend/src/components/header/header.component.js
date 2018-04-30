import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import SubNav from '../subNav/subNav.component';

import './heade.styles.scss';

export default function Header(props) {
	return (
		<header className='header-main'>
			<div className="header-sub">
				<div className="wrapper">
					<SubNav isUserLogin={props.isUserLogin} user={props.user} />
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
							<li><Link to={'/'}>Page 2</Link></li>
							<li><Link to={'/'}>Page 3</Link></li>
							<li><Link to={'/'}>Page 4</Link></li>
							<li><Link to={'/'}>Page 5</Link></li>
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
