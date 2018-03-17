import React from 'react';
import ReactDOM from 'react-dom';

import reduxThunk from 'redux-thunk';
import {createStore, applyMiddleware} from 'redux';
import reducers from './reducers';

const createStoreWithMiddleware = applyMiddleware(reduxThunk)(createStore);
const store = createStoreWithMiddleware(reducers);

import App from './containers/app.container';

ReactDOM.render(
	<App store={store}/>, document.getElementById('root')
);
