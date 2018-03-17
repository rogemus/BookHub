import {
	combineReducers
} from 'redux';

import ActiveBookReducers from './activeBook.reducer';
import BookReducers from './book.reducer';

const rootReducer = combineReducers({
	activeBook: ActiveBookReducers,
	book: BookReducers
});

export default rootReducer;
