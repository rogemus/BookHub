import {
	combineReducers
} from 'redux';

import ActiveBookReducers from './activeBook.reducer';

const rootReducer = combineReducers({
	activeBook: ActiveBookReducers
});

export default rootReducer;
