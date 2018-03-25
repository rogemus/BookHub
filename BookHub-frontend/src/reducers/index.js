import {
	combineReducers
} from 'redux';

import BookReducers from './book.reducer';
import BooksReducers from './books.reducer';
import AuthenticationReducer from './authentication.reducer';

const rootReducer = combineReducers({
	book: BookReducers,
	books: BooksReducers,
	authentication: AuthenticationReducer
});

export default rootReducer;
