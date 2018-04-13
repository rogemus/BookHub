import React, { Component } from 'react';
import Listing from '../listing/listing.container';

class HomePage extends Component {
	render() {
		return (
			<div>
				<h1>Home</h1>
				<Listing />
			</div>
		);
	}
}

export default HomePage;

