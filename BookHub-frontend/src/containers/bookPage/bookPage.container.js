import React, {Component} from 'react';
import {connect} from 'react-redux';
import {getBook} from '../../actions/book.action';

class BookPage extends Component {
	componentDidMount() {
		this.props.getBook(this.props.match.params.id);
	}

	renderBook() {
		if (this.props.book) {
			this.showBook = true;
		}
	}

	render() {
		return (
			<div>
				<h1>Book</h1>
				{this.showBook}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		book: state.book
	};
}

export default connect(mapStateToProps, {getBook})(BookPage);

