import React, { Component } from 'react';
import PropTypes from 'prop-types';
import isEmpty from 'lodash/isEmpty';
import { connect } from 'react-redux';
import { getBooks } from '../../actions/books.actions';
import Listing from '../../components/listing/listing.component';

class HomePage extends Component {
	componentDidMount() {
		document.title = 'BookHub | Home Page';

		this.props.getBooks();
	}

	renderList() {
		if (!isEmpty(this.props.books)) {
			return <Listing items={this.props.books} />;
		}
	}

	render() {
		return (
			<div>
				<h1> Home </h1>
				{this.renderList()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		books: state.books.booksList
	};
}

HomePage.propTypes = {
	books: PropTypes.array,
	getBooks: PropTypes.func.isRequired
};

export default connect(mapStateToProps, {getBooks})(HomePage);

