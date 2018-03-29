import {
	combineReducers
} from 'redux';

import BookReducers from './book.reducer';
import BooksReducers from './books.reducer';
import AuthenticationReducer from './authentication.reducer';
import ErrorsReducer from './errors.reducers';

const rootReducer = combineReducers({
	book: BookReducers,
	books: BooksReducers,
	authentication: AuthenticationReducer,
	errors: ErrorsReducer
});

export default rootReducer;
