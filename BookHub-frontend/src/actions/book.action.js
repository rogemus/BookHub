import {_get} from './axios.actions';
import {GET_BOOK} from './types';

export function getBook(bookID) {
	const config = {
		path: `books/${bookID}`,
		type: GET_BOOK
	};

	return _get(config.path, {}, config.type);
}
