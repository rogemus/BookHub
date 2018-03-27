import {_post} from './axios.actions';
import {LOGIN, REGISTER} from './types';

export function login(credential) {
	const config = {
		path: 'accounts/login',
		params: credential,
		type: LOGIN,
		redirect: ''
	};

	return _post(config.path, config.params, config.type, config.redirect);
}

export function register(data) {
	const config = {
		path: 'accounts/register',
		params: data,
		type: REGISTER,
		redirect: '/'
	};

	return _post(config.path, config.params, config.type, config.redirect);
}
