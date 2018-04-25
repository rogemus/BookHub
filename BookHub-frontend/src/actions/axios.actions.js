import axios from 'axios';
import {
	ERRORS,
	SET_CURRENT_USER,
	SET_TOKEN,
	LOGIN
} from './types';

const API_URL = '/api';

const instance = axios.create({
	headers: {
		accept: 'application/json'
	}
});

export function _get(path, config, actionType) {
	return (dispatch) => {
		return instance.get(`${API_URL}/${path}/`, {params: config})
			.then((response) => {
				dispatch({
					payload: response.data,
					type: actionType
				});
			})
			.catch((error) => {
				dispatch({
					payload: error,
					type: ERRORS
				});
			});
	};
}

export function _post(path, config, actionType, redirectPath, noApiUrl) {
	const requestConfig = {
		method: 'POST'
	};
	let url = `${API_URL}/${path}/`;

	if (noApiUrl) {
		url = `/${path}/`;
	}

	return (dispatch) => {
		return instance(Object.assign(requestConfig, {url: url}, config))
			.then((response) => {
				dispatch({
					payload: response.data,
					type: actionType
				});

				if (typeof redirectPath !== 'undefined') {
					window.location.hash = redirectPath;
				}
			})
			.catch((error) => {
				dispatch({
					payload: error.response.data,
					type: ERRORS
				});
			});
	};
}

export function _postLogin(path, config, redirectPath) {
	return (dispatch) => {
		return instance.post(`/${path}/`, config)
			.then((response) => {
				const isUserLogin = true;
				const token = response.data.token;
				const user = {
					email: response.data.email,
					username: response.data.username
				};

				dispatch({
					type: LOGIN,
					payload: isUserLogin
				});

				dispatch({
					type: SET_TOKEN,
					payload: token
				});

				dispatch({
					type: SET_CURRENT_USER,
					payload: user
				});

				localStorage.setItem('currentUser', JSON.stringify(user));
				localStorage.setItem('token', JSON.stringify(token));
				localStorage.setItem('isUserLogin', JSON.stringify(isUserLogin));

				if (typeof redirectPath !== 'undefined') {
					window.location.hash = redirectPath;
				}
			})
			.catch((error) => {
				dispatch({
					payload: error.response.data,
					type: ERRORS
				});
			});
	};
}
