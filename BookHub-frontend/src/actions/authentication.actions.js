import {_post} from './axios.actions';
import {GET_TOKEN} from './types';

export function postUserCredential(credential) {
	const config = {
		path: 'auth/login',
		params: credential,
		type: GET_TOKEN
	};

	return _post(config.path, config.params, config.type);
}
