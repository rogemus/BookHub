import { _postLogin, _post } from './axios.actions';
import { LOGIN, REGISTER } from './types';

export function login(credential) {
	const config = {
		path: 'accounts/login',
		params: credential,
		type: LOGIN,
		redirect: '/'
	};

	return _postLogin(config.path, config.params, config.type, config.redirect);
}

export function register(data) {
	const config = {
		path: 'accounts/register',
		type: REGISTER,
		redirect: '/',
		noApiUrl: true,
		conf: {
			data: data
		}
	};

	return _post(config.path, config.conf, config.type, config.redirect, config.noApiUrl);
}
