import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Provider} from 'react-redux';
import {
	BrowserRouter as Router,
	Route
} from 'react-router-dom';

import HomePage from './homePage/homePage.container';

const App = ({store}) => (
	<Provider store={store}>
		<Router>
			<Route path="/" component={HomePage}/>
		</Router>
	</Provider>
);

App.propTypes = {
	store: PropTypes.object.isRequired
};

export default App;
