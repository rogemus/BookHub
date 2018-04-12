import axios from 'axios';
import {
	ERRORS,
	SET_CURRENT_USER
} from './types';

/* eslint-disable */

// #if process.env.NODE_ENV === 'production'
import API_URL from '../configs/api.prod.config';
// #endif

// #if process.env.NODE_ENV !== 'production'
import API_URL from '../configs/api.local.config';
// #endif

/* eslint-enable */

const instance = axios.create({
	headers: {
		accept: 'application/json'
	}
});

export function _get(path, config, actionType) {
	return (dispatch) => {
		return instance.get(`${API_URL}/${path}/`, config)
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

export function _post(path, config, actionType, redirectPath) {
	return (dispatch) => {
		return instance.post(`/${path}/`, config)
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

export function _postLogin(path, config, actionType, redirectPath) {
	return (dispatch) => {
		return instance.post(`/${path}/`, config)
			.then((response) => {
				dispatch({
					payload: response.data,
					type: actionType
				});

				dispatch({
					type: SET_CURRENT_USER,
					payload: {
						email: response.data.email,
						username: response.data.username
					}
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
