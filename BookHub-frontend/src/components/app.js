import React, {Component} from 'react';
import BooksList from '../containers/books-list';
import BookDetail from '../containers/book-detail';
import '../styles/main.css';

export default class App extends Component {
	render() {
		return (
			<div>
				<BooksList/>
				<BookDetail/>
			</div>
		);
	}
}
