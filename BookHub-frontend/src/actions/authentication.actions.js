import { _postLogin, _post } from './axios.actions';
import { ERRORS, LOGIN, REGISTER, SET_CURRENT_USER, SET_TOKEN } from './types';

export function login(credential) {
	const config = {
		path: 'accounts/login',
		params: credential,
		redirect: '/'
	};

	return _postLogin(config.path, config.params, config.redirect);
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

export function logOutUser() {
	return (dispatch) => {
		dispatch({
			type: LOGIN,
			payload: false
		});

		dispatch({
			type: SET_TOKEN,
			payload: ''
		});

		dispatch({
			type: SET_CURRENT_USER,
			payload: {}
		});

		localStorage.setItem('currentUser', JSON.stringify({}));
		localStorage.setItem('token', JSON.stringify(''));
		localStorage.setItem('isUserLogin', JSON.stringify(false));
	};
}
