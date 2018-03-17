import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class HomePage extends Component {
	render() {
		return (
			<div>
				<h1>Home</h1>
				<p>
					<Link to="/books/153d69ac-8b9b-41e9-977c-4721be05d367">Book page</Link>
				</p>
			</div>
		);
	}
}

export default HomePage;

