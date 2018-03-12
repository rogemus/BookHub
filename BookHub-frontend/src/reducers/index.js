import {
	combineReducers
} from 'redux';
import BooksReducers from './reducer_books';
import ActiveBookReducers from './reducer_active_book';

const rootReducer = combineReducers({
	books: BooksReducers,
	activeBook: ActiveBookReducers
});

export default rootReducer;
