import React, {Component} from 'react';
import BooksListing from '../booksListing/booksListing.container';

class HomePage extends Component {
	componentDidMount() {
		document.title = 'BookHub | Home Page';
	}

	render() {
		return (
			<div>
				<h1>Home</h1>
				<BooksListing/>
			</div>
		);
	}
}

export default HomePage;

