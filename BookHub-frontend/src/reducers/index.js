import {
	combineReducers
} from 'redux';

import BookReducers from './book.reducer';

const rootReducer = combineReducers({
	book: BookReducers
});

export default rootReducer;
