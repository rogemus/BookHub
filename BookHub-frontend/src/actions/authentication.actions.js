import {_post} from './axios.actions';
import {GET_TOKEN, REGISTER} from './types';

export function postUserCredential(credential) {
	const config = {
		path: 'auth/login',
		params: credential,
		type: GET_TOKEN
	};

	return _post(config.path, config.params, config.type);
}

export function register(data) {
	const config = {
		path: 'accounts/register',
		params: data,
		type: REGISTER
	};

	return _post(config.path, config.params, config.type);
}
