import axios from 'axios';
import {
	ERRORS
} from './types';

const API_URL = '/api';

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
