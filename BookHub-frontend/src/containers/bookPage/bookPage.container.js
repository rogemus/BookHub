import React, {Component} from 'react';
import {connect} from 'react-redux';
import {getBook} from '../../actions/book.action';
import isEmpty from 'lodash/isEmpty';
import BookDetails from '../../components/bookDetails/bookDetails.componnet';

class BookPage extends Component {
	componentDidMount() {
		this.props.getBook(this.props.match.params.id);
	}

	renderBookDetails() {
		if (!isEmpty(this.props.book)) {
			this.updatePageTitle();

			return <BookDetails book={this.props.book}/>;
		}
	}

	updatePageTitle() {
		document.title = `BookHub | ${this.props.book.title}`;
	}

	render() {
		return (
			<div>
				{this.renderBookDetails()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		book: state.book.bookData
	};
}

export default connect(mapStateToProps, {getBook})(BookPage);

