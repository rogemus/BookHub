import React, {Component} from 'react';
import {connect, Provider} from 'react-redux';
import {Container} from 'semantic-ui-react';
import {
	HashRouter as Router,
	Route,
	Switch
} from 'react-router-dom';
import '../styles/main.css';
import 'semantic-ui-css/semantic.min.css';

import HomePage from './homePage/homePage.container';
import BookPage from './bookPage/bookPage.container';
import RegisterPage from './registerPage/registerPage.container';
import LoginPage from './loginPage/loginPage.container';

import ErrorsNotification from '../components/errorNotification/errorNotification.component';
import {clearErrors} from '../actions/errors.actions';

class App extends Component {
	handleErrorClick() {
		this.props.clearErrors();
	}

	render() {
		return (
			<Provider store={this.props.store}>
				<Router>
					<Container text>
						<Switch>
							<Route exact path="/" component={HomePage}/>
							<Route path="/books/:id" component={BookPage}/>
							<Route exact path="/register" component={RegisterPage}/>
							<Route exact path="/login" component={LoginPage}/>
						</Switch>

						<ErrorsNotification
							errors={this.props.errorContent}
							onCloseClick={this.handleErrorClick.bind(this)}/>
					</Container>
				</Router>
			</Provider>
		);
	}
}

function mapStateToProps(state) {
	return {
		errorContent: state.errors.errorContent
	};
}

export default connect(mapStateToProps, {clearErrors})(App);


