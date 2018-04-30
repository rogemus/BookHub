import {_get} from './axios.actions';
import {GET_BOOKS} from './types';

export function getBooks(filters) {
	const config = {
		path: 'books',
		type: GET_BOOKS,
		conf: {
			params: filters || {}
		}
	};

	return _get(config.path, config.conf, config.type);
}
