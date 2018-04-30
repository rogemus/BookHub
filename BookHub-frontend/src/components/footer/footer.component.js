import React from 'react';
import { Link } from 'react-router-dom';

import './footer.styles.scss';

export default function Footer() {
	return (
		<footer className="footer">
			<div className="wrapper">
				<div className="footer-logo">
					<Link to={'/'}>BookHub</Link>
				</div>
				<div className="footer-copy">
					&copy; 2018 <a href="mailto:kacper.rogowski@outlook.com">Kacper Rogowski</a>
				</div>

			</div>
		</footer>
	);
}
