import { _get } from './axios.actions';
import { GET_COMMENTS } from './types';

export function getComments(bookID) {
	const config = {
		path: `books/${bookID}/comments`,
		type: GET_COMMENTS
	};

	return _get(config.path, {}, config.type);
}
