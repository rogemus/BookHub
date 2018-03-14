import React, {Component} from 'react';
import {connect} from 'react-redux';

class HomePage extends Component {
	renderBook() {
		return (
			<span>
				{this.props.activeBook.title}
			</span>
		);
	}

	render() {
		return (
			<div>
				<h1>Home</h1>
				{this.renderBook()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		activeBook: state.activeBook
	};
}

export default connect(mapStateToProps, null)(HomePage);

