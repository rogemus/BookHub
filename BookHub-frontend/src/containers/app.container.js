import React, { Component } from 'react';
import { connect, Provider } from 'react-redux';
import { Container } from 'semantic-ui-react';
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
import LogoutPage from './logoutPage/logoutPage.container';
import CurrentUserPage from './currentUserPage/currentUserPage.container';

import { LOGIN, SET_CURRENT_USER, SET_TOKEN } from '../actions/types';

import ErrorsNotification from '../components/errorNotification/errorNotification.component';
import Header from '../components/header/header.component';
import { clearErrors } from '../actions/errors.actions';

import 'semantic-ui-css/semantic.min.css';
import '../styles/main.css';

class App extends Component {
	componentWillMount() {
		this.populateUser();
	}

	handleErrorClick() {
		this.props.clearErrors();
	}

	populateUser() {
		const token = JSON.parse(localStorage.getItem('token'));
		const current_user = JSON.parse(localStorage.getItem('currentUser'));
		const isUserLogin = JSON.parse(localStorage.getItem('isUserLogin'));

		if (isUserLogin) {
			this.props.store.dispatch({
				type: LOGIN,
				payload: isUserLogin
			});

			this.props.store.dispatch({
				type: SET_TOKEN,
				payload: token
			});

			this.props.store.dispatch({
				type: SET_CURRENT_USER,
				payload: current_user
			});
		}
	}

	render() {
		return (
			<Provider store={this.props.store}>
				<Router>
					<div>
						<Header isUserLogin={this.props.isUserLogin} user={this.props.currentUser} />

						<Container text>
							<Switch>
								<Route exact path="/" component={HomePage} />
								<Route path="/listing" component={ListingPage} />
								<Route path="/books/:id" component={BookPage} />
								<Route exact path="/register" component={RegisterPage} />
								<Route exact path="/login" component={LoginPage} />
								<Route exact path="/logout" component={LogoutPage} />
								<Route exact path="/me" component={CurrentUserPage} />
							</Switch>

							<ErrorsNotification
								errors={this.props.errorContent}
								onCloseClick={this.handleErrorClick.bind(this)}
							/>
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
		currentUser: state.user.current,
		isUserLogin: state.authentication.isLogin
	};
}

App.propTypes = {
	errorContent: PropTypes.object.isRequired,
	isUserLogin: PropTypes.bool.isRequired,
	currentUser: PropTypes.object.isRequired,
	store: PropTypes.object.isRequired,
	clearErrors: PropTypes.func.isRequired
};

export default connect(mapStateToProps, {clearErrors})(App);


