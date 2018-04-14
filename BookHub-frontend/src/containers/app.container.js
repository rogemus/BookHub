import React, {Component} from 'react';
import {connect, Provider} from 'react-redux';
import {Container} from 'semantic-ui-react';
import PropTypes from 'prop-types';
import {
	HashRouter as Router,
	Route,
	Switch
} from 'react-router-dom';

import HomePage from './homePage/homePage.container';
import BookPage from './bookPage/bookPage.container';
import ListingPage from './listingPage/listingPage.container';
import RegisterPage from './registerPage/registerPage.container';
import LoginPage from './loginPage/loginPage.container';

import ErrorsNotification from '../components/errorNotification/errorNotification.component';
import Header from '../components/header/header.component';
import {clearErrors} from '../actions/errors.actions';

import 'semantic-ui-css/semantic.min.css';
import '../styles/main.css';

class App extends Component {
	handleErrorClick() {
		this.props.clearErrors();
	}

	render() {
		return (
			<Provider store={this.props.store}>
				<Router>
					<div>
						<Header user={this.props.currentUser}/>

						<Container text>
							<Switch>
								<Route exact path="/" component={HomePage}/>
								<Route path="/listing" component={ListingPage}/>
								<Route path="/books/:id" component={BookPage}/>
								<Route exact path="/register" component={RegisterPage}/>
								<Route exact path="/login" component={LoginPage}/>
							</Switch>

							<ErrorsNotification
								errors={this.props.errorContent}
								onCloseClick={this.handleErrorClick.bind(this)}/>
						</Container>
					</div>
				</Router>
			</Provider>
		);
	}
}

function mapStateToProps(state) {
	return {
		errorContent: state.errors.errorContent,
		currentUser: state.user.current
	};
}

App.propTypes = {
	errorContent: PropTypes.object,
	currentUser: PropTypes.object,
	store: PropTypes.object.isRequired,
	clearErrors: PropTypes.func.isRequired
};

export default connect(mapStateToProps, {clearErrors})(App);


