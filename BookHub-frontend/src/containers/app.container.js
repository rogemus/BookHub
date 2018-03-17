import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Provider} from 'react-redux';
import {Container} from 'semantic-ui-react';
import {
	BrowserRouter as Router,
	Route,
	Switch
} from 'react-router-dom';
import '../styles/main.css';
import 'semantic-ui-css/semantic.min.css';

import HomePage from './homePage/homePage.container';
import BookPage from './bookPage/bookPage.container';

const App = ({store}) => (
	<Provider store={store}>
		<Router>
			<Container text>
				<Switch>
					<Route exact path="/" component={HomePage}/>
					<Route path="/books/:id" component={BookPage}/>
				</Switch>
			</Container>
		</Router>
	</Provider>
);

App.propTypes = {
	store: PropTypes.object.isRequired
};

export default App;
