import { _get, _post } from './axios.actions';
import { GET_COMMENTS, CREATE_COMMENT } from './types';

export function getComments(bookID) {
	const config = {
		path: `books/${bookID}/comments`,
		type: GET_COMMENTS
	};

	return _get(config.path, {}, config.type);
}

export function createComment(bookID, comment, token) {
	const config = {
		path: `books/${bookID}/comments`,
		type: CREATE_COMMENT,
		conf: {
			data: {
				text: comment
			},
			headers: {
				'Authorization': `Bearer ${token}`
			}
		}
	};

	return _post(config.path, config.conf, config.type);
}
