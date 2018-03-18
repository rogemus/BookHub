import {_get} from './axios.actions';
import {GET_BOOKS} from './types';

export function getBooks(filters) {
	const config = {
		path: 'books',
		type: GET_BOOKS,
		params: filters || {}
	};

	return _get(config.path, {params: config.params}, config.type);
}
