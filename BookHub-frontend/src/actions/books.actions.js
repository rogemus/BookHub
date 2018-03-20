import {_get} from './axios.actions';
import {GET_BOOKS} from './types';

export function getBooks(filters) {
	const config = {
		path: 'books',
		type: GET_BOOKS,
		params: {}
	};

	return _get(config.path, config.params, config.type);
}
