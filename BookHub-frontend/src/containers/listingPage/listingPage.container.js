import React, { Component } from 'react';
import PropTypes from 'prop-types';
import isEmpty from 'lodash/isEmpty';
import { connect } from 'react-redux';
import { queryStringToJSON } from '../../helpers/query';
import { getBooks } from '../../actions/books.actions';
import Listing from '../../components/listing/listing.component';

class ListingPage extends Component {
	constructor(props) {
		super(props);

		this.queryParams = queryStringToJSON(this.props.location.search);
	}

	componentDidMount() {
		document.title = 'BookHub | Listing';

		this.props.getBooks(this.queryParams);
	}

	renderList() {
		if (!isEmpty(this.props.books)) {
			return <Listing items={this.props.books} />;
		}
	}

	render() {
		return (
			<div>
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

ListingPage.propTypes = {
	books: PropTypes.array,
	getBooks: PropTypes.func.isRequired,
	location: PropTypes.object.isRequired
};

export default connect(mapStateToProps, {getBooks})(ListingPage);

