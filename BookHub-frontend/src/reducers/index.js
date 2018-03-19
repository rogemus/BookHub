import {
	combineReducers
} from 'redux';

import BookReducers from './book.reducer';
import BooksReducers from './books.reducer';

const rootReducer = combineReducers({
	book: BookReducers,
	books: BooksReducers
});

export default rootReducer;
