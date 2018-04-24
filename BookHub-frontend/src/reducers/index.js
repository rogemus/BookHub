import {
	combineReducers
} from 'redux';

import BookReducers from './book.reducer';
import BooksReducers from './books.reducer';
import AuthenticationReducer from './authentication.reducer';
import ErrorsReducer from './errors.reducers';
import UserReducer from './user.reducer';
import CommentsReducer from './comments.reducer';

const rootReducer = combineReducers({
	book: BookReducers,
	books: BooksReducers,
	authentication: AuthenticationReducer,
	errors: ErrorsReducer,
	user: UserReducer,
	comments: CommentsReducer
});

export default rootReducer;
