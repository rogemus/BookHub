import React, {Component} from 'react';
import BooksListing from '../booksListing/booksListing.container';
import RegisterPage from '../registerPage/registerPage.container';

class HomePage extends Component {
	render() {
		return (
			<div>
				<h1>Home</h1>
				<BooksListing/>
				<RegisterPage/>
			</div>
		);
	}
}

export default HomePage;

