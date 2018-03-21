import {_post} from './axios.actions';
import {LOG_IN_USER} from './types';

/* TODO BOOK-33 */
export function postUserCredential(credential) {
	const config = {
		path: 'login',
		params: credential,
		type: LOG_IN_USER
	};

	return _post(config.path, config.params, config.type);
}
