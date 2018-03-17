import React, {Component} from 'react';
import {connect} from 'react-redux';
import {getBook} from '../../actions/book.action';

class BookPage extends Component {
	componentDidMount() {
		this.bookID = this.props.match.params.id;
	}

	render() {
		return (
			<div>
				<h1>Book</h1>
				{this.bookID}
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

