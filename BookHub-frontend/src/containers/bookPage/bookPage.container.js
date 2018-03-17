import React, {Component} from 'react';
import {connect} from 'react-redux';
import {getBook} from '../../actions/book.action';
import {Container} from 'semantic-ui-react';
import isEmpty from 'lodash/isEmpty';
import BookDetails from '../../components/bookDetails/bookDetails.componnet';

class BookPage extends Component {
	componentDidMount() {
		this.props.getBook(this.props.match.params.id);
	}

	renderBookDetails() {
		if (!isEmpty(this.props.book)) {
			return <BookDetails book={this.props.book}/>;
		}
	}

	render() {
		return (
			<Container text>
				{this.renderBookDetails()}
			</Container>
		);
	}
}

function mapStateToProps(state) {
	return {
		book: state.book.bookData
	};
}

export default connect(mapStateToProps, {getBook})(BookPage);

